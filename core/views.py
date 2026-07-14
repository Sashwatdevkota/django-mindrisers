from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Welcome this is index page.")


def home(request):
    return HttpResponse("Welcome this is home page.")


def aboutus(request):
    return HttpResponse("Welcome this is About Us page.")


def contact(request):
    return HttpResponse("Welcome this is Contact page.")
