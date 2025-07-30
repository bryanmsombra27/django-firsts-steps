from django.shortcuts import render
from django.contrib import admin
from django.urls import include, path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("/admin", admin.site.urls),
    path("book/<slug:slug>", views.book_detail, name="book_detail"),
]
