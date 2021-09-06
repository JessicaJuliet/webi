from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.casestudies, name='casestudies'),
    path('<slug:slug>/', views.casestudy_content, name='casestudy_content'),
]
