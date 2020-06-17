from django.shortcuts import render
from django.http import HttpResponse

def home(request):
  return HttpResponse('<h1>Test</h1>')

def wayfarer_index(request):
  return render(request, 'wayfarer/index.html')