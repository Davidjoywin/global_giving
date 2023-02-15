from datetime import datetime
from re import A

"""
to be used as isocountrycode in the project search filter

example code:
        alpha.Nigeria.value         results- 'NG'
"""
from isocountrycode.alpha2 import Alpha2 as alpha
from django.template.defaultfilters import slugify
from django.http import HttpResponse, JsonResponse
from django.views.decorators.cache import cache_page
from django.shortcuts import render, redirect
from django.urls import reverse

from .global_giving_api import (
    get_access_token, get_all_projects, get_organization,
    get_project_with_id, search_for_projects, get_all_themes,
    get_all_projects_with_theme, get_all_organizations, get_featured_projects,
    get_all_projects_for_organization, submit_donation_to_project
    )
from .api_helpers import get_isocountrycode, get_theme_name_with_theme_id

# @cache_page(60 * 60 * 24)
def home(request):
    """
    main home of the website. i.e land page of the website
    """
    #try:
    themes = get_all_themes()
    projects = get_all_projects()
    organizations = get_all_organizations()
    countries = get_isocountrycode()
    featured_projects = get_featured_projects()
    
    context = {
        "themes": themes,
        "projects": projects,
        "organizations": organizations,
        "countries": countries,
        "featured_projects": featured_projects
    }
    return render(request, "geeve/main.html", context)

    #except:
     #   return render(request, "geeve/404.html")

def geeve_organizations(request, next_id):
    try:
        themes = get_all_themes()
        organizations = get_all_organizations()
        countries = get_isocountrycode()
        featured_projects = get_featured_projects()

        context = {
            "themes": themes,
            "organizations": organizations,
            "countries": countries,
            "featured_project": featured_projects
        }

        return render(request, "geeve/main.html", context)
    except:
        return render(request, "geeve/404.html")

def get_projects(request):
    """
    list all projects
    """
    projects = get_all_projects()

    context = {
        "projects": projects
    }

    return render(request, "geeve/projects.html", context)

def get_project_details(request, project_id):
    """
    Get project details using the id of the specific is
    """
    try:
        project = get_project_with_id(project_id)
        context = {
            "project": project 
        }
        return render(request, 'geeve/project_details.html', context)
    except:
        return render(request, 'geeve/404.html')
        
def get_projects_number_from_theme_id(request, theme_id):
    """
    list projects associated with a theme id
    """
    get_projects = get_all_projects_with_theme(theme_id)

    context = {
        "theme_projects": get_projects,
    }

    return JsonResponse(context)

def get_projects_from_theme_id(request, theme_id):
    get_projects  = get_all_projects_with_theme(theme_id)
    themes = get_all_themes()
    themes = themes['themes']['theme']
    theme = get_theme_name_with_theme_id(theme_id, themes)
    
    context = {
        "theme": theme,
        "projects": get_projects
    }
    return render(request, "geeve/projects.html", context)

def submit_donation(request, id):
    """
    Submit a donation to a project through its id
    """

    access_token = get_access_token()

    submit_donation_to_project(access_token)
    return HttpResponse(f"{access_token} to be used to donate to {id}")
    # return render(request, "geeve/donation_form.html")

def page_not_found(request):
    return render(request, "geeve/404.html")

def organization_details_by_id(request, organization_id):
    """
    details on organization. Like organization profile
    """

    organization = get_organization(organization_id)
    context = {
        "organization": organization
    }
    try:
        return render(request, "geeve/organization_details.html", context)
    except:
        return render(request, "geeve/404.html", context)

def projects_from_organization(request, organization_id):
    """
    list organization based on a particular organization
    """

    projects = get_all_projects_for_organization(organization_id)
    organization = get_organization(organization_id)

    context = {
        "projects": projects,
        "organization": organization
    }
    return render(request, "geeve/organization_projects.html", context)

def search_geeve_projects(request):
    """
    Searching for projects using filter and and search form
    """

    if request.method == 'POST':
        search = request.POST['search']
        project_search = search_for_projects(search)

        context = {
            "project_search": project_search
        }
        
        render(request, "geeve/search_result.html", context)
    else:
        redirect("geeve:projects")

    

def test_view(request):
    """just for testing"""

    context = {
        'names': [1,2,3,4,5,6]
    }
    return render(request, "geeve/test.html", context)
