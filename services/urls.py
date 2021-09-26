from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    # Services page URL
    path('', views.all_services, name='services'),
    # Service detail pages URLs
    path('<int:service_id>/', views.service_detail, name='service_detail'),
    # Add/edit/delete services URLs
    path('add/', views.add_service, name='add_service'),
    path('edit/<int:service_id>/', views.edit_service, name='edit_service'),
    path('delete/<int:service_id>/', views.delete_service, name='delete_service'),
]
