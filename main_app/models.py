from django.db import models
from datetime import datetime
# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    city = models.CharField(max_length=15)
    date = models.DateField(default=datetime.now(), blank=True)



class City(models.Model):
    city = models.CharField(max_length=15)
    attractions = models.CharField(max_length=100)
    review = models.CharField(max_length=450)
    rating = models.IntegerField()

class Post(models.Model):
    name = models.CharField(max_length=100)
    review = models.CharField(max_length=450)
    rating = models.IntegerField()
    date = models.DateField(default=datetime.now(), blank=True)
