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
import time
from datetime import datetime, timedelta
# Import modules
from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import FlightData
from notification_manager import NotificationManager

# =============================
# Program Start
# =============================

# --- Set your origin airport ---
ORIGIN_CITY_IATA = "LON"

# --- Date and time settings---
TODAY = datetime.today()
TOMORROW = TODAY + timedelta(days=1)
SIX_MONTHS = TODAY + timedelta(days=6*30)

# --- Remove any double-hashes below to run the program ---

# Create an instance of the DataManager class and get the sheet data
data_manager = DataManager()
sheet_data = data_manager.get_destination_data()
print(f"{pprint.pformat(sheet_data)}")

# Create an instance of the FlightManager class
flight_search = FlightSearch()

# Create an instance of the FlightData class
flight_data = FlightData()

# Create an instance of the NotificationManager class
notification_manager = NotificationManager()

# =============================
# Validate IATA Codes
# =============================

# Update any missing IATA codes
print("Validating IATA codes for the desired destinations:")
for row in sheet_data:
    if not row["iataCode"]:
        print(f"❌ Missing IATA code for {row["city"]}")
        print(f"Fetching IATA code...")
        iata_code = flight_search.get_iata_code(row["city"])
        data_manager.update_destination_iata_codes(row["id"], iata_code)
        print(f"✅ Updated {row["city"]} with IATA code {iata_code}.")
    else:
        print(f"✅ The IATA code for {row["city"]} is {row['iataCode']}")

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
        to_date=SIX_MONTHS
    )
    if not flights:
        print(f"No flight for {row['iataCode']} was found.")
    else:
        print(f"Flight(s) for {row['iataCode']} was found:\n")
        cheapest_flight = flight_data.get_cheapest_flight(flights)
        print(f"Lowest price: {cheapest_flight}")
        data_manager.update_destination_lowest_price(row["id"], row["iataCode"], cheapest_flight)
    time.sleep(0.2)  # To prevent rate limiting (<10 request per second, 0.1 s between request)

message_type = input("What is your message type? sms/whatsapp/email: ")
if message_type == "sms":
    notification_manager.send_sms_notification(f"Cheapest flight is...")
elif message_type == "whatsapp":
    notification_manager.send_whatsapp_notification(f"Cheapest flight is...")
else:
    notification_manager.send_email_notification(f"Cheapest flight is...")