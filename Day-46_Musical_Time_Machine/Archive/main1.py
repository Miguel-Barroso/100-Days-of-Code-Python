from requests_cache import CachedSession
from datetime import timedelta
from bs4 import BeautifulSoup

session = CachedSession(
    'test_cache',
    expire_after=timedelta(hours=1),
)

# date = input("Which year do you want to travel to? Type the date in this format, YYYY-MM-DD: ")
date = "2000-08-12"
URL = "https://www.billboard.com/charts/hot-100/" + date + "/"
print(URL)
header = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:142.0) Gecko/20100101 Firefox/142.0'}
response = session.get(URL, headers=header)
response.raise_for_status()
print(f"Response served from cache: {response.from_cache}\n")

billboard_hot100 = soup = BeautifulSoup(response.content,'html.parser')

# with open("billboard_hot100.html","w") as file:
#     file.write(billboard_hot100.prettify())

# Sorry for the crazy CSS selector, please check README1.md
songs = billboard_hot100.select('h3#title-of-a-story.c-title.a-font-basic.u-letter-spacing-0010.u-max-width-397.lrv-u-font-size-16.u-line-height-22px.u-word-spacing-0063.a-truncate-ellipsis-2line.lrv-u-margin-b-025')
# print(f"Number of Songs in Playlist: {len(songs)}\n")
artists = billboard_hot100.select('span.c-label.a-no-trucate')  # Was able to simply the CSS selector quite a bit
# print(f"Number of Artists in Playlist: {len(artists)}\n")
songs_list = []
artists_list = []
for song in songs:
    songs_list.append((song.get_text(strip=True)))  # This function strips away any rendered blank spaces
for artist in artists:
    artists_list.append((artist.get_text(strip=True)))

for _ in range(len(songs_list)):
    print(f"{_ + 1}. {songs_list[_]} - {artists_list[_]}\n")