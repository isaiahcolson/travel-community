from django.db import models
from django.contrib.auth.models import User
import datetime

class MyUser(models.Model):
    city = models.CharField(max_length=100, default='Add Your City')
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='MyUser')


# update city to a FK after City model creation
class User_Post(models.Model):
  title = models.CharField(max_length=100)
  date = models.DateField('Post Date', default=datetime.date.today)
  content = models.TextField(max_length=1000)
  city = models.CharField(max_length=100)
  user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='User_Posts')

  def __str__(self):
    return f"{self.title} on {self.date}"

  class Meta:
    ordering = ['-date', 'city']