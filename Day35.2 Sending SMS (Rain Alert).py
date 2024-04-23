import requests
from twilio.rest import Client

account_sid = "ACbc0ff2189cba7187b398f222a41e4bf0"
auth_token = "32fb76e40a51cf9f542bd1c39653b9e1"
client = Client(account_sid, auth_token)

message = client.messages.create(
    body="It's going to rain today⛈️⛈️.Take Your Umbrella ☂️☂️",
    from_="+12562039313",
    to="+919555943149",
)

print(message.sid)

parameter = {
    "lat": 26.449923,
    "lon": 80.331871,
    "appid": "c4bff11fd17bdf9b4d06905ac4c19079",
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
    print("Bring your Umbrella")
