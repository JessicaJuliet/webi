from django.urls import path
from . import views

urlpatterns = [
    # About page URL
    path('', views.about, name='about')
]
