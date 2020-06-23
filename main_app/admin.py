from django.contrib import admin
from .models import MyUser, City

# Register your models here.
admin.site.register(MyUser)
admin.site.register(City)