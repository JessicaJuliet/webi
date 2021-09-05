from django.shortcuts import render
# Resource: https://stackoverflow.com/questions/31406662/django-unable-to-import-model-from-another-app
from casestudies.models import Casestudy

# Create your views here.


def index(request):
    """A view to return the homepage (index)"""
    casestudies = Casestudy.objects.all()
    context = {
        'casestudies': casestudies,
    }

    return render(request, 'home/index.html', context)
