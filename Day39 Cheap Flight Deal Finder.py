import requests

sheety_header = {"Authorization": "Bearer gjh2342g2gru22g"}

# sheety_parameter = {}

sheety_response = requests.get(
    url="https://api.sheety.co/45cecaf5b844e88d6d4b1405ac9b2e64/flightData/sheet1",
    headers=sheety_header,
)

print(sheety_response.json())
