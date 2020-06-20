from django.db import models
from django.contrib.auth.models import User
import datetime

# Create your models here.
# class MyUser(models.Model):  # Note that parens are optional if not inheriting from another class
#   def __init__(self, first_name, last_name, username, city, joined_date):
#     self.first_name = first_name
#     self.last_name = last_name
#     self.full_name = f"{first_name} {last_name}"
#     self.username = username
#     self.city = city
#     # joined_date = datetime.date(date_joined)
#     self.joined_date = joined_date.strftime("%M %D %Y")

class MyUser(models.Model):
    first_name = models.CharField(max_length=100, default=None)
    last_name = models.CharField(max_length=100)
    full_name = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    city = models.CharField(max_length=100, default=None)
    # joined_date = models.DateField(default=datetime.datetime.now(), blank=True)


def __str__(self):
        return self.name