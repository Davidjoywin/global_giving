from django.urls import path

from . import views

app_name = "geeve"
urlpatterns = [
    path("", views.home, name="home"),
    path("projects", views.get_projects, name="projects"),
    path("project/<int:project_id>", views.get_project_details, name="project_details"),
    path("<int:next_id>", views.geeve_organizations, name="list_organizations"),
    path("organization/<int:organization_id>", views.organization_details_by_id, name="organization_details"),
    path("organization/<int:organization_id>/projects", views.projects_from_organization, name="organization_projects"),
    path("theme/<str:theme_id>", views.get_projects_number_from_theme_id, name="theme_project"),
    path("theme/<str:theme_id>/projects", views.get_projects_from_theme_id, name="list_projects_from_theme"),
    path("donate/<int:id>", views.submit_donation, name="submit_donation"),
    path("page-not-found", views.page_not_found, name="page_not_found"),
    path("...", views.search_geeve_projects, name="search"),
    path("test", views.test_view, name="test"),
]
