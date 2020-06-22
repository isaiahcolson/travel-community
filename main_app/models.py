from django.db import models
from django.contrib.auth.models import User
import datetime

class MyUser(models.Model):
    city = models.CharField(max_length=100, default='Add Your City')
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='MyUser')


class User_Post(models.Model):
  title = models.CharField(max_length=100)
  city = models.CharField(max_length=100)
  author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='User_Posts')
  date = models.DateField('Post Date')
  content = models.TextField(max_length=1000)

  def __str__(self):
    return f"{self.get_title_display()} on {self.date}"

  class Meta:
    ordering = ['-date', 'city']