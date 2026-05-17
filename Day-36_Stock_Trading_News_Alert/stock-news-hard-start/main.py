import os
from dotenv import load_dotenv
load_dotenv()

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
STOCK_API_KEY = os.getenv("STOCK_API_KEY")

NEWS_ENDPOINT = "https://newsapi.org/v2/everything"


#TODO: 1 Check for stock price movements (stocks open 9:30 US/Eastern)
# Check price at market close yesterday (16:00 US/Eastern), e.g., 13th of September
# Compare with price at market close day before yesterday (16:00 US/Eastern) e.g., 12th of September

stock_parameters = {
    "function": "TIME_SERIES_DAILY",  # Returns the OHLCV values over the course of a day/days
    "symbol": "TSLA",
    "apikey": STOCK_API_KEY,
}

import requests, pytz
from datetime import datetime, timedelta

# Define the US/Eastern time zone
EST = pytz.timezone("US/Eastern")  # This library handles daylight saving time transitions(!)

# Get the current time in EST
EST_today = datetime.now(EST)

# Get the yesterday's time in EST
EST_yesterday = EST_today - timedelta(days=1)

# Formatting the into YYYY-MM-DD format
EST_today = EST_today.strftime("%Y-%m-%d")
EST_yesterday = EST_yesterday.strftime("%Y-%m-%d")

# Getting the stock prices from the API
# stock_response = requests.get(STOCK_ENDPOINT, params=stock_parameters)
#
# stock_data = stock_response.json()
# print(stock_data)  # NB! Limited to 25 requests per day on the free tier
# latest_closing_price = stock_data["Time Series (Daily)"][EST_today]["4. close"]
# print(f"Latest {STOCK} closing price on {EST_today}: ${latest_closing_price}")
# previous_closing_price = stock_data["Time Series (Daily)"][EST_yesterday]["4. close"]
# print(f"Previous {STOCK} closing price on {EST_yesterday}: ${previous_closing_price}")

# Calculating the price deltas
# price_delta = float(previous_closing_price) - float(latest_closing_price)
# price_delta = round(abs(price_delta), 2)
# price_delta_percentage = round((price_delta/float(latest_closing_price) * 100), 2)
# print(f"A price difference of ${price_delta}")
# print(f"In other words a change of {price_delta_percentage}%")

## STEP 1: Use https://newsapi.org/docs/endpoints/everything
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
#HINT 1: Get the closing price for yesterday and the day before yesterday. Find the positive difference between the two prices. e.g. 40 - 20 = -20, but the positive difference is 20.
#HINT 2: Work out the value of 5% of yerstday's closing stock price. 
#TODO: 2 Get news articles

NEWS_API_KEY = os.getenv("NEWS_API_KEY")

news_parameters = {
    "q": "tesla",
    "apiKey": NEWS_API_KEY,
    "from": EST_yesterday,  # To get the latest news
}

news_response = requests.get(NEWS_ENDPOINT, params=news_parameters)
news_response.raise_for_status()  # Raise HTTP errors
message_content = []
for _ in range(0, 3):  # To get the first three articles
    headline = news_response.json()["articles"][_]["title"]
    brief = news_response.json()["articles"][_]["description"]
    message_content.append(f"Headline {_ + 1}: {headline}\n{brief}")  # Saves the news headlines in a list

price_delta_percentage = 5
message_header = f"{STOCK}: 🔺{price_delta_percentage}%"
print(message_header)
print(message_content[0])

## STEP 2: Use https://newsapi.org/docs/endpoints/everything
# Instead of printing ("Get News"), actually fetch the first 3 articles for the COMPANY_NAME. 
#HINT 1: Think about using the Python Slice Operator



## STEP 3: Use twilio.com/docs/sms/quickstart/python
# Send a separate message with each article's title and description to your phone number. 
#HINT 1: Consider using a List Comprehension.



#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

