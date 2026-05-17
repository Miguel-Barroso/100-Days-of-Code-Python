import requests, os
from twilio.rest import Client
from dotenv import load_dotenv

load_dotenv()

MY_LAT = 35.133190  # Mano Fumon Ichome
MY_LONG = 135.911646  #AKA Kitahama

# Twilio Settings
account_sid = os.getenv("TWILIO_ACCOUNT_SID")
auth_token = os.getenv("TWILIO_AUTH_TOKEN")


# Open Weather Settings
api_key = os.getenv("OWM_API_KEY")
# url = "https://api.openweathermap.org/data/2.5/weather"  # Only for the current weather
url = "https://api.openweathermap.org/data/2.5/forecast"  # 5 day/3 hour forcast (40 forecasts in total)
units = "metric"  # imperial/metric/standard, the latter returns results in kelvin
timestamps = 4



parameters = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "appid": api_key,
    "units": units,
    "cnt": timestamps,  # Number of timestamps returned out of the total
}

# 4 timestamp counts = 12h window (3h * 4)

response = requests.get(url, params=parameters)
response.raise_for_status()  # Raises HTTP errors in the response
# print(response)
weather_data = response.json()
need_umbrella = False
for hour_data in weather_data["list"]:
    weather_id = hour_data["weather"][0]["id"]  # Returns the id of the main weather for each forecast
    print(weather_id)  # Fortunately returned as type 'int'
    if weather_id < 700:
        need_umbrella = True
if need_umbrella:
    print("Need an umbrella today!")
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="No need to water the plants today, it's going to rain in the next 12 hours...",
        from_=os.getenv("TWILIO_FROM_NUMBER"),
        to=os.getenv("TWILIO_TO_NUMBER")
    )
    print(message.status)
else:
    print("Sun is shining!")