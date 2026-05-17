from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


# Keep Chromium browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)  # Instantiate a new Chrome driver
driver.get("https://en.wikipedia.org/wiki/Main_Page")

articles = driver.find_elements(By.CSS_SELECTOR, value='#articlecount a')[1]  # Finds the article count
print(articles.text)

# Angela's solution
# driver.find_element(By.CSS_SELECTOR, value='#articlecount')  # Does not work on current wikipedia

# Find element by Link Text and click
# all_portals = driver.find_element(By.LINK_TEXT, value='Content portals')
# all_portals.click()

# Find element by name, type and Enter
search = driver.find_element(By.NAME, value='search')
search.send_keys("Python")
search.send_keys(Keys.RETURN)
# Can also be chained like this:
# search.send_keys("Python", Keys.ENTER)

