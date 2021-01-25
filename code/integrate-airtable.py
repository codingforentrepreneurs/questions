"""
Installations:

python -m pip install requests python-dotenv

Create a .env file with:

AIRTABLE_BASE_ID='your_base_id'
AIRTABLE_API_KEY='your_api_key'
AIRTABLE_TABLE_NAME='your_table_name'

The AIRTABLE_API_KEY can be generated on: https://airtable.com/account
"""

import os
import requests
from dotenv import load_dotenv
load_dotenv()


AIRTABLE_BASE_ID=os.environ.get("AIRTABLE_BASE_ID")
AIRTABLE_API_KEY=os.environ.get("AIRTABLE_API_KEY")
AIRTABLE_TABLE_NAME=os.environ.get("AIRTABLE_TABLE_NAME")

endpoint=f'https://api.airtable.com/v0/{AIRTABLE_BASE_ID}/{AIRTABLE_TABLE_NAME}'

# python requests headers
# headers = {
#     "Authorization": f"Bearer {AIRTABLE_API_KEY}",
#     "Content-Type": "application/json"
# }

# data = {
#   "records": [
#     {
#       "fields": {
#         "name": "Justin",
#         "Email": "abc@notreal.com\n"
#       }
#     },
#     {
#       "fields": {
#         "name": "Justin",
#         "Email": "abc@notreal.com\n"
#       }
#     }
#   ]
# }

# # http methods?
# # what is the method for "create" -> HTTP Method POST


# r = requests.post(endpoint, json=data, headers=headers)
# print(r.status_code)


def add_to_airtable(email=None, name=""):
    if email is None:
        return
    headers = {
        "Authorization": f"Bearer {AIRTABLE_API_KEY}",
        "Content-Type": "application/json"
    }
    data = {
    "records": [
            {
            "fields": {
                "name": name,
                "email": email
                }
            }
        ]
    }
    r = requests.post(endpoint, json=data, headers=headers)
    return r.status_code == 200
    

# email = input("What is your email?\n")
# name = input("What is your name?\n")

# add_to_airtable(email, name=name)

add_to_airtable('abc-123fadsf@gmail.com', name="Not real")
