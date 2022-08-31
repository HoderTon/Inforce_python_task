from django.contrib.auth.models import User
from django.db import models


class Restaurant(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Menu(models.Model):
    DAYS = (('Mo', 'Monday'), ('Tu', 'Tuesday'),
            ('We', 'Wednesday'), ('Th', 'Thursday'),
            ('Fr', 'Friday'), ('Sa', 'Saturday'), ('Su', 'Sunday'))

    menu_name = models.CharField(max_length=200)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    dishes = models.TextField()
    day = models.CharField(max_length=50, choices=DAYS, default='Mo')

    def __str__(self):
        return self.menu_name


class Vote(models.Model):
    voter = models.ForeignKey(User, on_delete=models.CASCADE)
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
