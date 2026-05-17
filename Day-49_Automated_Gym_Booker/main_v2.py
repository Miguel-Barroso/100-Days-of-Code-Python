# --- V2 aims to book all Tuesday and Thursday 6 pm classes ---
# The original program only booked Tuesday 6 pm spinning classes

import os
import time
from dotenv import load_dotenv
from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

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
wait = WebDriverWait(driver, 2)

driver.get(GYM_URL)

# --- Step 2 — Logging into Gym Site ---
def login():
    print("Attempting to log in...")
    # Waits until the page has been loaded before continuing
    wait.until(ec.url_contains("/gym"))

    driver.find_element(By.TAG_NAME, "button").click()  # Clicks the login button

    # Wait until login form appears
    wait.until(ec.presence_of_element_located((By.ID, "email-input")))

    driver.find_element(By.CSS_SELECTOR, "#email-input").send_keys(ACCOUNT_EMAIL)
    driver.find_element(By.CSS_SELECTOR, "#password-input").send_keys(ACCOUNT_PASSWORD)
    driver.find_element(By.CSS_SELECTOR, "#submit-button").click()

    try:
        wait.until(ec.url_contains("/schedule"))
        print("✅ Logged in!")
        return True
    except TimeoutException:
        print("❌ Couldn't log in!")
        driver.refresh()
        return False

def retry(func, retries=7, description=None):
    # Retries any function passed as an argument
    for i in range(retries):
        try:
            if func():  # Successful functions return True, thus breaking this loop
                return True
        except Exception as e:
            print(e)
        print(f"Retry {i + 1}...")
    print("Failed after 7 attempts.")
    quit()


retry(login)

