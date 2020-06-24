from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import UserChangeForm
import datetime

from .forms import CreateUserForm, EditUserForm, Post_Form
from .models import User
from .models import MyUser, User_Post, City


# --- TEMPORARY POST MODEL --- #
class Post:
  def __init__(self, post_id, title, city, author, year, month, day, content):
    self.post_id = post_id
    self.title = title
    self.city = city
    self.author = author
    post_date = datetime.datetime(year, month, day)
    self.post_date = (post_date.strftime("%B %Y"))
    self.content = content

posts = [
  Post(0, 'Review of London', 'London', 'Goofy Goof', 2020, 6, 19, 'lots of history; cheeky people; good pints'),
  Post(1, 'Good Times in Montreal', 'Montreal', 'Goofy Goof', 2020, 6, 20, 'eclectic neighborhoods; great views from the top of Mount Royal')
]


def home(request):
  error_message = ''
  if request.method == 'POST':
    form = CreateUserForm(request.POST)
    print(form.errors)
    if form.is_valid():
      user = form.save()
      new_user = MyUser(user_id=user)
      new_user.save()
      login(request,user)
      return redirect('profile', user_id=user.pk)
    else:
      error_message: 'Invalid sign-up, please try again!'
  form = CreateUserForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'home.html', context)

def user_login(request):
  error_message = ''
  username = request.POST["username"]
  password = request.POST["password1"]
  user = authenticate(username=username, password=password)
  if user is not None:
    login(request,user)
    return redirect('profile', user_id=user.pk)
  else:
    error_message: 'Invalid login, please try again!'
  context = {'error_message': error_message}
  return render(request, 'home.html', context)

def wayfarer_index(request):
  return render(request, 'wayfarer/index.html')


def profile(request, user_id, city='Add Your City'):
  users = User.objects.get(pk=user_id)
  users_id = MyUser.objects.get(user_id=user_id)
  city = users_id.city
  post_form = Post_Form()
  context = { 'users': users, 'city': city, 'post': posts, 'post_form': post_form }
  return render(request, 'profile.html', context)

def user_edit(request):
  new_city = request.POST.get('city', '')
  current_user = request.user
  users_id = MyUser.objects.get(user_id=current_user.id)
  users_id.city = new_city
  users_id.save(update_fields=['city'])
  if request.method == 'POST':
    edit_form = EditUserForm(request.POST, instance=request.user)
    if edit_form.is_valid():
      edit_form.save()
      return redirect('profile', user_id=current_user.pk)
  else:
    edit_form = UserChangeForm(instance=request.user)
  context = { 'edit_form':edit_form, 'current_user':current_user }
  return render(request, 'profile.html', context)


# --- CITY ROUTES --- #
# Define the CITY_index view
def city_index(request):
  city = City.objects.all()
  context = { 'city':city }
  return render(request, 'city.html', context)

# Define the CITY_detail view
def city_detail(request, city_id):
  city = City.objects.all()
  city_id = City.objects.get(id=city_id)
  if request.method == 'POST':
    post_form = Post_Form(request.POST)
    if post_form.is_valid():
      new_post = post_form.save(commit=False)
      new_post.user = request.user
      new_post.city_id = city_id.id
      new_post.save()
      return redirect("city_detail", city_id=city_id.id)
  else:
    post_form = Post_Form()
  # post_form = Post_Form()
  post = User_Post.objects.filter(user=request.user)
  context = { 'city':city, 'city_id':city_id, 'post_form': post_form, 'post': post }
  return render(request, 'city/detail.html', context)


# --- POST ROUTES (C.R.U.D.) --- #
# def add_post(request):
#   if request.method == 'POST':
#     post_form = Post_Form(request.POST)
#     if post_form.is_valid():
#       new_post = post_form.save(commit=False)
#       new_post.user = request.user
#       # new_post.city_id = city_id
#       new_post.save()
#       return redirect("city_detail", new_post.city.id)
      # return redirect("city_detail", city_id=city_id)
  # else:
  #   post_form = Post_Form()
  # posts = User_Post.objects.filter(user=request.user)
  # context = { 'post': posts, 'post_form': post_form }
  # return render(request, 'profile.html', context)

def posts_detail(request, post_id):
  post = User_Post.objects.get(id=post_id)
  context = { 'post':post }
  return render(request, 'posts/detail.html', context)

def posts_edit(request, post_id):
  error_message = ''
  post = User_Post.objects.get(id=post_id)
  if request.method == 'POST':
    post_form = Post_Form(request.POST, instance=post)
    if post_form.is_valid():
      print('valid')
      post_form.save()
      return redirect('posts_detail', post_id=post_id)
    else:
      print('not valid')
  else:
    print('check3')
    post_form = Post_Form(instance=post)
  print('end check')
  context = { 'post':post, 'post_form':post_form }
  return render(request, 'posts/detail.html', context)

# update redirect to city index/detail page once city model and detail page is created
def posts_delete(request, post_id):
  User_Post.objects.get(id=post_id).delete()
  return redirect('home')
