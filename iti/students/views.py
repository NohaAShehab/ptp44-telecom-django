from django.shortcuts import render
from django.http import HttpResponse
# Create your views here. #
# define view as a function

# handle http request
def hello(request):
    return HttpResponse("<h1 style='text-align:center;color:red'> Hello World! from my student appliction </h1>")


def aboutus(request):
    return HttpResponse("<h2 style='text-align:center;'> About us page</h2>")


def landing(request):
    return HttpResponse("<h1 style='text-align:center;color:green'> Welcome to ITI website </h1>")