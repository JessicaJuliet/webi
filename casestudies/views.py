from django.shortcuts import render, get_object_or_404
from .models import Casestudy


def casestudies(request):
    """ A view to return the case studies page """

    casestudies = Casestudy.objects.all()

    context = {
        'casestudies': casestudies,
    }

    return render(request, 'casestudies/casestudies.html', context)


def casestudy_content(request, slug):
    """ A view to show individual case study pages """

    casestudy = get_object_or_404(Casestudy, slug=slug)

    context = {
        'casestudy': casestudy,
    }

    return render(request, 'casestudies/casestudy_content.html', context)
