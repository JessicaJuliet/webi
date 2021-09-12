from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('addons', views.addons, name='addons'),
    path('bundles', views.bundles, name='bundles'),
]
