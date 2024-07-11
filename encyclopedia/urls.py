from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:name>", views.article, name="article"),
    path("search", views.search, name="search"),
    path("random", views.random, name="random"),
    path("create new article", views.new_article, name="create_article"),
    path("wiki/<str:name>/edit", views.edit, name="edit")

]
