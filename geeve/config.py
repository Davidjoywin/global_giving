from traceback import print_list
from dotenv import dotenv_values, load_dotenv
import os

config=dotenv_values(".env")


"""
This is specifically for the geeve app. It manages 
everything related to the app configurations.
"""

load_dotenv()
EMAIL=os.getenv("EMAIL")

PASSWORD=os.getenv("PASSWORD")

API_KEY=os.getenv("API_KEY")

URL=os.getenv("URL")
