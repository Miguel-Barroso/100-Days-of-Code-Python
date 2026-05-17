import requests, os, math
from dotenv import load_dotenv  # In order to load environment variables
from zoneinfo import ZoneInfo  # In order to handle time zones dynamically
from datetime import datetime, timedelta

# Trip duration settings
trip_length = 14  # Number of days of the trip
search_range = 180  # Number of days ahead to search, i.e., half a year in the future
loop_iterations = math.floor(search_range / trip_length)  # Returns the number of possible iterations


load_dotenv()


class FlightSearch:
    def __init__(self):
        # This class is responsible for talking to the Flight Search API.
        self.amadeus_url = os.getenv("AMADEUS_END_POINT")
        self.amadeus_api_key = os.getenv("AMADEUS_API_KEY")
        self.amadeus_secret = os.getenv("AMADEUS_SECRET")
        self.amadeus_token = self.get_access_token()  # Makes sure a token is generated for each instance of FlightSearch

    # Getting an access token
    def get_access_token(self):
        security_end_point = f"{self.amadeus_url}/security/oauth2/token"

        headers = {
            "content-type": "application/x-www-form-urlencoded"
        }

        params = {
            "grant_type": "client_credentials",
            "client_id": self.amadeus_api_key,
            "client_secret": self.amadeus_secret
        }

        response = requests.post(url=security_end_point, headers=headers, data=params)
        response.raise_for_status()
        return response.json()["access_token"]

    def get_iata_codes(self, city):
        city_end_point = f"{self.amadeus_url}/reference-data/locations/cities"

        auth_header = {
            "Authorization": f"Bearer {self.amadeus_token}",
        }

        params = {
            "keyword": city,
            "max": 3  # To limit amount of data in the response
        }

        response = requests.get(url=city_end_point, headers=auth_header, params=params)
        response.raise_for_status()
        # data = response.json()["data"][0]["iataCode"]  # Works but may result in key error if given city doesn't exist
        data = response.json().get("data", None)  # Use .get to avoid KeyError, defaults to None
        if not data:  # Error handling in case nothing is returned from the API
            print(f"No IATA code for {city} available at this time.")
            return None
        # print(data)
        return data[0]["iataCode"]  # Will return only the first and main IATA code when multiples exist


    def find_flight_deal(self, iata_codes_list):
        flight_search_end_point = f"{os.getenv('AMADEUS_FLIGHT_END_POINT')}/shopping/flight-offers"
        auth_header = {
            "Authorization": f"Bearer {self.amadeus_token}",
            # "X-HTTP-Method-Override": "GET", # Docs says required but works without...
        }

        for city in iata_codes_list:
            print(f"Checking for cheapest flight to {city}:")
            # Date and time
            now = datetime.now(ZoneInfo("Asia/Tokyo"))  # Gets current datetime object for specified timezone
            trip_start = now + timedelta(days=1)  # Gets the datetime object for the start of a trip, i.e., "tomorrow"
            trip_end = trip_start + timedelta(days=trip_length)  # Gets the datetime object for the end of a trip
            print(f"Today is: {now}")
            # print(f"Trip start is: {trip_start}")
            # print(f"Trip end is: {trip_end}")
            for _ in range(1, loop_iterations):
                params = {
                    "originLocationCode": "LON",  # London Airports' IATA code
                    "destinationLocationCode": city,  # In IATA code format
                    "departureDate": trip_start.strftime("%Y-%m-%d"),
                    # (YYY-MM-DD), should be looking from tomorrow and 6 months ahead...
                    "returnDate": trip_end.strftime("%Y-%m-%d"),
                    # Need to be specified to get round trips. Duration not in program reqs...
                    "adults": 1,  # Specifies the number of adult travelers
                    "nonStop": "true",  # Only direct flights
                    "currencyCode": "GBP",  # Pound sterling
                    "maxPrice": 5000,  # Hard-coded price for now
                    "max": 2,  # Limits number of returned flights to minimize data use
                }

                trip_start = trip_end + timedelta(days=1)  # Gets the datetime object for the start of a trip
                trip_end = trip_start + timedelta(days=trip_length)  # Could be its own method by now...
                # print(f"Trip start is: {trip_start}")
                # print(f"Trip end is: {trip_end}")

                try:
                    # Get all flights cheaper than maxPrice
                    response = requests.get(url=flight_search_end_point, headers=auth_header, params=params)
                    response.raise_for_status()  # Check for HTTP errors
                    print(response.text)
                except:
                    print(f"Flight could not be retrieved for the specified dates.")
