from urllib import request

from django.http import HttpResponse
from django.shortcuts import render

from taskapp.models import Place

# Create your views here.
"""def home(request):
    #return HttpResponse("this is my home page")
def about(request):
    return render(request,'about.html')
def contract(request):
    return render(request,'contract.html')
def details(request):
    return render(request,'details.html')
def thanks(request):
    return HttpResponse("thanks")"""
def index(request):
    obj = Place.objects.all()
    return render(request,'index.html',{'result':obj})
