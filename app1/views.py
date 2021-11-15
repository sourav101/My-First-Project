from django import http
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def rohit(request):
    return HttpResponse("<marquee><h2>best opener in the world</h2></marquee>")