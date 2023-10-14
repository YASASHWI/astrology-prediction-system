from django.shortcuts import render

# Create your views here.

def loginpage(request):
    return render(request,"loginpage.html")

def registrationpage(request):
    return render(request,"registrationpage.html")

def aboutpage(request):
    return render(request,"aboutpage.html")

def contactpage(request):
    return render(request,"contactpage.html")
