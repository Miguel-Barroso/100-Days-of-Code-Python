# Imports the environment variables and the needed modules into Python's cache
import config

# Variables for the stock functions
api_key = config.os.getenv("ALPHA_VANTAGE_API_KEY")
base_url = config.os.getenv("ALPHA_VANTAGE_URL")
api_function = config.os.getenv("ALPHA_VANTAGE_API_FUNCTION")

def get_closing_prices_difference(ticker):
    """
    Returns the percent difference of the two most recent closing prices for the queried stock.
    """
    try:
        # Builds the request query based on the base url, api function, stock symbol/ticker and includes the api key
        r = config.requests.get(f"{base_url}query?function={api_function}&symbol={ticker}&apikey={api_key}")
        # Raises HTTP errors (4xx/5xx responses)
        r.raise_for_status()
        # Parse JSON response and store as a Python dictionary
        data = r.json()
    except config.requests.exceptions.RequestException as err:
        print(f"API Request failed: {err}")
        exit(1)  # Exits the program with a non-zero exit code

    '''
    The API returns JSON with two initial entries, 'Metadata' and 'Time Series (Daily)'.
    The second entry in turn contains 30 date entries, each containing information such as 'open', 'high', 'low', etc.
    For example, "data['Time Series (Daily)'][2025-03-14]['4. close']" returns the closing price on 2025-03-14.
    In order to access the most recent closing price and the previous closing prices, the data is accessed through a
    series of lists. This eliminates the need to specify specific dates or to use the date and time zones libraries 
    since the latest closing price is always the first entry and the previous closing price is always the second entry.
    '''

    # Checks whether API rate limit has been reached in which case only one entry is returned from the API
    if len(data) == 1:
        print(data)
        exit(1)

    # Picks 'Time Series (Daily)' and not 'Metadata'
    time_series_daily = list(data.values())[1]
    # Picks the most recent date
    recent_date = list(time_series_daily.keys())[0]
    # Picks the most recent closing price
    recent_closing_price = float(time_series_daily[recent_date]['4. close'])
    # Prints the date and the closing price
    #print(f"Closing price on {recent_date}: ${recent_closing_price}")
    # Picks the previous date
    previous_date = list(time_series_daily.keys())[1]
    # Picks the previous closing price
    previous_closing_price = float(time_series_daily[previous_date]['4. close'])
    #print(f"Closing price on {previous_date}: ${previous_closing_price}")

    # Returns the percent difference in closing prices
    return round(((recent_closing_price - previous_closing_price) / previous_closing_price * 100), 2)
