from django.contrib import admin
from django.urls import path
from Home import views

urlpatterns = [
    path("",views.index, name='Home'),
    path("about",views.about, name='about'), #if we go to /about then we will be directed to the about function in views
    path("contact",views.contact, name='contact')
]
