from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def start_view(request):
    return HttpResponse("Just a lowly turtle here.")


def turtles(request):
    return HttpResponse("Now there are two lowly turtles!!")


def more_turtles(request):
    return HttpResponse("There are turtles everywhere!!!")


def turtle_facts(request):
    return HttpResponse("Thank you for subscribing to Turtle Facts")


def truth(request):
    return HttpResponse("The truth is that it's TURTLES ALL THE WAY DOWN!!!")


def realtruth(request):
    return HttpResponse("Thank you for subscribing to Cat Facts!")