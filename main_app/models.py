from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Post(models.Model):
  title = models.CharField(max_length=100)
  city = models.CharField(max_length=20)
  author = models.ForeignKey(User, on_delete=models.CASCADE)
  date = models.DateField(timezone.now())
  content = models.CharField(max_length=500)