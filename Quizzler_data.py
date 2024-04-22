import requests

parameter = {"amount": 10, "category": 18, "type": "boolean"}
response = requests.get(url="https://opentdb.com/api.php", params=parameter)
response.raise_for_status()
question_data = response.json()["results"]
