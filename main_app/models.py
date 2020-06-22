from django.db import models
from django.contrib.auth.models import User
import datetime

class MyUser(models.Model):
    city = models.CharField(max_length=100, default='Add Your City')
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='MyUser')