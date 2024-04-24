import requests
from twilio.rest import Client

account_sid = "your_twilio_sid"
auth_token = "your_twilio_auth_token"

parameter = {
    "lat": 26.449923,
    "lon": 80.331871,
    "appid": "your_API_key",
    "cnt": 4,
}

response = requests.get(
    url="https://api.openweathermap.org/data/2.5/forecast", params=parameter
)
response.raise_for_status()
weather_data = response.json()
will_rain = False
for hour_data in weather_data["list"]:
    if hour_data["weather"][0]["id"] < 900:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="It's going to rain⛈️⛈️ today .Bring your Umbrella ☂️☂️",
        from_="",  # your twilio number
        to="verified_no",  # sender number must be verified
    )

    print(message.status)
