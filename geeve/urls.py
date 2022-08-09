from django.urls import path

from . import views

app_name = "geeve"
urlpatterns = [
    path("", views.home, name="home"),
    path("<int:next_id>", views.geeve_projects, name="projects"),
    path("search", views.search, name="search"),
]