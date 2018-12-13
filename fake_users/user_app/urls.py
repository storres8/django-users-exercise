from django.contrib import admin
from django.urls import path
from user_app import views

urlpatterns = [
    path('', views.index, name='home_page'),
    path('user/', views.users, name='users')
]
