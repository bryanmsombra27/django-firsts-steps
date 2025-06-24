from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

# Create your views here.


def index(request):
    return HttpResponse("this works")


def february(request):
    return HttpResponse("this works in february")


def march(request):
    return HttpResponse("learm django")


def monthly_challange(request, month):
    challange_text = None

    if month == "january":
        challange_text = "In January, learn Python"
    elif month == "february":
        challange_text = "In February, learn Django"
    elif month == "march":
        challange_text = "In March, learn JavaScript"
    else:
        return HttpResponseNotFound("Page not found")

    return HttpResponse(challange_text)
