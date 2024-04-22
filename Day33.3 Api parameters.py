import requests
import datetime as dt

MY_LAT = 40.058323
MY_LONG = -74.405663

parameter = {"lat": MY_LAT, "lng": MY_LONG, "formatted": 0}

response = requests.get(url=" https://api.sunrise-sunset.org/json", params=parameter)
response.raise_for_status()
data = response.json()
sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]
sunset = data["results"]["sunset"].split("T")[1].split(":")[0]

print(sunrise)

time_now = dt.datetime.now()
