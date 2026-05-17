import requests, os
from datetime import datetime
from zoneinfo import ZoneInfo
from dotenv import load_dotenv

load_dotenv()

#Date and time
now = datetime.now(ZoneInfo("Asia/Tokyo"))
date = now.strftime("%Y-%m-%d")
time = now.strftime("%H:%M:%S")
# print(date, time)

# Nutritionix
APP_ID = os.getenv("NUTRITIONIX_APP_ID")
API_KEY = os.getenv("NUTRITIONIX_API_KEY")
HOST_DOMAIN = "https://trackapi.nutritionix.com"
END_POINT = f"{HOST_DOMAIN}/v2/natural/exercise"  # Natural language processing for exercise

# sheety
END_POINT_SHEETY = os.getenv("SHEETY_ENDPOINT")


headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

params = {
    "query": input("Tell me which exercises you did: ")
}

# params = {
#     "query": "I ran 5k and then swam for 30 min"
# }

sheety_auth = {
    "Authorization": os.getenv("SHEETY_AUTH"),
}

workout_response = requests.post(url=END_POINT, headers=headers, json=params)
workout_response.raise_for_status()
workout_results = workout_response.json()
print(workout_results)

# Format workout data and send to Google sheet
for exercise in workout_results['exercises']:
    workout_data = {
        "workout": {
            "date": date,
            "time": time,
            "exercise": exercise['name'].title(),  # The API otherwise turns exercises into camelCase
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }
    sheety_response = requests.post(END_POINT_SHEETY, json=workout_data, headers=sheety_auth)
    sheety_response.raise_for_status()
    print(sheety_response.text)