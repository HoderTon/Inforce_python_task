from .models import Restaurant, Vote, Menu
from rest_framework import serializers


class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = ['id', 'menu_name', 'dishes', 'restaurant']
