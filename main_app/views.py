from django.shortcuts import render
from django.http import HttpResponse

def home(request):
  return render(request, 'home.html')

def wayfarer_index(request):
  return render(request, 'wayfarer/index.html')