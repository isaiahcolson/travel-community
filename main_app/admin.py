from django.contrib import admin
from .models import MyUser, City, User_Post

# Register your models here.
admin.site.register(MyUser)
admin.site.register(City)
admin.site.register(User_Post)
