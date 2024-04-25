import requests

pixela_endpoints = "https://pixe.la/v1/users"

pixela_user_parameter = {
    "token": "qd3rie02n20enr20f20",
    "username": "soulknight",
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}
pixela_response = requests.post(url=pixela_endpoints, json=pixela_user_parameter)
print(pixela_response.text)
