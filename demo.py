import requests

para = {
    "fly_from": "LON",
    "fly_to": "NYC",
    "date_from": "28/04/2024",
    "date_to": "01/05/2024",
    "one_for_city": 1,
}

headers = {"apikey": "n6ROzICxpBr1H0V3LxQ53u27d-7zyW7i"}
response = requests.get(
    url="https://api.tequila.kiwi.com/v2/search", params=para, headers=headers
)

print(response.json()["data"][0]["countryTo"]["name"])
