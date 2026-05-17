# =============================
# Data Manager
# =============================

"""
This module is responsible for accessing the Google sheet.
It can both read and write relevant data using Sheety API calls.
"""

# =============================
# Imports and Environment Variables
# =============================

import os
from api_cache import cached_session, check_response_cache_status
from dotenv import load_dotenv

load_dotenv()

SHEETY_ENDPOINT = os.getenv("SHEETY_ENDPOINT")


# =============================
# DataManager Class
# =============================

class DataManager:
    """
    This class is responsible for reading and writing data in the Google sheet.
    It uses Sheety's REST API for all communication.
    """
    def __init__(self):
        self.sheety_headers = {
            "Authorization": os.getenv("SHEETY_AUTH")
        }
        self.destination_data = {}
        self.recipient_data = {}

    def get_destination_data(self):
        response = cached_session.get(url=f"{SHEETY_ENDPOINT}/prices", headers=self.sheety_headers)
        response.raise_for_status()
        check_response_cache_status(response)
        self.destination_data = response.json()["prices"]  # Important: This is the sheet name
        return self.destination_data

    def update_destination_iata_codes(self, city_id, iata_code):
        """
        This method updates any missing IATA codes in the Google sheet.
        It gets called by main.py if any cities are missing IATA codes.
        It then connects to the sheety API and updates those city (row) IDs.
        """
        new_data = {
            "price": {
                "iataCode": iata_code
            }
        }
        response = cached_session.put(
            url=f"{SHEETY_ENDPOINT}/prices/{city_id}",
            headers=self.sheety_headers,
            json=new_data
        )
        response.raise_for_status()
        check_response_cache_status(response)
        print("Updated destination IATA code in the Google sheet.\n")

    def update_destination_lowest_price(self, city_id, iata_code, lowest_price):
        """
        This method updates the Google sheet with the current lowest price for the destination.
        """
        new_data = {
            "price": {
                "lowestPrice": lowest_price
            }
        }
        response = cached_session.put(
            url=f"{SHEETY_ENDPOINT}/prices/{city_id}",
            headers=self.sheety_headers,
            json=new_data
        )
        response.raise_for_status()
        check_response_cache_status(response)
        print(f"Updated {iata_code} lowest price to £{lowest_price} in the Google sheet.")

    def get_recipients(self):
        response = cached_session.get(url=f"{SHEETY_ENDPOINT}/users", headers=self.sheety_headers)
        response.raise_for_status()
        check_response_cache_status(response)
        self.recipient_data = response.json()["users"]  # Important: This is the sheet name
        return self.recipient_data