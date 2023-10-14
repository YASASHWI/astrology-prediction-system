from django.urls import path
from . import views


urlpatterns = [

    path("", views.loginpage, name="loginpage"),
    path("registrationpage", views.registrationpage, name="registrationpage"),
    path("aboutpage",views.aboutpage,name="aboutpage"),
    path("contactpage",views.contactpage,name="contactpage"),


    ]