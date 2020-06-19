from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
import datetime

from .forms import CreateUserForm

def home(request):
  error_message = ''
  if request.method == 'POST':
    form = CreateUserForm(request.POST)
    print(form.errors)
    if form.is_valid():
      user = form.save()
      login(request,user)
      return redirect('profile')
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
    return redirect('profile')
  else:
    error_message: 'Invalid login, please try again!'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'home.html', context)

def wayfarer_index(request):
  return render(request, 'wayfarer/index.html')



class User:  # Note that parens are optional if not inheriting from another class
  def __init__(self, first_name, last_name, username, city, year, month, day):
    self.first_name = first_name
    self.last_name = last_name
    self.full_name = f"{first_name} {last_name}"
    self.username = username
    self.city = city
    joined_date = datetime.datetime(year, month, day)
    self.joined_date = (joined_date.strftime("%B %Y"))

users = [
  User('Goofy', 'Goof', 'goofus', 'San Francisco', 2020, 6, 19)
]

def profile(request):
  context = { 'users' : users }
  return render(request, 'profile.html', context)



class Post:
  def __init__(self, post_id, title, city, author, year, month, day, content):
    self.post_id = post_id
    self.title = title
    self.city = city
    self.author = author
    post_date = datetime.datetime(year, month, day)
    self.post_date = (post_date.strftime("%B %D %Y"))
    self.content = content

posts = [
  Post(0, 'Review of London', 'London', 'Goofy Goof', 2020, 6, 19, 'really old; cheeky people; good pints')
]

def posts_detail(request, post_id):
  # post = Post.objects.get(id=post_id)
  context = { 'post' : posts[post_id] }
  return render(request, 'post.html', context)