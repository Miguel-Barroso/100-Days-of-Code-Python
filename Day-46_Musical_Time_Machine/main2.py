# --- Imports ---
from requests_cache import CachedSession
from datetime import timedelta
from bs4 import BeautifulSoup
# from pprint import pprint
from spotify_manager import get_track_id, create_playlist, add_tracks

session = CachedSession(  # Working with cached requests so as not to get IP-banned by Billboard
    'test_cache',
    expire_after=timedelta(hours=1),
)

# --- Input ---
date = input("Which year do you want to travel to? Type the date in this format, YYYY-MM-DD: ")
# date = "2000-08-12"  # Was the default date during testing

# --- Start Web Scraping of Billboard ---
URL = "https://www.billboard.com/charts/hot-100/" + date + "/"
print(URL)
header = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:142.0) Gecko/20100101 Firefox/142.0'}
response = session.get(URL, headers=header)
response.raise_for_status()
print(f"Response served from cache: {response.from_cache}\n")
billboard_hot100 = BeautifulSoup(response.content,'html.parser')  # Make soup of the Billboard Hot100

# with open("billboard_hot100.html","w") as file:
#     file.write(billboard_hot100.prettify())  # Had to write to a file to inspect the response because it was too big

# Angela's CSS selector
song_names_spans = billboard_hot100.select('li ul li h3')  # Much better than mine, lol
print(f"Number of Songs in Playlist: {len(song_names_spans)}\n")
artists_spans = billboard_hot100.select('span.c-label.a-no-trucate')  # Works (tried a bunch of others)
print(f"Number of Artists in Playlist: {len(artists_spans)}\n")

song_names = [song.getText().strip() for song in song_names_spans]  # Angela's solution
artist_names = [artist.getText().strip() for artist in artists_spans]  # Based on that, finding artists

# print(song_names)
# print(artist_names)

# Builds a list of Spotify URIs for each track based on artist and track name
track_uris = []
for _ in range(len(song_names)):
   track_uris.append(get_track_id(artist_names[_], song_names[_]))

valid_uris = [uri for uri in track_uris if uri is not None]  # Filter out songs that were not found

# print(track_uris)
# print(valid_uris)

# --- Creating Playlist ---
playlist_name = f"{date} Billboard Hot100"
print(f"Playlist Name: {playlist_name}")
playlist_id = create_playlist(playlist_name)
print(f"Playlist ID: {playlist_id}\n")

# Adding tracks
add_tracks(playlist_id, valid_uris)