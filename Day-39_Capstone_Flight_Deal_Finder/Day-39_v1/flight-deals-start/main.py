#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program
# requirements.
from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import FlightData

# Remove double hashes ## to run the whole program

# Create an instance of the FlightSearch class
flight_search = FlightSearch()

# Create an instance of the DataManager class and pass the flight_search instance so it can be used by DataManager
data_manager = DataManager(flight_search)

# Get IATA codes for the listed destinations
iata_codes_list = data_manager.get_iata_codes()
# print(iata_codes_list)

# Will get flight deals for the listed destinations (IATA format)
##flight_search.find_flight_deal(iata_codes_list)

# Will structure the received flight data
##flight_data.structure_data(flight_search)