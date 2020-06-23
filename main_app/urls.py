from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('wayfarer/', views.wayfarer_index, name='index'),
  path('profile/<int:user_id>/', views.profile, name='profile'),
  path('login/', views.user_login, name='user_login'),
  path('profile/edit', views.user_edit, name='user_edit'),
  path('posts/<int:post_id>/', views.posts_detail, name='posts_detail'),
  path('posts/<int:post_id>/edit', views.posts_edit, name='posts_edit'),
  path('posts/<int:post_id>/delete', views.posts_delete, name='posts_delete'),
  path('cities/', views.city_detail, name='city_detail')
]