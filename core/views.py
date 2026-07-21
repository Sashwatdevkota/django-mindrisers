from django.shortcuts import render
from django.http import HttpResponse
from .models import Todolist


def index(request):
    people = [
        {"name": "Alice Johnson", "age": 25, "address": "New York, USA"},
        {"name": "Bob Smith", "age": 30, "address": "London, UK"},
        {"name": "Charlie Brown", "age": 22, "address": "Sydney, Australia"},
    ]
    context = {"body": "Welcome, This is index Page", "people": people}
    return render(request, "index.html", context)


def learning(request):
    return render(request, "learning.html")


def base(request):
    return render(request, "base.html")


def home(request):
    return render(request, "home.html")


def task(request):
    task = Todolist.objects.all()
    context = {"tasks": task}
    return render(request, "task.html", context)


def aboutus(request):
    return HttpResponse("Welcome this is About Us page.")


def contact(request):
    return HttpResponse("Welcome this is Contact page.")


def create_task(request):
    return render(request, "create.html")


def edit_task(request):
    return render(request, "edit.html")
