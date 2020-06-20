from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import UserChangeForm
import datetime

from .forms import CreateUserForm, EditUserForm
from .models import User



def home(request):
  error_message = ''
  if request.method == 'POST':
    form = CreateUserForm(request.POST)
    print(form.errors)
    if form.is_valid():
      user = form.save()
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

def profile(request, user_id):
  users = User.objects.get(pk=user_id)
  context = { 'users' : users }
  return render(request, 'profile.html', context)

def user_edit(request):
  current_user = request.user
  if request.method == 'POST':
    edit_form = EditUserForm(request.POST, instance=request.user)
    if edit_form.is_valid():
      edit_form.save()
      return redirect('profile', user_id=current_user.pk)
  else:
    edit_form = UserChangeForm(instance=request.user)
  context = {'edit_form': edit_form, 'current_user': current_user}
  return render(request, 'profile.html', context)


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
  Post(0, 'Review of London', 'London', 'Goofy Goof', 2020, 6, 19, 'really old; cheeky people; good pints')
]

def posts_detail(request, post_id):
  # post = Post.objects.get(id=post_id)
  context = { 'post' : posts[post_id] }
  return render(request, 'post.html', context)
