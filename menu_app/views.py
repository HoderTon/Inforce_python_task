from django.shortcuts import render
from .models import Restaurant, Menu, Vote
from rest_framework import generics
from .serializers import MenuSerializer


class MenuList(generics.ListAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

# class AddMenu(generics.CreateAPIView):
#
#     serializer_class = MenuSerializer
#
#     def get_queryset(self):
#         menu = Menu.objects.get(pk=self.kwargs['pk'])



