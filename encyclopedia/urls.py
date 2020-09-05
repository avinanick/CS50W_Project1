from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/search", views.search, name="search"),
    path("wiki/new", views.new_page, name="new_page"),
    path("wiki/<str:title>", views.entry, name="entry")
]
