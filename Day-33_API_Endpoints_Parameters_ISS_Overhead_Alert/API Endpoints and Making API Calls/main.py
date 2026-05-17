import requests

# Use the get method to get data as an object from one of the endpoints
response = requests.get(url="http://api.open-notify.org/iss-now.json")

# Tells the developer what the error, if any there was in accessing the API
response.raise_for_status()

# Accessing the data of the response object in the form of JSON
data = response.json()
# print(data["iss_position"])  # Works like a python dictionary now

longitude = data["iss_position"]["longitude"]
latitude = data["iss_position"]["latitude"]

iss_position = (longitude, latitude)
print(iss_position)
