from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('wayfarer/', views.wayfarer_index, name='index'),
  path('profile/', views.profile, name='profile'),
  path('login/', views.user_login, name='user_login'),
  path('profile/edit', views.user_edit, name='user_edit'),
]