import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇

response = requests.get(URL)
response.raise_for_status()

soup = BeautifulSoup(response.content, 'html.parser')  # Don't use response.text, use response.content
                                                               # You get encoding issues otherwise

movies = soup.find_all(name='h3', class_='title')
for movie in reversed(movies):
    with open('movies.txt', 'a') as file:
        file.write(f"{movie.text}\n")
