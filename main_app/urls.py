from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('wayfarer/', views.wayfarer_index, name='index'),
  path('accounts/signup', views.signup, name='signup'),
  path('profile/', views.profile, name='profile')
]