import requests, os
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

PIXELA_END_POINT = "https://pixe.la/v1/users"
USERNAME = os.getenv("PIXELA_USERNAME")
API_KEY = os.getenv("PIXELA_API_KEY")
GRAPH_ID = "graph1"

user_params = {
    "token": API_KEY,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url=PIXELA_END_POINT, json=user_params)  # Created a new user, this line is no longer needed
# print(response.text)  # Getting a response message

PIXELA_GRAPH_END_POINT = f"{PIXELA_END_POINT}/{USERNAME}/graphs"
# print(PIXELA_GRAPH_END_POINT)

graph_config = {
    "id": GRAPH_ID,
    "name": "Running Graph",
    "unit": "km",
    "type": "float",
    "color": "ajisai",
}

headers = {
    "X-USER-TOKEN": API_KEY,

}

# response = requests.post(url=PIXELA_GRAPH_END_POINT, json=graph_config, headers=headers)  # Finished making a graph
# print(response.text)  # Getting a response message

graph_1_end_point = f"{PIXELA_END_POINT}/{USERNAME}/graphs/{GRAPH_ID}"
# print(graph_1_end_point)

today = datetime.now()
another_day = datetime(year=2024, month=9, day=9)
# print(another_day.strftime("%Y%m%d"))

graph_update = {
    "date": another_day.strftime("%Y%m%d"),
    "quantity": "4"
}

# response = requests.post(url=graph_1_end_point, json=graph_update, headers=headers)
# print(response.text)  # Getting a response message

# Updating a pixle
pixel_end_point = f"{graph_1_end_point}/{another_day.strftime('%Y%m%d')}"
print(pixel_end_point)

pixel_update = {
    "quantity": "4"
}

# response = requests.put(url=pixel_end_point, json=pixel_update, headers=headers)
# print(f"{response.status_code}, {response.text}")  # Getting a response message


# Deleting a pixel

response = requests.delete(url=pixel_end_point, headers=headers)
print(f"{response.status_code}, {response.text}")  # Getting a response message
