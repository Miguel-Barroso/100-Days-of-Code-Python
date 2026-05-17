import os

from dotenv import load_dotenv
from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait

load_dotenv()  # Loads the environment variables

# Global variables
PROMISED_DOWN = 1000
PROMISED_UP = 1000
TWITTER_EMAIL = os.environ.get("TWITTER_EMAIL")
TWITTER_PASSWORD = os.environ.get("TWITTER_PASSWORD")
TWITTER_USERNAME = os.environ.get("TWITTER_USERNAME")


class InternetSpeedTwitterBot:
    def __init__(self, speed: int | None = None):  # A Pythonic way of hinting what a variable should be
        # Internet speed variables initialization
        self.up = speed
        self.down = speed

        # Keep Chromium browser open after program finishes
        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_experimental_option("detach", True)

        # Give Selenium its own user profile
        user_data_dir = os.path.join(os.getcwd(), "chrome_profile")

        # Tell Chrome Driver to use this directory to store all settings
        self.chrome_options.add_argument(f"--user-data-dir={user_data_dir}")
        # Start the driver with the above options
        self.driver = webdriver.Chrome(options=self.chrome_options)
        self.wait60 = WebDriverWait(self.driver, 60)
        self.wait10 = WebDriverWait(self.driver, 10)
        self.wait2 = WebDriverWait(self.driver, 2)


    def get_internet_speed(self):
        # Get the Speed Test by Ookla website
        print("Navigating to speedtest.net")
        speed_test_url = "https://www.speedtest.net"
        self.driver.get(speed_test_url)
        self.wait2.until(ec.url_contains("https://www.speedtest.net"))
        # Click the Go button
        go_button = self.wait2.until(ec.presence_of_element_located((By.CSS_SELECTOR, ".js-start-test")))
        go_button.click()
        # Get the speed test results
        print("Waiting for speed test results...")
        self.wait60.until(ec.presence_of_element_located((By.CSS_SELECTOR, ".audience-survey")))  # Appears at the end
        download_speed = self.driver.find_element(By.CSS_SELECTOR, ".download-speed")
        upload_speed = self.driver.find_element(By.CSS_SELECTOR, ".upload-speed")
        message = f"Download speed: {download_speed.text} Mbps, Upload speed: {upload_speed.text} Mbps"
        print(message)
        return message


    def twitter_login(self):
        # Login steps
        print("Logging in to Twitter")
        # Click the login button
        login_button = self.wait10.until(
            ec.presence_of_element_located((By.CSS_SELECTOR, "a[data-testid='loginButton']")))
        login_button.click()
        # Fill in the email
        user_input = self.wait2.until(
            ec.presence_of_element_located((By.CSS_SELECTOR, "input[autocomplete='username']")))
        user_input.send_keys(TWITTER_EMAIL)
        # Click the next button
        next_button = self.wait2.until(ec.presence_of_element_located((By.XPATH, "//span[text()='Next']")))
        next_button.click()

        # Sometimes Twitter asks for username as well
        try:
            # Fill in username
            password_input = self.wait2.until(ec.presence_of_element_located((By.CSS_SELECTOR,
                                                                              "input[data-testid='ocfEnterTextTextInput']")))
            password_input.send_keys(TWITTER_USERNAME)
            # Click the next button
            next_button = self.wait2.until(ec.presence_of_element_located((By.XPATH, "//span[text()='Next']")))
            next_button.click()
        except TimeoutException:
            print("Username not needed for login.")

        # Fill in the password
        password_input = self.wait2.until(ec.presence_of_element_located((By.CSS_SELECTOR, "input[name='password']")))
        password_input.send_keys(TWITTER_PASSWORD)
        # Click the 2nd Login button
        login_button = self.wait60.until(ec.presence_of_element_located((By.XPATH, "//span[text()='Log in']")))
        login_button.click()

        # Sometimes login gets blocked due to suspicious activity
        try:
            got_it_button = self.wait10.until(
                ec.presence_of_element_located((By.CSS_SELECTOR, "button[data-testid='OCF_CallToAction_Button']")))
            print("Login attempt go blocked, retrying...")
            got_it_button.click()
            self.twitter_login()
        except TimeoutException:
            print("Hold on...")

        # Sometimes 2FA is needed in this step
        try:
            if self.wait10.until(ec.presence_of_element_located((By.XPATH,
                                                                 "//span[text()='Enter code']"))):
                print("⚠️ Please enter the 2FA code and click Next within 60s.")
        except TimeoutException:
            print("2FA not needed")

        # Check if login was successful
        if self.wait60.until(ec.url_to_be("https://x.com/home")):
            print("Logged in successfully!")
        else:
            print("Login failed")

    def tweet_at_provider(self):
        # Get the Twitter website
        print("Navigating to Twitter...")
        twitter_url = "https://x.com"
        self.driver.get(twitter_url)
        self.wait2.until(ec.url_contains("https://x.com"))

        try:
            if self.wait2.until(ec.url_to_be("https://x.com/home")):
                print("Already logged in!")
        except TimeoutException:
            self.twitter_login()

        # Sending Internet speed complain steps
        # Click the Post button
        print("Sending a Tweet...")
        post_button = self.wait2.until(ec.presence_of_element_located((By.XPATH, "//span[text()='Post']")))
        post_button.click()
        # Fill in the complaint
        tweet = self.wait2.until(ec.presence_of_element_located((By.XPATH,
                                                         "//*[@id='layers']/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div[2]/div[1]/div/div/div/div[1]/div[2]/div/div/div/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div/div/div[2]/div/div/div/div")))
        tweet.send_keys(f"Hi ZTV! Why is my Internet speed slow?\n"
                        f"{internet_speeds}")
        # Send the Tweet
        post_button = self.wait2.until(ec.presence_of_element_located((By.XPATH, "//span[text()='Post']")))
        post_button.click()

        # Navigate to profile
        print("Showing profile...")
        self.driver.get(f"https://x.com/{TWITTER_USERNAME}")

# Instantiates the object
twitter_bot = InternetSpeedTwitterBot()
# internet_speeds = "Nothing to report"  # For test purposes
internet_speeds = twitter_bot.get_internet_speed()
twitter_bot.tweet_at_provider()