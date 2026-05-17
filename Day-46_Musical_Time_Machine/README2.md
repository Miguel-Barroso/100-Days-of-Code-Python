# Scraping Billboard Hot 100 with BeautifulSoup

The **Billboard Hot 100** website was accessed on **2025-08-29**.  

At first, the selectors for the song names seemed really complicated.  
It was not enough to simply select all `<h3>` tags with `id="title-of-a-story"` and `class="c-title"`.

---

## Finding the Correct Selector

To figure this out, I opened **Developer Tools (Firefox)** and ran:

```javascript
document.querySelectorAll(
  'div.o-chart-results-list-row-container:nth-child(1) > ul:nth-child(1) > li:nth-child(4) > ul:nth-child(1) > li:nth-child(1) > h3:nth-child(1)'
)
```

This query was copied directly by **inspecting a song name** and selecting  
“Copy → CSS Selector”.

The console returned:

```javascript
NodeList [
  h3#title-of-a-story.c-title.a-font-basic.u-letter-spacing-0010.u-max-width-397.lrv-u-font-size-16.lrv-u-font-size-14@mobile-max.u-line-height-22px.u-word-spacing-0063.u-line-height-normal@mobile-max.a-truncate-ellipsis-2line.lrv-u-margin-b-025.lrv-u-margin-b-00@mobile-max
]
```

---

## Cleaning Up the Selector

Since BeautifulSoup cannot handle CSS classes containing `@`, I stripped those away.  
This left me with a working selector:

```python
songs = billboard_hot100.select(
    'h3#title-of-a-story.c-title.a-font-basic.u-letter-spacing-0010.u-max-width-397.lrv-u-font-size-16.u-line-height-22px.u-word-spacing-0063.a-truncate-ellipsis-2line.lrv-u-margin-b-025'
)
```

With this, I was able to successfully grab all the song names.

---

## Key Insights

- The best help came from [this guide](https://scrapeops.io/python-web-scraping-playbook/python-beautifulsoup-returns-empty-list/#step-1-check-if-response-contains-data),  
  which showed how to use `document.querySelectorAll('h1')` in Developer Tools and then reuse that selector in BeautifulSoup.  
- The **response contains rendered HTML**, which included a lot of blank spaces before and after the song names.  
  - Using `.get_text(strip=True)` in BeautifulSoup cleaned these up, keeping the titles intact.  
- Always use `response.content` instead of `response.text` to ensure proper encoding when parsing with BeautifulSoup.

---

## Minimal Working Example

Here’s a Python script that fetches all 100 songs for a given date:

```python
from requests_cache import CachedSession
from datetime import timedelta
from bs4 import BeautifulSoup

# Setup caching so we don't re-fetch the same page during testing
session = CachedSession(
    'test_cache',
    expire_after=timedelta(hours=1),
)

# Choose a date in YYYY-MM-DD format
date = "2000-08-12"
URL = "https://www.billboard.com/charts/hot-100/" + date + "/"

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:142.0) Gecko/20100101 Firefox/142.0'
}
response = session.get(URL, headers=headers)
response.raise_for_status()

# Use response.content for correct encoding
soup = BeautifulSoup(response.content, 'html.parser')

# Extract song titles
titles = soup.select("h3#title-of-a-story.c-title.a-font-basic.u-letter-spacing-0010.u-max-width-397.lrv-u-font-size-16.u-line-height-22px.u-word-spacing-0063.a-truncate-ellipsis-2line.lrv-u-margin-b-025")
songs = [t.get_text(strip=True) for t in titles]

# Print the Hot 100 list
for i, song in enumerate(songs, start=1):
    print(f"{i}. {song}")
```

---

## Example Output

```
1. Incomplete
2. It's Gonna Be Me
3. Bent
4. Doesn't Really Matter
5. He Wasn't Man Enough
...
100. I Need A Girl (Part One)
```

---

✅ With this approach, you can scrape the **Billboard Hot 100** reliably,  
while keeping song names clean and intact.
