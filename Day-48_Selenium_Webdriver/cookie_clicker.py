import random

from selenium import webdriver
from selenium.common import NoSuchElementException, StaleElementReferenceException
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
# Reusing a real browser profile carries cookies and session info, so Cloudflare treats it like a human user.
chrome_options.add_argument("user-data-dir=/Users/mb/Library/Application Support/Chromium")
chrome_options.add_argument("profile-directory=Default")
chrome_options.add_experimental_option("detach", True)
chrome_options.binary_location = "/opt/homebrew/bin/chromium"

# Start the webdriver with the correct options
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://orteil.dashnet.org/cookieclicker/")

# --- Solve CAPTCHAs ---
while True:
    captcha = input("Did you solve all CAPTCHA, Y/N?")
    if captcha.lower() == "y":
        break

# --- Start Webscraping ---
# Finding cookie
cookie = driver.find_element(By.CSS_SELECTOR, "#bigCookie")
# Finding powerups
cursor = driver.find_element(By.CSS_SELECTOR, "#product0")
grandma = driver.find_element(By.CSS_SELECTOR, "#product1")
farm = driver.find_element(By.CSS_SELECTOR, "#product2")
mine = driver.find_element(By.CSS_SELECTOR, "#product3")
factory = driver.find_element(By.CSS_SELECTOR, "#product4")
# Finding upgrades
# If an upgrade is not available, just click the big cookie button again

# --- Defining the tasks ---
# Defining powerups
def click_cursor():
    print(f"Clicking cursor powerup")
    cursor.click()

def click_grandma():
    print(f"Clicking grandma powerup")
    grandma.click()

def click_farm():
    print(f"Clicking farm powerup")
    farm.click()

def click_mine():
    print(f"Clicking mine powerup")
    mine.click()

def click_factory():
    print(f"Clicking factory powerup")
    factory.click()

# Defining upgrades
# They only become available after a certain conditions are met
# If they are not available, they will only result in a cookie click
def first_upgrade():
    try:
        driver.find_element(By.CSS_SELECTOR, "#upgrade0").click()
        print("Clicking first upgrade")
    except (NoSuchElementException, StaleElementReferenceException):
        cookie.click()

def second_upgrade():
    try:
        driver.find_element(By.CSS_SELECTOR, "#upgrade1").click()
        print("Clicking second upgrade")
    except (NoSuchElementException, StaleElementReferenceException):
        cookie.click()

def third_upgrade():
    try:
        driver.find_element(By.CSS_SELECTOR, "#upgrade2").click()
        print("Clicking third upgrade")
    except (NoSuchElementException, StaleElementReferenceException):
        cookie.click()

def fourth_upgrade():
    try:
        driver.find_element(By.CSS_SELECTOR, "#upgrade3").click()
        print("Clicking fourth upgrade")
    except (NoSuchElementException, StaleElementReferenceException):
        cookie.click()

def fifth_upgrade():
    try:
        driver.find_element(By.CSS_SELECTOR, "#upgrade4").click()
        print("Clicking fifth upgrade")
    except (NoSuchElementException, StaleElementReferenceException):
        cookie.click()

powerups = {'0': click_cursor,
            '1': click_grandma,
            '2': click_farm,
            '3': click_mine,
            '4': click_factory,
            '5': first_upgrade,
            '6': second_upgrade,
            '7': third_upgrade,
            '8': fourth_upgrade,
            '9': fifth_upgrade,
            }

# --- Start Clicking

while True:
    print(f"Clicking cookie!")
    cookie.click()
    random_int = random.randint(0, len(powerups) - 1)
    powerups[str(random_int)]()  # Don't forget to call the function with ()
