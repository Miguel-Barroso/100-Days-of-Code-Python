import requests
from datetime import datetime, timezone

# Globals
MY_LAT = 35.133190  # Mano Fumon Ichome
MY_LNG = 135.911646

parameters = {
    "lat": MY_LAT,
    "lng": MY_LNG,
    "formatted": 0,  # To get an ISO time format (Unix time) 24h
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()  # If there was an error during the API call
data = response.json()
sunrise = data["results"]["sunrise"]
sunset = data["results"]["sunset"]

# Get the hour of sunrise at set location
sunrise_hour = sunrise.split("T")[1].split(":")[0].lstrip("0")  # Using split 2 times to format the date time string
print(f"Hour of sunrise = {sunrise_hour} in UTC")

# Get the hour of sunset at set location
sunset_hour = sunset.split("T")[1].split(":")[0].lstrip("0")  # .lstrip("0") removes any leading zeroes
print(f"Hour of sunset = {sunset_hour} in UTC")

# Get the current hour
current_time = datetime.now(timezone.utc)
print(f"Current hour = {current_time.hour} in UTC")
