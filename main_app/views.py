from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

def home(request):
  return render(request, 'home.html')

def wayfarer_index(request):
  return render(request, 'wayfarer/index.html')


# --- User Authentication / Authorization --- #
def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request,user)
      return redirect('index')
    else:
      error_message: 'Invalid sign-up, please try again!'
  else:
    form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'signup.html', context)

def profile(request):
  return render(request, 'profile.html')