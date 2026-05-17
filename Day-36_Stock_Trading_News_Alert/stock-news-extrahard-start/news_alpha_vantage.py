"""Attempt at rewriting the News Module to hanlde news from Alpha Vantage instead of News API
However, the news from Alpha Vantage are very one-sided. Don't think I will go further with them..."""

import config  # Imports all environment variables and global modules
import pyshorteners  # To make short urls

# Instatiates a shortener object
s = pyshorteners.Shortener()

# Variables for the news functions
api_key = config.os.getenv("ALPHA_VANTAGE_API_KEY")
base_url = config.os.getenv("ALPHA_VANTAGE_URL")
api_function = config.os.getenv("ALPHA_VANTAGE_NEWS_API_FUNCTION")

def get_latest_news(query):

    try:
        # Builds the request query based on the base url, api function, company name and includes the api key
        r = config.cached_session.get(f"{base_url}query?function={api_function}&tickers={query}&apikey={api_key}")
        # Parse JSON response and store as a Python dictionary
        data = r.json()
    except config.requests.exceptions.RequestException as err:
        print(f"❌ News API request failed: {err}")
        exit(1)

    # Check if "articles" exists and there is no empty data
    if "articles" in data and data["articles"]:
        # We are only interested in the three latest news though there are sometimes fewer headlines.
        sliced_data = data["articles"][:3]
        stock_news_message = ""  # Initializes the empty string
        for article in sliced_data:

            stock_news_message += (f"{article['title']}\n"
                                  f"{article['description']}\n"
                                  f"{s.tinyurl.short(article['url'])}\n\n")

        return stock_news_message

    else:
        print(f"No news articles found for {query}.")
