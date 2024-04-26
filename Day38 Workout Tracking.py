# You have to pre-define the headings like 'Date','Time',...previously at the time of sheet creation to post data to those rows.
# You can also hide you credentials using enviroment variable

import requests
from datetime import datetime

NUTRITIONIX_APP_ID = "your_app_id"
NUTRITIONIX_API_KEY = "your_key"

Nutrinox_end_point = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheety_endpoint = "your_sheety_endpoint"

excercise_text = input("Tell me which excercise you did?")
headers = {
    "Content-Type": "application/json",
    "x-app-id": NUTRITIONIX_APP_ID,
    "x-app-key": NUTRITIONIX_API_KEY,
}
para = {"query": excercise_text, "gender": "male"}

# providing bearer_auth for sheety
bearer_headers = {
    "Authorization": "Bearer your_auth"
}  # Only change "your_auth" not the 'Bearer' with your value


response = requests.post(url=Nutrinox_end_point, json=para, headers=headers)
result = response.json()

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

for exercise in result["exercises"]:
    sheet_inputs = {
        "datum": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"],
        }
    }

    sheet_response = requests.post(
        sheety_endpoint, json=sheet_inputs, headers=bearer_headers
    )

    print(sheet_response.text)
