from requests_cache import CachedSession
from bs4 import BeautifulSoup
from datetime import timedelta
from notifications_manager import send_email

session = CachedSession(
    'test_cache',
    expire_after=timedelta(hours=1),
)

# --- Set Price Target ---
price_target = 100  # In USD

# --- Start Web Scraping of Amazon Clone ---
# URL = "https://appbrewery.github.io/instant_pot/"  # Test Example
URL = "https://www.amazon.com/dp/B075CYMYK6?th=1"  # Live Website
header = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:142.0) Gecko/20100101 Firefox/142.0',
          'Accept-Language': 'en-US,en;q=0.5',
          }
response = session.get(URL, headers=header)
response.raise_for_status()
print(f"Response served from cache: {response.from_cache}\n")

soup = BeautifulSoup(response.content, 'html.parser')  # Uses html parser to make soup on content (correct encoding)

# Finding the Product Title
product_title_tags = soup.select('#productTitle.a-size-large.product-title-word-break')
# print(f"Length of product_title_tags: {len(product_title_tags)}")
product_title = product_title_tags[0].get_text().split('\n')[0].strip().split(',')[0] # Grabs the product title

print(product_title)

# Finding the Product Price
product_price_tags = soup.select('.a-offscreen')  # Best selector I could find
# print(f"Length of product_price_tags: {len(product_price_tags)}")  # Returned only one tag
product_price = str(product_price_tags[0]).split('$')[1]  # Had to make a string out of the list object
product_price = float(product_price.split('<')[0])  # After removing '$', removing last html tag, making a float
print(f"Product price: ${product_price}")

# --- Sending an Email if Price is Below Alert Threshold ---
if product_price < price_target:
    send_email(f"Price of {product_title} is now lower than ${price_target}!")