# --- Step 3 & 4 — Book all Classes for Next Tuesday and Thursday, 6 pm ---
# Initialize variables that keep track of existing and new bookings
class GymBooker:
    def __init__(self):
        self.new_bookings_made = 0
        self.new_waitlists_joined = 0
        self.classes_already_booked = 0
        self.waitlisted_already = 0
        # Handles all the booking logic
        self.booked_classes = {}
        self.joined_waitlists = {}
        self.check_already_booked()

    def check_already_booked(self):
        """
        Checks what has already been booked or waitlisted. This is run at the start of the booking program.
        Can only be run after login has been completed successfully.
        """
        buttons = driver.find_elements(By.TAG_NAME, "button")
        for button in buttons:
            if button.text == "Booked":
                self.classes_already_booked += 1
            if button.text == "Waitlisted":
                self.waitlisted_already += 1

    def booking(self):
        print("Attempting to book classes...")
        # Wait until schedule page appears
        try:
            wait.until(ec.url_contains("/schedule"))
        except TimeoutException:
            print("Wrong page, navigating...")  # In an edge case, you get here after failing to verify bookings
            driver.get(GYM_URL + "/schedule")  # You are moved back to the schedule page
            self.new_bookings_made = 0  # You make no assumptions as to previous bookings or waitlists joined
            self.new_waitlists_joined = 0   # You either make new bookings or just report those already made
            self.check_already_booked()  # Then check what's already been booked

        bookable_classes = 0
        joinable_waitlists = 0

        # Find all classes available
        all_days = driver.find_elements(By.CSS_SELECTOR, ".Schedule_dayGroup__y79__")

        # Go through each day and check if there is a Tuesday or Thursday
        for day in all_days:
            day_title = day.find_element(By.CSS_SELECTOR, "h2").text

            if "Tue" in day_title or "Thu" in day_title:
                # Check if it's a 6 pm class
                gym_class_cards = day.find_elements(By.CSS_SELECTOR, ".ClassCard_card__KpCx5")
                for gym_class in gym_class_cards:
                    time_text = gym_class.find_element(By.CSS_SELECTOR, "p[id^='class-time']").text

                    if "6:00 PM" in time_text:
                        gym_class_title = gym_class.find_element(By.CSS_SELECTOR,"h3[id^='class-name']").text
                        button = gym_class.find_element(By.CSS_SELECTOR, "button[id^='book-button']")
                        # scroll to the element
                        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", button)
                        if button.text == "Book Class":
                            print(f"Found a bookable class on {day_title}")
                            bookable_classes += 1
                            print(f"Total bookable classes: {bookable_classes}")
                            date = (day_title.replace("Today ", "").replace("Tomorrow ", "")
                                    .replace("(", "").replace(")", "")
                                    + ', 6:00 PM')  # Trims the date from words and parenthesis
                            print("Clicking the button now!")
                            button.click()
                            print("Clicked button, now checking for errors...")
                            try:
                                network_error = wait.until(ec.visibility_of_element_located(
                                    (By.CSS_SELECTOR, "div[id^='class-error-'")))
                                print("⚠️", network_error.text)  # Only shows if network errors occur
                            except TimeoutException:
                                self.new_bookings_made += 1
                                bookable_classes -= 1
                                self.booked_classes[date] = gym_class_title
                                print(f"✅ Successfully booked: {gym_class_title} on {day_title}")
                        if button.text == "Join Waitlist":
                            joinable_waitlists += 1
                            date = (day_title.replace("Today ", "").replace("Tomorrow ", "")
                                    .replace("(", "").replace(")", "")
                                    + ', 6:00 PM')  # Trims the date from words and parenthesis
                            button.click()
                            print("Clicked button, now checking for errors...")
                            try:
                                network_error = wait.until(ec.visibility_of_element_located(
                                    (By.CSS_SELECTOR, "div[id^='class-error-'")))
                                print("⚠️", network_error.text)
                            except TimeoutException:
                                self.new_waitlists_joined += 1
                                joinable_waitlists -= 1
                                self.joined_waitlists[date] = gym_class_title + ' (Waitlist)'
                                print(f"✅ Successfully joined waitlist: {gym_class_title} on {day_title}")
                            except Exception as e:
                                print(f"Unhandled exception: {e}")

        if bookable_classes + joinable_waitlists == 0:
            print("✅ No more classes left to book or join.")
            return True
        else:
            print("❌ Still classes left to book or join.")
            return False

    # --- Step 5 — Bookings Summary ---
    def verify_booking(self):
        # Sometimes the button clicks are not registered before moving to the next page
        time.sleep(2)

        driver.get("https://appbrewery.github.io/gym/my-bookings/")
        # Waits until the page has been loaded before continuing
        wait.until(ec.url_contains("/my-bookings"))
        print("\n--- BOOKING SUMMARY ---")
        print(f"New bookings: {self.new_bookings_made}")
        print(f"New Waitlist entries: {self.new_waitlists_joined}")
        print(f"Already booked/waitlisted: {self.classes_already_booked + self.waitlisted_already}")
        total_bookings = (self.new_bookings_made + self.new_waitlists_joined + self.classes_already_booked +
                          self.waitlisted_already)
        print(f"Total Tuesday & Thursday 6 pm classes: {total_bookings}")

        # --- Step 6 — Verify Bookings ---
        # if driver.current_url != "https://appbrewery.github.io/gym/my-bookings/":
        #     driver.get("https://appbrewery.github.io/gym/my-bookings/")

        verified_bookings = {}

        all_verified_bookings = driver.find_elements(By.CSS_SELECTOR, "div[class^='MyBookings_bookingDetails']")
        print(f"Verified bookings: {len(all_verified_bookings)}")
        for booking in all_verified_bookings:
            verified_gym_class_name = booking.find_element(By.CSS_SELECTOR, "h3").text
            verified_gym_class_date = booking.find_element(By.CSS_SELECTOR, "p").text.split("When: ")[1]
            verified_bookings[verified_gym_class_date] = verified_gym_class_name
            # print(f"Verified Gym Class: {verified_gym_class_name}, {verified_gym_class_date}")

        print("\n--- VERIFYING ON MY BOOKINGS PAGE ---")
        # Unlike the teacher who made no difference on normal bookings and waitlists, I have to split the verification
        if self.booked_classes:  # Empty dicts validates as False, thus this only runs if there's anything to check
            for date, class_name in self.booked_classes.items():
                try:
                    if verified_bookings[date] == class_name:
                        print(f"✓ Verified: {class_name} on {date}")
                except KeyError:
                    print(f"⚠️ {class_name} on {date} not verified")
        else:
            print("No bookings to verify")

        if self.joined_waitlists:  # Empty dicts validates as False, thus this only runs if there's anything to check
            for date, class_name in self.joined_waitlists.items():
                try:
                    if verified_bookings[date] == class_name:
                        print(f"✓ Verified: {class_name} on {date}")
                except KeyError:
                    print(f"⚠️ {class_name} on {date} not verified")
        else:
            print("No waitlists to verify")

        total_verified = len(verified_bookings)
        print("\n--- VERIFICATION RESULTS ---")

        print(f"Expected: {total_bookings}")
        print(f"Found: {total_verified}")
        if total_bookings != total_verified:
            print(f"❌ MISMATCH: Missing -1 bookings")
            booker.booking()
            return False
        else:
            print(f"✅ SUCCESS: All bookings verified!")
            return True

booker = GymBooker()

retry(booker.booking)

retry(booker.verify_booking)