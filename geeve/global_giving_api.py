from uuid import uuid4
import requests
import logging

from .config import EMAIL, PASSWORD, API_KEY, URL

_HEADERS = {
    "content-type": "application/json",
    "accept": "application/json"
}


_SESSION = requests.session()

logging.basicConfig(
    filename="global_giving.log", format= '%(asctime)s %(message)s', 
    level=logging.WARNING
    )

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
    except requests.exceptions.RequestException as err:
        raise "Requests Exception found."
        logging.warning(err)

def get_project_with_id(project_id):
    path = f"{URL}/api/public/projectservice/projects/collection/ids"
    params = {
        "api_key": API_KEY,
        "projectIds": project_id
        }

    try:
        response = _SESSION.get(url=path, 
            params=params, headers=_HEADERS, timeout=10)

        response = response.json()
        return response

    except requests.exceptions.RequestException as err:
        raise "Requests Exception found."
        logging.warning(err)

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
        return response

    except requests.exceptions.RequestException as err:
        raise "Requests Exception found."
        logging.warning(err)
        # get_all_projects(next_project_id, summary)

# create a decarator recursively request paginated api method

def request_more(api_method):
    def wrapper(project_id):
        has_next = True
        available_response = api_method(project_id)
        next_project_id = available_response["projects"]["nextProjectId"]

        while (has_next):        
            available_response = api_method(next_project_id)
            next_project_id = available_response["projects"]["project"]
            available_list = available_response["projects"]["project"]
            number_found = available_response["projects"]["numberFound"]
            try:
                has_next = available_response["projects"]["hasNext"]
            except Exception:
                has_next = False
    
       
def get_featured_projects(summary=False):
    path = "/api/public/projectservice/featured/projects"

    if summary:
        path = "/api/public/projectservice/featured/projects/summary"

    params = {
        "api_key": API_KEY,
    }

    try:
        response = _SESSION.get(f"{URL}{path}",
        params=params, headers=_HEADERS)
        
        response = response.json()

        return response
    except requests.exceptions.RequestException as err:
        raise "Requests Exception found."
        logging.warning(err)

def search_for_projects(search_keyword, start=0, **filter):
    path = "/api/public/services/search/projects"

    filter_format = [
        f"{key}:{value}" 
        for key, value in filter.items()
        ]

    filter = ",".join(filter_format)
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

    except requests.exceptions.RequestException as err:
        raise "Requests Exception found."
        logging.warning(err)

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

    except requests.exceptions.RequestException as err:
        raise "Requests Exception found."
        logging.warning(err)

def get_all_projects_with_theme(theme_Id):
    path = f"{URL}/api/public/projectservice/themes/{theme_Id}/projects"

    param = {
        "api_key": API_KEY,
    }

    try:
        response = _SESSION.get(url=path, 
        params=param, headers=_HEADERS)

        response = response.json()

        return response

    except requests.exceptions.RequestException as err:
        raise "Requests Exception found."
        logging.warning(err)

def get_organization(organization_id):
    path = f"{URL}/api/public/orgservice/organization/{organization_id}"

    param = {
        "api_key": API_KEY
    }

    try:
        response = _SESSION.get(url=path,
        params=param, headers=_HEADERS)

        response = response.json()

        return response

    except requests.exceptions.RequestException as err:
        raise "Requests Exception found."
        logging.warning(err)
        

def get_all_organizations(variation="all"):
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

    except requests.exceptions.RequestException as err:
        raise "Requests Exception found."
        logging.warning(err)

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

    except requests.exceptions.RequestException as err:
        raise "Requests Exception found."
        logging.warning(err)

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

    except requests.exceptions.RequestException as err:
        raise "Requests Exception found."
        logging.warning(err)
        
def submit_donation_to_project(access_token, **donation_data):
    path = f"{URL}/api/secure/givingservice/donationsclient"

    params = {
        "api_key": API_KEY,
        "api_token": access_token,
        "is_test": True
    }

    data = {
        "refcode": str(uuid4()),
        "transactionId": str(uuid4()),
        "email": donation_data["email"],
        "twitter_username": donation_data["twitter_username"],
        "amount": donation_data["amount"],
        "currencyCode": donation_data["currencyCode"],
        "addon": {
            "amount": donation_data["addon_amount"]
        },
        "project": {
            "id": donation_data["project_id"]
        },
        "noteToOrganization": donation_data["note_to_organization"],
        "partnerCode": donation_data["partner_code"],
        "signupForGGNewsletter": donation_data["signup_for_GG_newsletter"],
        "signupForCharityNewsletter": donation_data["signup_for_charity_newsletter"],
        "ipAddress": donation_data["ip_address"],
        "userAgent": donation_data["user_agent"],
        "payment_detail": {
            "firstname": donation_data["payment_detail_firstname"],
            "lastname": donation_data["payment_detail_lastname"],
            "address": donation_data["payment_detail_address"],
            "city": donation_data["payment_detail_city"],
            "state": donation_data["payment_detail_state"],
            "is03166CountryCode": donation_data["payment_detail_country_code"],
            "zip": donation_data["payment_detail_zip"],
            "phone": donation_data["payment_detail_phone"],
            "paymentGateway": donation_data["payment_detail_payment_gateway"],
            "paymentGatewayKey": donation_data["payment_detail_payment_gateway_key"],
            "paymentGatewayNonce": donation_data["payment_detail_payment_gateway_nonce"],
            "paymentGatewaySavedPaymentToken": donation_data["payment_detail_payment_gateway_saved_payment_token"]
        },
        "giftCertificationNumber": donation_data["gift_certification_number"],
        "giftCardDesign": donation_data["giftcard_design"],
        "giftCard_detail": {
            "dateTOSend": donation_data["giftcard_date_to_send"],
            "firstname": donation_data["giftcard_firstname"],
            "lastname": donation_data["giftcard_lastname"],
            "email": donation_data["giftcard_email"],
            "phone": donation_data["giftcard_phone"],
            "to": donation_data["giftcard_to"],
            "from": donation_data["giftcard_from"],
            "message": donation_data["giftcard_message"]
        }
    }

    try:
        response = _SESSION.post(url=path, 
        headers=_HEADERS, params=params, data=data)
    except requests.exceptions.RequestException as err:
        raise "Requests Exception found."
        logging.warning(err)

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

# if __name__ == "__main__":

    
#     # response = search_for_projects("flood", country="IN", theme="edu")
#     # print(response)

    # from config import EMAIL, PASSWORD, API_KEY, URL

    # response = get_all_projects()
    # print(response) 