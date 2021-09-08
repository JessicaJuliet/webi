from django.shortcuts import render
from .models import Category, Bundle, Addon, Image, Type


def addons(request):
    """ A view to return the Add-ons page """

    return render(request, 'services/addons.html')
