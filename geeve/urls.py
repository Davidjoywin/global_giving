from django.urls import path

from . import views

app_name = "geeve"
urlpatterns = [
    path("", views.home, name="home"),
    path("<int:next_id>", views.geeve_organizations, name="list_organizations"),
    path("organization/<int:organization_id>", views.organization_details_by_id, name="organization_details"),
    path("theme/<str:theme_id>", views.get_projects_with_theme_id, name="theme_project"),
    path("donate/<int:id>", views.submit_donation, name="submit_donation"),
    path("<slug:rev>", views.page_not_found, name="page_not_found"),
    path("...", views.search_geeve_projects, name="search"),
    path("test", views.test_view, name="test"),
]
