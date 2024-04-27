import requests


class DataManager:
    # This class is responsible for talking to the Google Sheet.
    def __init__(self) -> None:
        self.sheety_header = {"Authorization": "Bearer gjh2342g2gru22g"}

        self.sheety_response = requests.get(
            url="https://api.sheety.co/45cecaf5b844e88d6d4b1405ac9b2e64/flightData/sheet1",
            headers=self.sheety_header,
        )
        return print(self.sheety_response.json()["sheet1"])
