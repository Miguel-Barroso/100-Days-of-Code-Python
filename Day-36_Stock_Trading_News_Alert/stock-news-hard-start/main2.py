import os
from dotenv import load_dotenv
load_dotenv()

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
STOCK_API_KEY = os.getenv("STOCK_API_KEY")
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
NEWS_API_KEY = os.getenv("NEWS_API_KEY")



#TODO: 1 Check for stock price movements (stocks open 9:30 US/Eastern)
# Check price at market close yesterday (16:00 US/Eastern), e.g., 13th of September
# Compare with price at market close day before yesterday (16:00 US/Eastern) e.g., 12th of September

stock_parameters = {
    "function": "TIME_SERIES_DAILY",  # Returns the OHLCV values over the course of a day/days
    "symbol": "TSLA",
    "apikey": STOCK_API_KEY,
}

import requests

stock_response = requests.get(STOCK_ENDPOINT, params=stock_parameters)
stock_response.raise_for_status()  # Raise any HTTP errors
stock_data = stock_response.json()["Time Series (Daily)"]
stock_data_list = [value for (key, value) in stock_data.items()]  # The days (values) of the dictionary are now in a list
# print(stock_data_list)
yesterday = stock_data_list[0]
yesterday_closing_price = yesterday["4. close"]
print(yesterday_closing_price)
day_before_yesterday = stock_data_list[1]
day_before_yesterday_closing_price = day_before_yesterday["4. close"]
print(day_before_yesterday_closing_price)

# Calculating the price deltas
difference = round(float(yesterday_closing_price) - float(day_before_yesterday_closing_price), 2)
up_down = None
if difference > 0:
    up_down = "🔺"
else:
    up_down = "🔻"

percent_difference = round((difference/float(yesterday_closing_price) * 100), 2)
print(f"A price difference of ${difference}")
print(f"In other words a change of {percent_difference}%")
message_header = f"{STOCK}: {up_down}]{percent_difference}%"

if difference > 0:
    news_parameters = {
        # "q": "tesla",
        "qInTitle": COMPANY_NAME,
        "apiKey": NEWS_API_KEY,
        # "from": EST_yesterday,  # To get the latest news
    }
    news_response = requests.get(NEWS_ENDPOINT, params=news_parameters)
    news_response.raise_for_status()  # Raise HTTP errors
    articles = news_response.json()["articles"]
    three_articles = articles[:3]  # Uses slice to get the first three list items
    # print(three_articles)
    formatted_articles = [f"Headline: {article['title']}\nBrief: {article['description']}\n{article['url']}" for article in three_articles]
    # print(formatted_articles)
    from twilio.rest import Client

    # Twilio Settings
    account_sid = os.getenv("TWILIO_ACCOUNT_SID")
    auth_token = os.getenv("TWILIO_AUTH_TOKEN")

    client = Client(account_sid, auth_token)

    for article in formatted_articles:
        message = client.messages.create(

            body=f"{message_header}\n{article}",
            from_=os.getenv("TWILIO_FROM_NUMBER"),
            to=os.getenv("TWILIO_TO_NUMBER")

        )

else:
    print("Nothing new...")
