from django.shortcuts import render
from .models import Restaurant, Menu, Vote
from rest_framework import generics, permissions
from .serializers import MenuSerializer, VoteSerializer, RestaurantSerializer
from rest_framework.exceptions import ValidationError
from datetime import date
import calendar
from django.db.models import Count


# Menu


class MenuList(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class MenuRetrieveDestroy(generics.RetrieveDestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class MenuTodayList(generics.ListAPIView):
    today = calendar.day_name[date.today().weekday()][:2]
    queryset = Menu.objects.filter(day=today)
    serializer_class = MenuSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class MostVotedMenu(generics.ListAPIView):
    serializer_class = MenuSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        all_votes = Vote.objects.values('menu').order_by('menu').annotate(the_count=Count('menu'))
        menu_and_votes = sorted([(x['menu'], x['the_count']) for x in all_votes], key=lambda x: x[1], reverse=True)
        menu_day = [Menu.objects.get(pk=x[0]) for x in menu_and_votes]
        today = calendar.day_name[date.today().weekday()][:2]
        most_voted = [x.id for x in menu_day if x.day == today]

        return Menu.objects.filter(pk=most_voted[0], day=today)

# Restaurant


class RestaurantCreate(generics.CreateAPIView):
    serializer_class = RestaurantSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        name = self.request.POST.get('name')
        return Restaurant.objects.filter(name=name)

    def perform_create(self, serializer):
        if self.get_queryset().exists():
            raise ValidationError('This restaurant has already been added!')
        serializer.save(name=self.request.POST.get('name'))

# Votes


class VoteCreate(generics.CreateAPIView):
    serializer_class = VoteSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        menu = Menu.objects.get(pk=self.kwargs['pk'])
        return Vote.objects.filter(voter=user, menu=menu)

    def perform_create(self, serializer):
        if self.get_queryset().exists():
            raise ValidationError('You already voted for this menu :)')
        serializer.save(voter=self.request.user, menu=Menu.objects.get(pk=self.kwargs['pk']))



