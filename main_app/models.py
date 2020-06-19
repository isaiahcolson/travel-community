from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class User:  # Note that parens are optional if not inheriting from another class
  def __init__(self, first_name, last_name, username, city, year, month, day):
    self.first_name = first_name
    self.last_name = last_name
    self.full_name = f"{first_name} {last_name}"
    self.username = username
    self.city = city
    joined_date = datetime.datetime(year, month, day)
    self.joined_date = (joined_date.strftime("%B %Y"))