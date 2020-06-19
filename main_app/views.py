from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

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

def wayfarer_index(request):
  return render(request, 'wayfarer/index.html')



class User:  # Note that parens are optional if not inheriting from another class
  def __init__(self, first_name, last_name, username, city, joined_date):
    self.first_name = first_name
    self.last_name = last_name
    self.full_name = f"{first_name} {last_name}"
    self.username = username
    self.city = city
    self.joined_date = joined_date

users = [
  User('Goofy', 'Goof', 'goofus', 'San Francisco', 4-4-2020)
]

def profile(request):
  context = { 'users' : users }
  return render(request, 'profile.html', context)
