from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    # Blog page URL
    path('', views.blog, name='blog'),
    # Individual blog post URL
    path('<slug:slug>/', views.blog_post, name='blog_post'),
]
