from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.all_services, name='services'),
    path('<service_id>', views.service_detail, name='service_detail'),
    path('bundles/', views.bundles, name='bundles'),
    path('<slug:slug>/', views.bundle_details, name='bundle_details'),
    path('add', views.add_product, name='add_product'),
]
