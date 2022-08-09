from datetime import datetime

def datetime_conversion(dtime):
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