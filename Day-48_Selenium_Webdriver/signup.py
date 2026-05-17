import os
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

load_dotenv()

# Keep Chromium open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

URL = "https://secure-retreat-92358.herokuapp.com/"

# Start the webdriver with the correct options
driver = webdriver.Chrome(options=chrome_options)
driver.get(URL)

# --- Start Webscraping ---

#Fill out the form
first_name = driver.find_element(By.NAME, 'fName')
first_name.send_keys("Ahmed")
last_name = driver.find_element(By.NAME, 'lName')
last_name.send_keys("Abdul")
email = driver.find_element(By.NAME, 'email')
email.send_keys(os.getenv("FORM_EMAIL"))

# Click sign-up
button = driver.find_element(By.TAG_NAME, 'button')
button.click()
