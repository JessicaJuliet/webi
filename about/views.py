from django.shortcuts import render
from casestudies.models import Casestudy


def about(request):
    """ A function to render the About page """
    # Import Casestudy model content
    casestudies = Casestudy.objects.all()
    context = {
        'casestudies': casestudies,
    }

    return render(request, 'about/about.html', context)
