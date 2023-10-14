from django.http import HttpResponse
from django.shortcuts import render


def demofunction(request):
    return HttpResponse("<font color='red'> Astrology Prediction System </font>")

def homefunction(request):
    return render(request,"index.html")

def aboutfunction(request):
    return render(request,"about.html")

def loginfunction(request):
    return render(request,"login.html")

def contactfunction(request):
    return render(request,"contact.html")

