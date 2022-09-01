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
    get_access_token, get_all_projects, get_all_projects_id, get_organization, get_project_with_id, search_for_projects, 
    get_all_themes, get_all_projects_with_theme, get_all_organizations, get_featured_projects,
    get_all_projects_for_organization, submit_donation_to_project
    )
from .api_helpers import flatten_projects, get_isocountrycode

# @cache_page(60 * 60 * 24)
def home(request):
    try:
        themes = get_all_themes()
        projects = get_all_projects_id()
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
    except:
        return render(request, "geeve/404.html")

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
        
def page_not_found(request):
    return render(request, "geeve/404.html")

def organization_details_by_id(request, organization_id):
    organization = get_organization(organization_id)
    context = {
        "organization": organization
    }

    return render(request, "geeve/organization_details.html", context)

def search_geeve_projects(request):
    if request.method == 'POST':
        search = request.POST['search']
        project_search = search_for_projects(search)

        context = {
            "project_search": project_search
        }
        
        render(request, "geeve/search_result.html", context)
    else:
        redirect("geeve:projects")

def get_projects_with_theme_id(request, theme_id):
    get_projects = get_all_projects_with_theme(theme_id)
    themes = get_all_themes()
    organizations = get_all_organizations()
    countries = get_isocountrycode()

    context = {
        "theme_projects": get_projects,
        "theme": themes,
        "organizations": organizations,
        "countries": countries
    }

    return JsonResponse(context)

def submit_donation(request, id):
    access_token = get_access_token()

    return HttpResponse(f"{access_token} to be used to donate to {id}")
    # return render(request, "geeve/donation_form.html")
    

def test_view(request):
    context = {
        "name": get_isocountrycode()
    }
    return render(request, "geeve/main.html", context)
