import config  # Imports all environment variables and global modules
import pyshorteners  # To make short urls

s = pyshorteners.Shortener()

# Variables for the news functions
api_key = config.os.getenv("NEWS_API_KEY")
base_url = config.os.getenv("NEWS_API_URL")
api_function = config.os.getenv("NEWS_API_FUNCTION")

def get_latest_news(query):

    # Builds the request query based on the base url, api function, company name and includes the api key
    r = config.requests.get(f"{base_url}{api_function}?q={query}&language=en&apiKey={api_key}")
    # Parse JSON response and store as a Python dictionary
    data = r.json()

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
