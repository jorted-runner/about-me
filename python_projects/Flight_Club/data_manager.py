import requests
import datetime as dt
import os
from dotenv import load_dotenv

def configure():
    load_dotenv()

configure()

tequila_api = os.environ.get("tequila_api")


class DataManager:
    def __init__(self):
        self.SHEETY_TOKEN = os.environ.get("SHEETY_TOKEN")
        self.SHEETY_ENDPOINT = os.environ.get("sheety_price")
        tommorrow = dt.datetime.now() + dt.timedelta(days=1)
        six_month = dt.datetime.now() + dt.timedelta(days=180)
        self.tommorrow = tommorrow.strftime("%d/%m/%Y")
        self.six_month = six_month.strftime("%d/%m/%Y")

    def get_cities(self):
        # response = requests.get(url=self.SHEETY_ENDPOINT, headers=self.SHEETY_TOKEN)
        # data = response.json()['prices']
        ## This data represents the data on the Google Sheets ##
        data = [{'city': 'Berlin', 'iataCode': 'BER', 'lowestPrice': 500, 'id': 3},
                {'city': 'Tokyo', 'iataCode': 'NRT', 'lowestPrice': 485, 'id': 4},
                {'city': 'Sydney', 'iataCode': 'SYD', 'lowestPrice': 551, 'id': 5},
                {'city': 'Kuala Lumpur', 'iataCode': 'KUL', 'lowestPrice': 414, 'id': 7},
                {'city': 'New York', 'iataCode': 'JFK', 'lowestPrice': 240, 'id': 8},
                {'city': 'San Francisco', 'iataCode': 'SFO', 'lowestPrice': 260, 'id': 9},
                {'city': 'Salt Lake City', 'iataCode': 'SLC', 'lowestPrice': 350, 'id': 11},
                {'city': 'Phoenix', 'iataCode': 'PHX', 'lowestPrice': 150, 'id': 12}]
        return data

    def update_sheet_w_iata(self, data):
        endpoint = f"{self.SHEETY_ENDPOINT}/{data['id']}"
        sheet_input = {
            "price":
                data
        }
        response = requests.put(url=endpoint, json=sheet_input)
        response.raise_for_status()

    def get_emails(self):
        response = requests.get(url=os.environ.get("sheety_email"))
        data = response.json()["users"]
        return data
