import requests
import datetime as dt

pixela_endpoints = "https://pixe.la/v1/users"
pixela_graph_endpoint = "https://pixe.la/v1/users/soulknight/graphs"
TOKEN = "qd3rie02n20enr20f20"

today_date = dt.datetime.now().date().strftime("%Y%m%d")
# print((today_date))

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

pixela_records_parameters = {
    "date": today_date,
    "quantity": "5.09"
}

pixela_header = {"X-USER-TOKEN": TOKEN}

# pixela_user_response = requests.post(url=pixela_endpoints, json=pixela_user_parameter)

# pixela_graph_response = requests.post(
#     url=pixela_graph_endpoint, json=pixela_graph_parameter, headers=pixela_header
# )
pixela_data_response=requests.post(url=f"{pixela_graph_endpoint}/{pixela_graph_parameter["id"]}",json=pixela_records_parameters,headers=pixela_header)
print(pixela_data_response.text)
