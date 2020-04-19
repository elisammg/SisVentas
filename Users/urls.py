from django.contrib import admin
from django.urls import path
from Users import views

urlpatterns = [
    path('welcome/', views.welcome),
    path('register', views.register),
    path('', views.login),
    path('logout/', views.logout),
]