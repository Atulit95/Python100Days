import requests

# api_key = "c4bff11fd17bdf9b4d06905ac4c19079"
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
