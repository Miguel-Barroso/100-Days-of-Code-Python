# =============================
# Flight Data
# =============================

"""
This module parses the JSON data returned from Amadeus and evaluates the cheapest flights.
NB: The assignment in this lesson uses an API that only returns flight between specific dates.
    This means the API will always return any flights it finds with a departure of tomorrow and return 6 months later.
    Those are not necessarily the true "cheapest flights". To achieve this, one would have to specify a duration and
    then iterate through several dates in order to find the true cheapest flight from tomorrow and up to 6 months.
    For the purposes of the lesson I will just assume the API returns the cheapest flight and go on with the course.
"""

# =============================
# Imports and Environment Variables
# =============================

# None

class FlightData:
    """
    This class structures the data so it can be easily accessed by other modules when it is instantiated as an object.
    Note that this object is not instantiated in main.py, only by the other function within this module.
    """
    def __init__(self, price, origin, destination, from_date, to_date, stop_overs=0):
        self.lowest_price = price
        self.origin_iata_code = origin
        self.destination_iata_code = destination
        self.from_date = from_date
        self.to_date = to_date
        self.stop_overs = stop_overs


def get_cheapest_flight(flight_data):
    """
    Returns the cheapest flight from the given flight data.
    Notice how this function is not indented. This allows this function to be accessed as an import from main.py as
    it is not a method belonging to the class.
    """

    # Initialize the variables
    cheapest_flight = None
    lowest_price = float("inf")  # Placeholder for a very large number (infinity)

    for flight in flight_data:
        flight_price = float(flight["price"]["grandTotal"])
        if flight_price < lowest_price:
            lowest_price = flight_price
            origin_iata_code = flight_data[0]['itineraries'][0]['segments'][0]['departure']['iataCode']
            number_of_stops = len(flight_data[0]['itineraries'][0]['segments']) - 1
            if number_of_stops > 2:
                number_of_stops = 2  # Limits the number of stop-overs to a maximum of 2
            # print(f"Number of stops: {number_of_stops}")
            destination_iata_code = flight_data[0]['itineraries'][0]['segments'][number_of_stops]['arrival']['iataCode']
            from_date = flight_data[0]['itineraries'][0]['segments'][0]['departure']['at'].split('T')[0]
            to_date = flight_data[0]['itineraries'][0]['segments'][number_of_stops]['arrival']['at'].split('T')[0]  # Strip away time
            # Instantiates the FlightData object with the data of the cheapest flight thus far in the loop
            cheapest_flight = FlightData(
                price=lowest_price,
                origin=origin_iata_code,
                destination=destination_iata_code,
                from_date=from_date,
                to_date=to_date,
                stop_overs=number_of_stops
            )

    return cheapest_flight