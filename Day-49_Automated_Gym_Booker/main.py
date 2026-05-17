import os
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
from date_handler import DateHandler

load_dotenv()

# --- Step 1 — Setup Chrome Profile and Driver ---

# Website Details & Credentials
ACCOUNT_EMAIL = os.getenv("ACCOUNT_EMAIL")
ACCOUNT_PASSWORD = os.getenv("ACCOUNT_PASSWORD")
GYM_URL = "https://appbrewery.github.io/gym/"

# Keep Chromium browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
# Give Selenium its own user profile
user_data_dir = os.path.join(os.getcwd(), "chrome_profile")
# Tell Chrome Driver to use this directory to store all settings
chrome_options.add_argument(f"--user-data-dir={user_data_dir}")

# NB: All the options need to come before the driver is started

# Start the driver with the above options
driver = webdriver.Chrome(options=chrome_options)
driver.implicitly_wait(2)  # Doesn't wait if resource is found, otherwise waits 2s before throwing an exception
                           # This applies to all driver calls
driver.get(GYM_URL)

# --- Step 2 — Logging into Gym Site ---

driver.find_element(By.TAG_NAME, "button").click()  # Clicks the login button

driver.find_element(By.CSS_SELECTOR, "#email-input").send_keys(ACCOUNT_EMAIL)
driver.find_element(By.CSS_SELECTOR, "#password-input").send_keys(ACCOUNT_PASSWORD)
driver.find_element(By.CSS_SELECTOR, "#submit-button").click()

# --- Step 3 & 4 — Book a Spin Class for Next Tuesday, 6 pm ---
new_bookings_made = 0
new_waitlists_joined = 0
# Check if class is booked already
# Find out when the next Tuesday is
next_tuesday = DateHandler().get_next_tuesday()
if next_tuesday is not None:
    gym_class_status = driver.find_element(By.CSS_SELECTOR, f"button[id^='book-button-spin-{str(next_tuesday)}-1800']")
else:
    print("No next tuesday, program exiting...")
    quit()

if gym_class_status.text == "Booked":
    print(f"Spinning Class for {next_tuesday} is already booked!")
else:
    # Click the booking button for next Tuesday's 6 pm spinning class
    driver.find_element(By.CSS_SELECTOR, f"button[id^='book-button-spin-{next_tuesday}-1800']").click()
    new_bookings_made += 1
    # Prints status in console and sends the user to their confirmed Booking's page
    print(f"This confirms your booking of spinning class, 6 pm on Next Tuesday: {next_tuesday}")

    driver.get("https://appbrewery.github.io/gym/my-bookings/")

# --- Step 5 — Bookings Summary ---
if driver.current_url != "https://appbrewery.github.io/gym/schedule/":
    driver.get("https://appbrewery.github.io/gym/schedule/")

print("--- BOOKING SUMMARY ---")

buttons = driver.find_elements(By.TAG_NAME, "button")
classes_already_booked = 0
waitlisted_already = 0
for button in buttons:
    if button.text == "Booked":
        classes_already_booked += 1
    if button.text == "Waitlisted":
        waitlisted_already += 1

print(f"Classes booked: {new_bookings_made}")
print(f"Waitlisted: {new_waitlists_joined}")
print(f"Already booked/waitlisted: {classes_already_booked + waitlisted_already}")