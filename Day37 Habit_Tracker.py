import requests

pixela_endpoints = "https://pixe.la/v1/users"
pixela_graph_endpoint = "https://pixe.la/v1/users/soulknight/graphs"
TOKEN = "qd3rie02n20enr20f20"

pixela_user_parameter = {
    "token": TOKEN,
    "username": "soulknight",
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

pixela_graph_parameter = {
    "id": "g01",
    "name": "HabitTracker",
    "unit": "Kilometer",
    "color": "shibafu",
    "type": "float",
}

pixela_graph_header = {"X-USER-TOKEN": TOKEN}

pixela_user_response = requests.post(url=pixela_endpoints, json=pixela_user_parameter)

pixela_graph_response = requests.post(
    url=pixela_graph_endpoint, json=pixela_graph_parameter, headers=pixela_graph_header
)
print(pixela_graph_response.text)
