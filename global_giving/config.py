from dotenv import dotenv_values

config=dotenv_values(".env")

"""
This is for the projects configuration. Manages 
the DB and other related to the projects at large
"""

DB_NAME=config["DB_NAME"]

DB_USER=config["DB_USER"]

DB_PASSWORD=config["DB_PASSWORD"]