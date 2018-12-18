from django.urls import path
from user_app import views

urlpatterns = [
    path('', views.index, name='home_page'),
    path('users/', views.users, name='users'),
    path('forms/', views.form_name, name='form'),
]
