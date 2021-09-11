from django.shortcuts import render
from casestudies.models import Casestudy


def about(request):
    """ A view to return the about page """
    casestudies = Casestudy.objects.all()
    context = {
        'casestudies': casestudies,
    }

    return render(request, 'about/about.html', context)
