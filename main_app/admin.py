from django.contrib import admin
from .models import MyUser, User_Post

# Register your models here.
admin.site.register(MyUser)
admin.site.register(User_Post)