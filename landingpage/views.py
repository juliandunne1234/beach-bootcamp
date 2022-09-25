from django.shortcuts import render


def index(request):
    """ Return index page """
    return render(request, 'index.html')
