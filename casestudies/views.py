from django.shortcuts import render


def casestudies(request):
    """ A view to return the case studies page """
    return render(request, 'casestudies/casestudies.html')
