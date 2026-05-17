import requests, smtplib, time, os
from datetime import datetime, timezone
from retry import retry
from dotenv import load_dotenv

load_dotenv()

# Globals
MY_LAT = 35.133190  # Mano Fumon Ichome
MY_LONG = 135.911646
# MY_LAT = 18  # Tests
# MY_LONG = -126
MY_EMAIL = os.getenv("MY_EMAIL")
MY_PASSWORD = os.getenv("MY_PASSWORD")


# iss_latitude and iss_longitude must be within +/- 5 degrees of set location
@retry(tries=3, delay=2, backoff=2)
# Explanation:
#
#     @retry(tries=3, delay=2, backoff=2): This decorator attempts the function call up to 3 times if an exception is raised. The delay=2 means it waits 2 seconds between each attempt, and the backoff=2 doubles the delay after each attempt.
#     If the API call fails (e.g., due to a network issue or a server error), the function will automatically retry according to the parameters provided.
#
# This should help ensure that your function handles transient network issues gracefully.
def is_iss_overhead():
    # ISS position API Calls
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()  # Raises error if not successful
    data = response.json()

    # Getting the ISS position
    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])
    print(f"ISS position: ({iss_latitude}, {iss_longitude})")

    # Checking the ISS position relative to set location
    if (MY_LAT + 5) >= iss_latitude >= (MY_LAT - 5) and (MY_LONG + 5) >= iss_longitude >= (MY_LONG - 5):
        print("The ISS is overhead!")
        return True
    else:
        print(f"The ISS is too far away from your location: ({MY_LAT}, {MY_LONG})")
        return False

def is_nighttime():
    # Checking whether it's day or nighttime at set location
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()  # Raises error if not successful
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now(timezone.utc).hour

    if (sunrise >= time_now >= sunset) and is_iss_overhead():  # Notice lack of "and" keyword
        print("It's nighttime at your location!")
        return True
    else:
        print("The sun is still out...")
        return False

while True:
    if is_iss_overhead() and is_nighttime():  # Notice lack of "and" keyword
        print("It's dark now and the ISS is overhead!")
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()  # Encrypts the email in transit
            connection.login(user=MY_EMAIL, password=MY_PASSWORD)

            connection.sendmail(from_addr=MY_EMAIL,
                                to_addrs=MY_EMAIL,
                                msg=f"Subject:Look for the ISS!\n\nIt's dark now and the ISS is overhead!"
                                )
    else:
        print("You can't see the ISS right now...")
    time.sleep(60)