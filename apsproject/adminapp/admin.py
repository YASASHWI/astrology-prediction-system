from django.contrib import admin
from django.shortcuts import render


# Register your models here.
def adminhome(request):
    return render(request,"adminhome.html")
