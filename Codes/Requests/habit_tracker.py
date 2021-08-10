#!/usr/bin/env python3
import requests
import datetime as dt
# Setting up pixela user account:
TOKEN = "youcantypeanytokenhere"
USERNAME = "username"
GRAPH_ID = "graph1"
pixela_endpoint = "https://pixe.la/v1/users"
user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

# Configuring graph for our user:
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
graph_config = {
    "id": GRAPH_ID,
    "name": "Programming Graph",
    "unit": "hours",
    "type": "float",
    "color": "shibafu"
}
headers = {
    "X-USER-TOKEN": TOKEN
}
# response = requests.post(
#     url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)
# you can confirm the response success by visiting "https://pixe.la/v1/users/<username>/graphs/<id>.html"


# Posting value on the graph:
today = dt.datetime.now().strftime("%Y%m%d")
graph1_endpoint = f"{graph_endpoint}/{GRAPH_ID}"
graph1_data = {
    "date": today,
    "quantity": input("How many hours did you programmed today? ")
}

response = requests.post(
    url=graph1_endpoint, json=graph1_data, headers=headers)
print(response.text)


# Using put method:
update_endpoint = f"{graph1_endpoint}/{today}"
new_graph1_data = {
    "quantity": "6.2"
}
# response = requests.put(url=update_endpoint,
#                         json=new_graph1_data, headers=headers)
# print(response.text)

# Using delete method:
delete_endpoint = f"{update_endpoint}"
# response = requests.delete(url=delete_endpoint, headers=headers)
# print(response.text)

''' Make sure to comment out other requests while making one '''
