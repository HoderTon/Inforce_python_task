from .models import Restaurant, Vote, Menu
from rest_framework import serializers


class MenuSerializer(serializers.ModelSerializer):
    votes = serializers.SerializerMethodField()

    class Meta:
        model = Menu
        fields = ['id', 'menu_name', 'dishes', 'restaurant', 'votes', 'day']

    def get_votes(self, menu):
        return Vote.objects.filter(menu=menu).count()


class VoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vote
        fields = ['id']


class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = ['id', 'name']