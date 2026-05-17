# --- SF Rental Research ---

# Capstone Project to scrape data from a website and proceed with automated data entry

# --- Program Requirements ---

# TODO 1: Create a new Google Form ✅ (URL loaded from .env)

# TODO 2: Access the Zillow clone website
ZILLOW_URL = "https://appbrewery.github.io/Zillow-Clone/"

# TODO 3: Scrape using bs4 all the listings ✅
#  Search criteria:
#  - San Francisco, CA
#  - For Rent
#  - Up to $3K
#  - 1+ bedroom
#  Create three lists, clean up any data:
#  - Addresses
#  - Prices per month
#  - Links to the listings

# TODO 4: Fill out the Google Form using Selenium ✅

# TODO 5: Create a Google Sheet ✅


# --- Project Start ---

import requests
import re
import os

from dotenv import load_dotenv
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait

load_dotenv()
GOOGLE_FORM_URL = os.getenv("GOOGLE_FORM_URL")

# --- Parsing the Zillow Website with bs4 ---

response = requests.get(ZILLOW_URL, headers={'User-Agent': 'Mozilla/5.0',
                                             'Accept-Language': 'en-US,en;q=0.5'})
response.raise_for_status()
zillow_webpage = response.content  # Do not use response.text, use response.content to avoid issues

soup = BeautifulSoup(zillow_webpage, "html.parser")

# print(soup.prettify())

#  Getting hold of all the listings
listings = soup.find_all(name="div", class_="StyledPropertyCardDataWrapper")

# Getting hold of the data
addresses = []
prices = []
links = []

for listing in listings:

    address = listing.find(name="address").text
    address = address.strip().replace("|", "")
    addresses.append(address)

    price = listing.find(name="span", class_="PropertyCardWrapper__StyledPriceLine").text
    price_cleaned = re.sub(r'\+/mo|/mo|\+\s*\d+\s*bd', '', price)  # Regex targeting all pricing variants
    prices.append(price_cleaned)

    link = listing.find(name="a", class_="StyledPropertyCardDataArea-anchor")["href"]
    links.append(link)

# Just to confirm there's no mismatch between the lists
if len(addresses) == len(prices) == len(links):
    print("All lists match!")
    print(addresses)
    print(prices)
    print(links)
else:
    print("Something went wrong!")
    exit(0)


# --- Filling out the Google Form ---

# Keep Chromium browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

# Give Selenium its own user profile
user_data_dir = os.path.join(os.getcwd(), "chrome_profile")

# Tell Chrome Driver to  use this directory to store all its settings
chrome_options.add_argument(f"user-data-dir={user_data_dir}")

# Start the driver with the above options
driver = webdriver.Chrome(options=chrome_options)
wait3 = WebDriverWait(driver, 3)

def fill_form():

    for _ in range(len(listings)):

        # Open the Google Form
        print("Navigating to Google Form...")
        driver.get(f"{GOOGLE_FORM_URL}/viewform")  # To view the form
        wait3.until(ec.url_contains(GOOGLE_FORM_URL))

        print(f"Loop iteration {_ + 1}")  # For testing purposes

        # Fill out the address
        address_field = wait3.until(ec.presence_of_element_located(
            (By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')))
        address_field.send_keys(addresses[_])

        # Fill out the price
        price_field = wait3.until(ec.presence_of_element_located(
            (By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')))
        price_field.send_keys(prices[_])

        # Fill out the link
        link_field = wait3.until(ec.presence_of_element_located(
            (By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')))
        link_field.send_keys(links[_])

        # Click the Submit button
        submit_button = wait3.until(ec.presence_of_element_located((By.CSS_SELECTOR, "div[aria-label='Submit']")))
        submit_button.click()

        try:
            wait3.until(ec.url_contains(f"{GOOGLE_FORM_URL}/formResponse"))
            print("Formed filled out successfully!")
        except TimeoutException:
            print("Timed out!")
            exit(0)

fill_form()