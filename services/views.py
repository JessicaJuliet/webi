from django.shortcuts import render, reverse, get_object_or_404
from .models import Category, Bundle, Addon, Image, Type

from .forms import ProductForm


def all_services(request):
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

    return render(request, 'services/services.html', context)


def service_detail(request, service_id):
    """ A view to show individual service details """

    service = get_object_or_404(Addon, pk=service_id)

    context = {
        'service': service,
    }

    return render(request, 'services/service_detail.html', context)


def add_service(request):
    """ Add a service to the store """
    form = ProductForm()
    template = 'services/add_service.html'
    context = {
        'form': form,
    }

    return render(request, template, context)
