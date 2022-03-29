from django.contrib import admin
from django.urls import path, include
from ECoachApp import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('base', views.base, name='base'),
]