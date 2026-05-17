# =============================
# Flight Search
# =============================

"""
This module is responsible for accessing the Amadeus Flight Search API.
Other modules of this program is dependent on this module for getting flight data.
"""

# =============================
# Imports and Environment Variables
# =============================

import os
import time
from api_cache import cached_session, check_response_cache_status
from dotenv import load_dotenv

load_dotenv()

IATA_ENDPOINT = "https://test.api.amadeus.com/v1/reference-data/locations/cities"
FLIGHT_ENDPOINT = "https://test.api.amadeus.com/v2/shopping/flight-offers"
TOKEN_ENDPOINT = "https://test.api.amadeus.com/v1/security/oauth2/token"

# =============================
# FlightSearch Class
# =============================

class FlightSearch:
    def __init__(self):
        self.amadeus_access_token = self.get_amadeus_access_token()

    @staticmethod
    def get_amadeus_access_token():
        _headers = {
            "content-type": "application/x-www-form-urlencoded",
        }

        _params = {
            "grant_type": "client_credentials",
            "client_id": os.getenv("AMADEUS_API_KEY"),
            "client_secret": os.getenv("AMADEUS_API_SECRET"),
        }

        response = cached_session.post(url=TOKEN_ENDPOINT, headers=_headers, data=_params)
        response.raise_for_status()
        check_response_cache_status(response)
        print(f"Received Amadeus Access Token: {response.json()["access_token"]} "
              f"Expiry time: {response.json()['expires_in']} seconds\n")
        return response.json()["access_token"]

    def get_iata_code(self, city_name):
        time.sleep(0.2)  # To prevent rate limiting (<10 request per second, 0.1 s between request)
        _headers = {
            "Authorization": f"Bearer {self.amadeus_access_token}",
        }

        _query = {
            "keyword": city_name,
            "max": 2,  # To limit amount of data in the response
            "include": "AIRPORTS",  # Will include nearby airports if none found for given city
        }

        response = cached_session.get(url=IATA_ENDPOINT, headers=_headers, params=_query)
        response.raise_for_status()
        check_response_cache_status(response)
        city_data = response.json().get("data", None)  # Grabs the data but returns None if there is none for the city
        if not city_data:
            print(f"No IATA code for {city_name} found.")
            return None
        else:
            return city_data[0]["iataCode"]  # Returns the first found IATA code for given city

    def find_flight_offer(self, origin_iata_code, destination_iata_code, from_date, to_date, non_stop='true'):
        time.sleep(0.2)  # To prevent rate limiting (<10 request per second, 0.1 s between request)
        _headers = {
            "Authorization": f"Bearer {self.amadeus_access_token}",
        }

        _query = {
            "originLocationCode": origin_iata_code,
            "destinationLocationCode": destination_iata_code,
            "departureDate": from_date.strftime("%Y-%m-%d"),
            "returnDate": to_date.strftime("%Y-%m-%d"),
            "adults": 1,
            "nonStop": non_stop,  # Must be a string, Python booleans won't work
            "currencyCode": "GBP",
            "max": 10,
        }
        print(f"\n"
              f"Checking {destination_iata_code}, hold on...")
        response = cached_session.get(url=FLIGHT_ENDPOINT, headers=_headers, params=_query)
        response.raise_for_status()
        check_response_cache_status(response)
        # print(response.text)  # For debugging purposes
        flight_data = response.json().get("data", None)  # Either gets data or returns None
        return flight_data