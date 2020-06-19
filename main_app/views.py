from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm

def home(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request,user)
      return redirect('profile')
    else:
      error_message: 'Invalid sign-up, please try again!'
  form = UserCreationForm()
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
  def __init__(self, name, city, joined_date):
    self.name = name
    self.city = city
    self.joined_date = joined_date

users = [
  User('Goofy', 'San Francisco', 4-4-2020)
]

def profile(request):
  context = { 'users' : users }
  return render(request, 'profile.html', context)
