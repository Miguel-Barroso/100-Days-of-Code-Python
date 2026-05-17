"""
This is the Stock News Program.
It will cover a specific stock ticker, i.e., Tesla.
If the price change of the most recent closing vs the previous closing is greater than 5%, the percent difference is
returned along with the three latest news headlines and sent via Twilio.
"""

# TODO: 1
"""🏆 Best Approach

    Batch translation per company → Send one API call per company, but include all its news articles in one request.
    Split the message before sending via Twilio → Ensure each SMS is within Twilio's character limits."""

import config

# Ask the user if they want to clear the cache
print("Welcome to the Stock News Program!")
clear_cache = input("Do you want to clear the cache? (yes/no): ").strip().lower()
if clear_cache == "yes":
    config.clear_cache()

# Import modules
import stocks_cached
import news_cached
import notifications_email
import translations


# Variables
notification_threshold = 3  # For when to trigger a notification, i.e., 5% price change in absolute terms
message = ""

# Stores a list of the stock ticker and company name
stock_list = [
    ("TSLA", "Tesla"),
    ("AAPL", "Apple"),
    ("GOOGL", "Alphabet"),
    ("NVDA", "NVIDIA"),
    ("INTC", "Intel"),
    ("TSM", "TSMC")
]

def stock_news(ticker, company_name):
    """
    This is the main function of the program. It first gets the percent difference in stock prices using the stocks
    module. Then it evaluates the change if it was significant to a specific degree (i.e., 5% ). It then attaches
    either an up or down arrow as the message title. Then, it fetches up to three news headlines and their descriptions
    via the news module. The concatenated message is then sent as a message to the subscriber via the notifications
    module.
    """
    global message
    percent_difference = stocks_cached.get_closing_prices_difference(ticker)

    if abs(percent_difference) > notification_threshold:  # Checks if there has been a significant change
        if percent_difference > 0:  # Checks whether it was an increase or decrease and chooses symbol accordingly
            arrow_symbol = "↗️"
        else:
            arrow_symbol = "↘️"

        message_title = f"{ticker}: {arrow_symbol}{percent_difference}%"
        print(message_title)
        message_body = news_cached.get_latest_news(company_name)
        message += f"{message_title}\n{message_body}\n"
        if message_body is not None:  # Checks whether there were news headlines returned or not
            return message
        else:
            print(f"No message for {company_name} will be sent.")

    else:
        print(f"No significant change for {ticker}")

# Calls the main function of the program
for stock, company in stock_list:
    stock_news(stock, company)

if message != "":
    get_translation = input("Do you want to apply Japanese translation? (yes/no): ")