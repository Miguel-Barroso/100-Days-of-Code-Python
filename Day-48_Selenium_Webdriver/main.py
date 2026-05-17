from selenium import webdriver
from selenium.webdriver.common.by import By

# Keep Chromium browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

# driver.get("https://www.amazon.com")
# driver.get("https://www.amazon.com/dp/B075CYMYK6?th=1")

# price_dollar = driver.find_element(By.CLASS_NAME, "a-price-whole")
# price_cents = driver.find_element(By.CLASS_NAME, "a-price-fraction")
# print(f"The price is ${price_dollar.text}.{price_cents.text}")

driver.get("https://www.python.org/")

# search_bar = driver.find_element(By.NAME, "q")
# print(search_bar.get_attribute("placeholder"))
# button = driver.find_element(By.NAME, "submit")
# print(button.size)
# documentation_link = driver.find_element(By.CSS_SELECTOR, ".documentation-widget a")
# print(documentation_link.text)
#
# bug_link = driver.find_element(By.XPATH, value='//*[@id="site-map"]/div[2]/div/ul/li[3]/a')
# print(bug_link.text)

upcoming_event_dates = driver.find_elements(By.CSS_SELECTOR, "time")[5:]  # Get event dates
# Angela's solution: .event-widget time
upcoming_event_titles = driver.find_elements(By.CSS_SELECTOR, ".event-widget.last a")[1:]  # Get event names
# Angela's solution: .event-widget li a
all_events = {}

# The below works but I updated according to Angela's solution below this
# for _ in range(len(upcoming_event_titles)):
#     event = {  # This creates a new dictionary for each loop iteration
#         'date':upcoming_event_dates[_].text,
#         'name':upcoming_event_titles[_].text
#     }
#     all_events[_] = event

for _ in range(len(upcoming_event_titles)):
    all_events[_] = {
        'time': upcoming_event_dates[_].text,
        'name': upcoming_event_titles[_].text,
    }

print(all_events)

#  driver.close()  # Closes a single tab
driver.quit()  # Quits the entire program