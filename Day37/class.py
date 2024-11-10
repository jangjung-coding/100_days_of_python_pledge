# HTTP Requests
'''
GET: Retrieve data from the server
POST: Send data to the server
PUT: Update data on the server
DELETE: Delete data from the server
'''

# Pixela API
import requests

TOKEN = "kictIntern-20241105"
USERNAME = "jjang"
GRAPH_ID = "graph1"

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": GRAPH_ID,
    "name": "Coding Graph",
    "unit": "Km",
    "type": "float",
    "color": "ajisai",
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers={"X-USER-TOKEN": TOKEN})
# print(response.text)

import datetime
today = datetime.datetime.now()

pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"
pixel_data = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "7",
}

response = requests.post(url=pixel_creation_endpoint, json=pixel_data, headers={"X-USER-TOKEN": TOKEN})
print(response.text)


