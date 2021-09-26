from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    # Case Studies page URL
    path('', views.casestudies, name='casestudies'),
    # Individual Case Studies URLs
    path('<slug:slug>/', views.casestudy_content, name='casestudy_content'),
]
