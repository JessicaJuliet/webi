from django.shortcuts import render, reverse
from .models import Category, Bundle, Addon, Image, Type


def addons(request):
    """ A view to return the Add-ons page and filter addons by type """

    addons = Addon.objects.all()
    types = None

    if request.GET:
        if 'type' in request.GET:
            types = request.GET['type'].split(',')
            addons = addons.filter(type__name__in=types)
            types = Type.objects.filter(name__in=types)

    context = {
        'addons': addons,
        'current_types': type,
    }

    return render(request, 'services/addons.html', context)


def bundles(request):
    """ A view to render the Bundles page """

    bundles = Bundle.objects.all()
    addons = Addon.objects.all()

    context = {
        'bundles': bundles,
        'addons': addons,
    }

    return render(request, 'services/bundles.html', context)
