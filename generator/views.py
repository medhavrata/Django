from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def root(request):
    return HttpResponse('This is root')

def user(request):
    return HttpResponse("This is return for User")
