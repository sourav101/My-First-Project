from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def dhoni(request):
    return HttpResponse("<marquee><h2>best captain in the world</h2></marquee>")