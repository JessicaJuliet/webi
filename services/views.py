from django.shortcuts import render, redirect, reverse, get_object_or_404

from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import Service, Type

from .forms import ProductForm


def all_services(request):
    """ A function to return the Services page and filter services by type """

    services = Service.objects.all()
    type = None

    if request.GET:
        if 'type' in request.GET:
            types = request.GET['type'].split(',')
            services = services.filter(type__name__in=types)
            types = Type.objects.filter(name__in=types)

    context = {
        'current_types': type,
        'services': services,
    }

    return render(request, 'services/services.html', context)


def service_detail(request, service_id):
    """ A function to render individual service details """

    service = get_object_or_404(Service, pk=service_id)

    context = {
        'service': service,
    }

    return render(request, 'services/service_detail.html', context)


@login_required
def add_service(request):
    """ A function to allow superusers to add a service to the website """

    if not request.user.is_superuser:
        messages.error(request, 'Sorry, you do not have sufficient privileges \
                                to do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            service = form.save()
            messages.success(request, 'Successfully added service.')
            return redirect(reverse('service_detail', args=[service.id]))
        else:
            messages.error(request, 'Failed to add service. Please ensure the \
                                    form is valid.')
    else:
        form = ProductForm()

    template = 'services/add_service.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_service(request, service_id):
    """ A function to allow superusers to edit a service on the website """

    if not request.user.is_superuser:
        messages.error(request, 'Sorry, you do not have sufficient privileges \
                                to do that.')
        return redirect(reverse('home'))

    service = get_object_or_404(Service, pk=service_id)

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=service)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated service.')
            return redirect(reverse('service_detail', args=[service.id]))
        else:
            messages.error(request, 'Failed to update service. \
                                    Please ensure the form is valid.')
    else:
        form = ProductForm(instance=service)
        messages.info(request, f'You are editing {service.name}')

    template = 'services/edit_service.html'
    context = {
        'form': form,
        'service': service,
    }

    return render(request, template, context)


@login_required
def delete_service(request, service_id):
    """ A function to allow superusers to delete a service from the website """

    if not request.user.is_superuser:
        messages.error(request, 'Sorry, you do not have sufficient \
                                 privileges to do that.')
        return redirect(reverse('home'))

    service = get_object_or_404(Service, pk=service_id)
    service.delete()
    messages.success(request, 'Service deleted!')

    return redirect(reverse('services'))
