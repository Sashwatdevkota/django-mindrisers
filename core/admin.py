from django.contrib import admin
from .models import Todolist
from .models import NoteApp


@admin.register(Todolist)
class TodolistAdmin(admin.ModelAdmin):
    list_display = ("title", "description", "status")


@admin.register(NoteApp)
class NoteAppAdmin(admin.ModelAdmin):
    list_display = ("title", "description", "date")


# Register your models here.
# admin.site.register(Todolist, TodolistAdmin)
# admin.site.register(NoteApp, NoteAppAdmin)
