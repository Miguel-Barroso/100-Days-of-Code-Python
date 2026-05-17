## My solution
### My solution works and has a slew of nifty features
- .env file for credentials
- chrome_profile, allows you to click accept cookies and other pop-ups once so you don't have to repeat this
- dynamic waiting for elements to become ready using WebDriverWait and expected_condition (please read the Selenium docs for more)

### Here is the code:

```
import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

# Global variables
PROMISED_DOWN = 1000
PROMISED_UP = 1000
TWITTER_EMAIL = os.environ.get("TWITTER_EMAIL")
TWITTER_PASSWORD = os.environ.get("TWITTER_PASSWORD")


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
        self.wait = WebDriverWait(self.driver, 60)


    def get_internet_speed(self):
        # Get the Speed Test by Ookla website
        speed_test_url = "https://www.speedtest.net"
        self.driver.get(speed_test_url)
        self.wait.until(ec.url_contains("https://www.speedtest.net"))
        # Click the Go button
        self.wait.until(ec.presence_of_element_located((By.CSS_SELECTOR, ".js-start-test")))
        go_button = self.driver.find_element(By.CSS_SELECTOR, ".js-start-test")
        go_button.click()
        # Get the speed test results
        self.wait.until(ec.presence_of_element_located((By.CSS_SELECTOR, ".audience-survey")))  # Appears when finished
        download_speed = self.driver.find_element(By.CSS_SELECTOR, ".download-speed")
        upload_speed = self.driver.find_element(By.CSS_SELECTOR, ".upload-speed")
        print(f"Download speed: {download_speed.text}, Upload speed: {upload_speed.text}")


    def tweet_at_provider(self):
        pass


twitter_bot = InternetSpeedTwitterBot()
time.sleep(2)
twitter_bot.get_internet_speed()
twitter_bot.tweet_at_provider()
```