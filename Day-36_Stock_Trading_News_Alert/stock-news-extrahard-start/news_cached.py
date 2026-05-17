import config  # Imports all environment variables and global modules
import pyshorteners  # To make short urls
import ftfy  # Fixes encoding errors when there are encoding misses "upstream" in the API source

# Instantiates a shortener object
s = pyshorteners.Shortener()

# Variables for the news functions
api_key = config.os.getenv("NEWS_API_KEY")
base_url = config.os.getenv("NEWS_API_URL")
api_function = config.os.getenv("NEWS_API_FUNCTION")

def get_latest_news(query):

    try:
        # Builds the request query based on the base url, api function, company name and includes the api key
        url = base_url + api_function
        params = {
            "q": query,
            "pageSize": 3,
            "apiKey": api_key,
        }

        r = config.cached_session.get(url=url, params=params)
        # Raises HTTP errors (4xx/5xx responses)
        r.raise_for_status()
        # Parse JSON response and store as a Python dictionary
        data = r.json()

        # Checks whether data was served from cache or fresh from API
        if r.from_cache:
            print(f"Retrieved {query} news headlines from cache.")
        else:
            print(f"Retrieved {query} news headlines fresh from API.")
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

        return ftfy.fix_text(stock_news_message)  # Fixes any encoding errors in the news article

    else:
        print(f"No news articles found for {query}.")
