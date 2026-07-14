from django.contrib import admin
from django.urls import path, include
from core.views import *

urlpatterns = [
    path("admin/", admin.site.urls),
    path("index/", index),
    path("home/", home),
    path("aboutus/", aboutus),
    path("contact/", contact),
    path("learning/", learning),
    path("base/", base),
]
