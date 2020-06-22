from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import UserChangeForm
import datetime

from .forms import CreateUserForm, EditUserForm
from .models import User
from .models import MyUser, User_Post


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
      user = form.save(commit=False)
      user.save()
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
  context = { 'users': users, 'city': city, 'post': posts }
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
      # city = users_id.city
      return redirect('profile', user_id=current_user.pk)
  else:
    edit_form = UserChangeForm(instance=request.user)
  context = {'edit_form': edit_form, 'current_user': current_user}
  return render(request, 'profile.html', context)

def posts_detail(request, post_id):
  post = User_Post.objects.get(id=post_id)
  context = { 'post' : post }
  return render(request, 'post.html', context)
