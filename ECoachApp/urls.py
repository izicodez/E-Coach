from django.contrib import admin
from django.urls import path, include
from ECoachApp import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('base', views.base, name='base'),
    path('delete/<list_id>', views.delete, name='delete'),
    path('timer/<list_id>', views.timer, name='timer'),
    path('<list_id>/start', views.start, name='start'),
]