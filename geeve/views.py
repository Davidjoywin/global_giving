from datetime import datetime
from this import d

from django.shortcuts import render, redirect
from django.urls import reverse

from .global_giving_api import get_all_projects, search_for_projects
from .api_helpers import flatten_projects

projects = []

def home(request):
    return redirect(reverse("geeve:projects", args=(2,)))

def geeve_projects(request, next_id=2):
    get_projects = get_all_projects(next_project_id=next_id)
    next_project_id = get_projects["nextProjectId"]
    project = get_projects["project"]
    projects.extend(flatten_projects(project))

    context = {
        "next_project_id": next_project_id,
        "projects": projects
    }

    return render(request, "geeve/home.html", context)

def search_geeve_projects(request):
    pass