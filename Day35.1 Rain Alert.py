import requests

parameter = {
    "lat": 26.449923,
    "lon": 80.331871,
    "appid": "your API key",
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
