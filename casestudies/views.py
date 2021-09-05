from django.shortcuts import render
from .models import Casestudy


def casestudies(request):
    """ A view to return the case studies page """
    casestudies = Casestudy.objects.all()
    context = {
        'casestudies': casestudies,
    }

    return render(request, 'casestudies/casestudies.html', context)
