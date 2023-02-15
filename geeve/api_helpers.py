from datetime import datetime

from isocountrycode.alpha2 import Alpha2 as alpha

def datetime_conversion(dtime):

    """
    convert the api given datetime format to just date;
    which is in dd mm yyyy format. 

    mm: shortend month name
    """
    dtime = dtime.split("-")[:-1]
    dtime = "-".join(dtime)
    old_format = datetime.strptime(dtime, "%Y-%m-%dT%H:%M:%S")
    new_format = old_format.strftime("%d %b %Y")
    return new_format

def flatten_projects(api):
    projects = []
    for data in api:
        project = {}
        for key, value in data.items():
            if type(value) != dict:
                project[key] = value
                if (key == "dateOfMostRecentReport") | (key == "approvedDate") | (key == "modifiedDate"):
                    project[key] = datetime_conversion(value)
            if key == "image":
                for val in value["imagelink"]:
                    """forming camelcase with imagelink and the individual size"""
                    link = "imageLink%s"
                    link %= val["size"].capitalize()
                    project[link] = val["url"]
        projects.append(project)
    return projects

def get_isocountrycode():

    """
    Return the isocountry code gotten from the python3 library
    'isocountrycode' in tuple-in-list format.
    """
    isocountrycode = {
        " ".join(key.split("_")): value.value
        for key, value in alpha.__dict__.items() 
        if (not key.startswith("_")) & isinstance(value, alpha)
    }

    return isocountrycode

def get_theme_name_with_theme_id(theme_id, themes):
    theme_name = None
 
    for theme in themes:
        if theme['id'] == theme_id:
            theme_name = theme['name']
    return theme_name