import requests, os
# from flight_search import FlightSearch  # No need to import this since an instance is passed via main.py to init func.
from dotenv import load_dotenv

load_dotenv()

class DataManager:
    # This class is responsible for talking to the Google Sheet.
    def __init__(self, flight_search_instance):
        self.sheety_headers = {
            "Authorization": os.getenv("SHEETY_AUTH")
        }
        self.sheety_url = os.getenv("SHEETY_END_POINT")
        self.destinations_list = []
        self.data = {}
        self.flight_search = flight_search_instance  # Passes flight search instance to the init function
        self.get_destinations()  # Gets the list of destinations as soon as this method is initialized
        self.check_iata_codes()  # Checks the IATA codes for the listed destinations (will update missing ones)
        self.check_trip_prices()  # Checks the trip prices for the listed destinations (will update missing ones)

    # Fetches destinations from the Google Sheet
    def get_destinations(self):
        response = requests.get(url=self.sheety_url, headers=self.sheety_headers)
        response.raise_for_status()  # Check for HTTP errors
        self.data = response.json()["prices"]  # self. makes data available to other methods, "prices" = sheet name
        # for _ in range(len(data)):
        #     self.destinations_list.append(data[_]["city"])
        self.destinations_list = [city_data["city"] for city_data in self.data]
        # print(self.data)
        return self.destinations_list  # Now we have a list of destinations

    # Checks whether IATA codes already exists, else fetches them via API call
    def check_iata_codes(self):
        cities_to_update = []
        for city in self.data:
            # if city_data["iataCode"] == "":  # May result in key error if column is empty
            iata_code = city.get("iataCode", None)  # Safely gets the IATA code in the Google sheet or return None
            #  When there was an empty column, the "iataCode" is not part of the JSON response
            if not iata_code:  # If there is no dict entry for the given city
                print(f"IATA code for {city['city']} updated.")
                cities_to_update.append(city)  # List of cities in need of IATA code
            else:
                # print(f"IATA code for {city['city']} is already present.")
                pass

        if len(cities_to_update) == 0:  # In effect if there are no cities to update
            print("No IATA codes were missing")
        else:
            self.update_iata_codes(cities_to_update)

    # Updates cities' IATA codes if they are missing
    def update_iata_codes(self, cities):
        # row_index = 2  # Starting row, below the headers  # Moved to dynamic row id, see below

        # Format IATA data and send to Google sheet
        for city in cities:
            row_id = city["id"]  # Fetches the row id of the current city
            city_name = city["city"]
            iata_code = self.flight_search.get_iata_codes(city_name)
            iata_data = {
                "price": {
                    "iataCode": iata_code,  # Note that Sheetly API uses camelCase
               }
            }
            print(f"Updating row {row_id} with data: {iata_data}")

            sheety_response = requests.put(url=f"{self.sheety_url}/{row_id}", headers=self.sheety_headers, json=iata_data)
            sheety_response.raise_for_status()  # Checks for HTTP errors
            print(f"Update:\n{sheety_response.text}")
            # row_index += 1  # Not needed with dynamic row ids

    def get_iata_codes(self):
        iata_codes_list = []
        for city in self.data:
            iata_codes_list.append(city.get("iataCode", None))
        return iata_codes_list  # Returns IATA codes for the listed destinations


    # Checks whether price info already exists and imports it, if not sets a default price
    def check_trip_prices(self):
        cities_to_update = []
        for city in self.data:
            lowest_price = city.get("lowestPrice", None)
            if not lowest_price:
                print(f"Price for {city['city']} trip updated.")
                cities_to_update.append(city)  # List of cities in need of price adjustment
            else:
                    # print(f"Price for {city['city']} trip is already present.")
                    pass

        if not cities_to_update:
            print("No price data was missing")
        else:
            self.update_trip_prices(cities_to_update)

    # Updates trip prices if they are missing
    def update_trip_prices(self, cities):
        # Format IATA data and send to Google sheet
        for city in cities:
            row_id = city["id"]  # Fetches the row id of the current city
            default_price = 4321  # Bogus price, will update sheet by fetching real price data later
            price_data = {
                "price": {
                    "lowestPrice": default_price,  # Note that Sheetly API uses camelCase
                }
            }
            print(f"Updating row {row_id} with data: {price_data}")

            sheety_response = requests.put(url=f"{self.sheety_url}/{row_id}", headers=self.sheety_headers,
                                           json=price_data)
            sheety_response.raise_for_status()  # Checks for HTTP errors
            print(f"Update:\n{sheety_response.text}")
            # row_index += 1  # Not needed with dynamic row ids
