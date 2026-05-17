# =============================
# Flight Club Program
# =============================

# This program lets registered users find the best flight deals from their home airport to a set of dream destinations.
# Destinations are listed in a Google sheet which is accessed via Sheety API calls.

# =============================
# Imports of Modules and Libraries
# =============================

# Import libraries
import pprint
from datetime import datetime, timedelta
from api_cache import clear_api_cache
# Import modules
from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import get_cheapest_flight
from notification_manager import NotificationManager

# =============================
# Program Start
# =============================

# Ask the user if they want to clear the global cache
print("Welcome to the Flight Club Program!\n")
clear_cache_user_input = input("Would you like to clear the cache? (y/n): ").strip().lower()
clear_api_cache(clear_cache_user_input)

# --- Set your origin airport ---
ORIGIN_CITY_IATA = "LON"

# --- Choose what type of notification ---
message_type = input("What is your message type? sms/whatsapp/email: ")

# --- Date and time settings---
TODAY = datetime.today()
TOMORROW = TODAY + timedelta(days=1)
SIX_MONTHS = TODAY + timedelta(days=6*30)

# --- Remove any double-hashes below to run the program ---

# Create an instance of the DataManager class and get the sheet data
data_manager = DataManager()
sheet_data = data_manager.get_destination_data()
print(f"{pprint.pformat(sheet_data)}")
# Get recipient data
recipient_data = data_manager.get_recipients()
print(f"{pprint.pformat(recipient_data)}")


# Create an instance of the FlightManager class
flight_search = FlightSearch()

# Create an instance of the NotificationManager class
notification_manager = NotificationManager()

# =============================
# Validate IATA Codes
# =============================

# Update any missing IATA codes
print("Validating IATA codes for the desired destinations:")
for row in sheet_data:
    existing_iata_code = row.get("iataCode", None)  # To prevent key errors
    if existing_iata_code is None:
        print(f"❌ Missing IATA code for {row["city"]}")
        print(f"Fetching IATA code...")
        iata_code = flight_search.get_iata_code(row["city"])
        data_manager.update_destination_iata_codes(row["id"], iata_code)
        print(f"✅ Updated {row["city"]} with IATA code {iata_code}.")
    else:
        print(f"✅ The IATA code for {row["city"]} is {row['iataCode']}")
clear_api_cache(clear_cache_user_input)  # If requested, clears cache before sheet data  is reloaded via API
sheet_data = data_manager.get_destination_data()
print(f"{pprint.pformat(sheet_data)}\n")

# =============================
# Validate Prices
# =============================

# Update any missing prices
print("Validating existing prices for the desired destinations:")
for row in sheet_data:
    existing_price = row.get("lowestPrice", None)
    if existing_price is None:
        print(f"❌ Missing price data for {row["city"]}")
        print(f"Updating with placeholder:")
        data_manager.update_destination_lowest_price(row["id"],
                                                     row['iataCode'],
                                                     999999)
    else:
        print(f"✅ The current price for {row["city"]} is {row['lowestPrice']}")
clear_api_cache(clear_cache_user_input)  # If requested, clears cache before sheet data  is reloaded via API
sheet_data = data_manager.get_destination_data()
print(f"{pprint.pformat(sheet_data)}\n")

# =============================
# Find the cheapest flights
# =============================

print(f"\n"
      f"Searching for flights between {TOMORROW.strftime("%Y-%m-%d")} and {SIX_MONTHS.strftime("%Y-%m-%d")}, this "
      f"may take a few minutes.")

for row in sheet_data:
    flights = flight_search.find_flight_offer(
        origin_iata_code=ORIGIN_CITY_IATA,
        destination_iata_code=row["iataCode"],
        from_date=TOMORROW,
        to_date=SIX_MONTHS,
        non_stop='true'  # Begin searching for non-stop flights
    )
    if not flights:
        print(f"No direct flight for {row['iataCode']} was found.\n"
              f"Searching further...")
        flights = flight_search.find_flight_offer(
            origin_iata_code=ORIGIN_CITY_IATA,
            destination_iata_code=row["iataCode"],
            from_date=TOMORROW,
            to_date=SIX_MONTHS,
            non_stop='false'  # Starts looking for flights with stop-overs
        )
        if not flights:
            print(f"No flight with stop-over(s) for {row['iataCode']} was found.\n")
            continue  # Continues the loop, searching flights for the other destinations

    if flights:  # If there are any flights after normal and extensive search
        print(f"{len(flights)} flight(s) for {row['iataCode']} was found!\n")
        cheapest_flight = get_cheapest_flight(flights)

        # Checks the Google sheet if we have a new lowest price
        if cheapest_flight.lowest_price < float(row['lowestPrice']):
            print(f"New lowest price for {row['iataCode']}")

            # Creating a message to send a price alert notification
            message_body = (f"Cheapest flight for {cheapest_flight.destination_iata_code} "
                            f"is departing {cheapest_flight.origin_iata_code} "
                            f"on {cheapest_flight.from_date} "
                            f"and arriving {cheapest_flight.to_date}, "
                            f"for only £{cheapest_flight.lowest_price}!\n"
                            f"Number of stop-overs: {cheapest_flight.stop_overs}")
            print(f"{message_body}\n")
            print(f"\n"
                  f"Sending message...")
            if message_type == "sms":
                notification_manager.send_sms_notification(f"{message_body}")
            elif message_type == "whatsapp":
                notification_manager.send_whatsapp_notification(f"{message_body}")
            elif message_type == "email":
                for user in recipient_data:
                    notification_manager.send_email_notification(user['whatIsYourEmail?'], f"{message_body}")
            else:
                print(f"No message was sent")  # Secret dev option to not send any notification during debugging

            # Updates the Google sheet with the latest price lowest price for the destination
            data_manager.update_destination_lowest_price(row["id"], row["iataCode"], cheapest_flight.lowest_price)
        else:
            print(f"No new lowest price for {row['iataCode']} was found.")