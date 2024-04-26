from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def track_landing(request):
    return HttpResponse('Track landing page ')


def tracks_index(request):
    return render(request, 'tracks/landing.html')