from django.db import models
from django.contrib.auth.models import User


class Drink(models.Model):
    name = models.CharField(max_length=100)
    drink_type = models.CharField(max_length=100)


class Rater(models.Model):
    ip_address = models.GenericIPAddressField()
    user = models.ForeignKey(User, null=True)


class Rating(models.Model):
    drink = models.ForeignKey(Drink)
    rating = models.IntegerField()


class Food(models.Model):
    food_type = models.CharField(max_length=100)
    food_name = models.CharField(max_length=100)
    rating = models.DecimalField(decimal_places=2, max_digits=5)
    food_picture = models.URLField(max_length=1024, blank=True, null=True)
