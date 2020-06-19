from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('wayfarer/', views.wayfarer_index, name='index'),
  path('profile/', views.profile, name='profile'),
  path('login/', views.user_login, name='user_login'),
  path('posts/<int:post_id>', views.posts_detail, name='posts_detail'
]