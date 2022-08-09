from urllib import response
import requests

from config import EMAIL, PASSWORD, API_KEY, URL

_HEADERS = {
    "content-type": "application/json",
    "accept": "application/json"
}


_SESSION = requests.session()

def get_all_projects_id():
    path = f"{URL}/api/public/projectservice/all/projects/ids"
    params = {
        "api_key": API_KEY
        }

    try:
        response = _SESSION.get(url=path, 
            params=params, headers=_HEADERS, timeout=10)

        response = response.json()
        return response
    except Exception as err:
        print(err)

def get_all_projects(next_project_id=None, summary=False):
    """
        next_project_id - The next id of the project if there is 
        any.

        summary - Return full version of the projects if summary 
        is not defined. And if the summary is argument is true 
        return the summary of the projects
    """
    path = f"{URL}/api/public/projectservice/all/projects"
    summary_path = f"{URL}/api/public/projectservice/all/projects/summary"
    params = {
        "api_key": API_KEY
        }

    if next_project_id is not None:
        params["nextProjectId"] = next_project_id

    try:
        if not summary:
            res = _SESSION.get(url=path,
            params=params, headers=_HEADERS)
        else:
            res = _SESSION.get(url=summary_path,
            params=params, headers=_HEADERS)

        response = res.json()
        return response["projects"]
        
        # {
        #     "has_next": response["projects"]["hasNext"],
        #     "next_project_Id": response["projects"]["nextProjectId"],
        #     "projects": response["projects"]["project"]
        #     }

    except Exception as err:
        get_all_projects(next_project_id, summary)

def search_for_projects(search_keyword, start=0, **filter):
    path = "/api/public/services/search/projects"

    params = {
        "api_key": API_KEY,
        "q": search_keyword,
        "start": start,
        "filter": filter
        }

    try:
        response = _SESSION.get(f"{URL}{path}", 
        params=params, headers=_HEADERS)

        response = response.json()

        return response

    except Exception as err:
        print(err)

def get_all_themes():
    path = f"{URL}/api/public/projectservice/themes"

    param = {
        "api_key": API_KEY
    }

    try:
        response = _SESSION.get(url=path, 
        params=param, headers=_HEADERS)

        response = response.json()

        return response

    except Exception as err:
        print(err)

def get_project_with_theme(theme_Id):
    path = f"{URL}/api/public/projectservice/themes/{theme_Id}/projects"

    param = {
        "api_key": API_KEY,
    }

    try:
        response = _SESSION.get(url=path, 
        params=param, headers=_HEADERS)

        response = response.json()

        return response

    except Exception as err:
        print(err)

def get_all_organization(variation="all"):
    path = f"{URL}/api/public/orgservice/all/organizations/{variation}"
    
    if variation == "all":
        path = f"{URL}/api/public/orgservice/all/organizations"
    
    param = {
        "api_key": API_KEY
    }

    try:
        response = _SESSION.get(url=path, 
        params=param, headers=_HEADERS)

        response = response.json()

        return response

    except Exception as err:
        print(err)

def get_all_projects_for_organization(organization_Id, active=False, summary=False):
    path = f"{URL}/api/public/projectservice/organizations/{organization_Id}/projects"
    if active:
        path = f"{URL}/api/public/projectservice/organizations/{organization_Id}/projects/summary"
        
    if summary:
        path += "/summary"

    param = {
        "api_key": API_KEY
    }
    try:
        response = _SESSION.get(url=path, 
        params=param, headers=_HEADERS)

        response = response.json()

        return response

    except Exception as err:
        print(err)

def get_access_token():
    path = f"{URL}/api/userservice/tokens"

    auth_data = {
        "auth_request": {
            "user": {
                "email": EMAIL,
                "password": PASSWORD
            },
            "api_key": API_KEY
        }
    }

    try:
        response = _SESSION.post(url=path, headers=_HEADERS, json=auth_data)
        res = response.json()
        return res["auth_response"]["access_token"]
    except Exception as err:
        print(err)
        
def donate_to_projects():
    pass

def get_data_from_api(api_method):
    """
    -Get api items from each function 
    requesting the api method

    -This serve as the entry point for 
      all the api method used
    """
    try:
        api = api_method()
    except Exception:
        return get_data_from_api(api_method)
    
    return api

if __name__ == "__main__":

    
    response = search_for_projects("flood", country="IN")
    print(response)