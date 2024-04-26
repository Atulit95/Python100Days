import requests

NUTRITIONIX_APP_ID = "7f4cfde2"
NUTRITIONIX_API_KEY = "9bbca1431e842815f407d7c7139a2cb1"

Nutrinox_end_point = "https://trackapi.nutritionix.com/v2/natural/exercise"

excercise_text = input("Tell me which excercise you did?")
headers = {
    "Content-Type": "application/json",
    "x-app-id": NUTRITIONIX_APP_ID,
    "x-app-key": NUTRITIONIX_API_KEY,
}
para = {"query": excercise_text, "gender": "male"}


response = requests.post(url=Nutrinox_end_point, json=para, headers=headers)
result = response.json()
print(result)
