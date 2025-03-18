from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'home.html')

def about(request):
    return HttpResponse('Home 2')

def contact(request):
    return HttpResponse('Home 3')
# Create your views here.
