from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create-user/', views.createUser, name='create-user'),
    path('users/', views.users, name='users'),
]