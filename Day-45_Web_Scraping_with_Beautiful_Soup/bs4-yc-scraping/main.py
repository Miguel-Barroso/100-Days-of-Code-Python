from bs4 import BeautifulSoup
import requests

base_url = 'https://news.ycombinator.com/'

response = requests.get('https://news.ycombinator.com/news')

yc_webpage = response.text

soup = BeautifulSoup(yc_webpage, 'html.parser')

# article_tag = soup.find(name='a', class_='titleline')  # Finding the title of the first article;
                                                       # Angela's solution doesn't work however in the
                                                       # current iteration of HN

# article_tag = soup.select_one('.titleline a')  # Finding the title of the first article, my solution
# print(article_tag)
#
# article_text = article_tag.text  # Seems like a cleaner implementation than Angela's article_text.getText()
# print(article_text)
#
# article_link = article_tag.get('href')  # Selects the link of the first article
# print(f"{base_url}{article_link}")  # Prints the link together with the HN base url
#
# article_upvote = soup.select_one('.subline .score').text  # Selects the upvotes of the first article
# print(article_upvote)







articles = soup.find_all(name='span', class_='titleline')
headlines = []
links = []
for article in articles:
    headline = article.find('a').text
    headlines.append(headline)
    link = article.find('a').get('href')
    if 'http' not in link:
        link = base_url + link  # Some articles are hosted on HN and if so, attach the base url
    links.append(link)

print(headlines)
print(links)

scores = soup.find_all(name='span', class_='score')
# upvotes = []
# for score in scores:
#     upvotes.append(score.text)  # It works but use the alternative below:

# Alternatively:
upvotes = [int(score.getText().split()[0]) for score in scores]  # Angela used list comprehension for the above
                                                 # Note that getText() and .text are equivalent in bs4
                                                 # She is getting the number and turning it into an integer

print(upvotes)

index_highest_score = upvotes.index(max(upvotes))
print(f'{headlines[index_highest_score]}, {links[index_highest_score]}')

# --- Old stuff below ---

# for title in soup.find_all(name='span', class_='.titleline'):
#     print(title.text)
#     if title.find(class_='sitebit comhead'):
#         continue
#     print(title.text)
# for article in articles:
#     print(article.getText().split(','))
# article_texts = []
# article_links = []
# for article in articles:
#     article_text = article.text
#     article_texts.append(article_text)
#     article_link = article.get('href')
#     article_links.append(article_link)

# article_upvotes = soup.select('.subline .score').text  # Selects all article upvotes

# print(article_texts)
# print(article_links)
# print(article_upvotes)