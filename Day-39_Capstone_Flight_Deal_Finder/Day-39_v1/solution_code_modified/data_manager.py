import os
import requests
from requests.auth import HTTPBasicAuth
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# SHEETY_PRICES_ENDPOINT = YOUR ENDPOINT HERE

class DataManager:

    def __init__(self):
        # self._user = os.environ["SHEETY_USRERNAME"]
        # self._password = os.environ["SHEETY_PASSWORD"]
        self.sheety_headers = {
            "Authorization": os.getenv("SHEETY_AUTH")
        }
        self.sheety_url = os.getenv("SHEETY_END_POINT")
        # self._authorization = HTTPBasicAuth(self._user, self._password)
        self.destination_data = {}

    def get_destination_data(self):
        # Use the Sheety API to GET all the data in that sheet and print it out.
        response = requests.get(url=self.sheety_url, headers=self.sheety_headers)
        data = response.json()
        self.destination_data = data["prices"]
        # Try importing pretty print and printing the data out again using pprint() to see it formatted.
        # pprint(data)
        return self.destination_data

    # In the DataManager Class make a PUT request and use the row id from sheet_data
    # to update the Google Sheet with the IATA codes. (Do this using code).
    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{self.sheety_url}/{city['id']}", headers=self.sheety_headers,
                json=new_data
            )
            print(response.text)
