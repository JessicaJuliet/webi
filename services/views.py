from django.shortcuts import render
from .models import Category, Bundle, Addon, Image, Type


def addons(request):
    """ A view to return the Add-ons page """

    addons = Addon.objects.all()

    context = {
        'addons': addons,
    }
    return render(request, 'services/addons.html', context)
