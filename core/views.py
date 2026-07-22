from django.shortcuts import render, redirect
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
    if request.method == "POST":
        titles = request.POST.get("title")
        descriptions = request.POST.get("description")
        if titles == "" or descriptions == "":
            context = {"error": "Both field are required"}
            return render(request, "create.html", context)
        # Todolist.objects.create(title=titles, description=descriptions)
        # return redirect("/task/")

    return render(request, "create.html")


def complete_task(request, id):
    task = Todolist.objects.get(id=id)
    task.status = True
    task.save()
    return redirect("/task/")


def delete_task(request, id):
    task = Todolist.objects.get(id=id)
    task.delete()
    return redirect("/task/")


def edit_task(request, id):
    task = Todolist.objects.get(id=id)
    context = {"task": task}
    if request.method == "POST":
        titles = request.POST.get("title")
        descriptions = request.POST.get("description")
        task.title = titles
        task.description = descriptions
        task.save()
        return redirect("/task/")
    return render(request, "edit.html", context)

