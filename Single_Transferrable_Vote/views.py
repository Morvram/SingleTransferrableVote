from django.shortcuts import render
from django.http import HttpResponse

#Create views here.

def index(request):
    return HttpResponse("Hello, world!")