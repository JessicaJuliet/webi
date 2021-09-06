from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog, name='blog'),
    path('<slug:slug>/', views.blog_post, name='blog_post'),
]
