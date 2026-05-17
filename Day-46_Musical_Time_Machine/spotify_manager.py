import os
from pprintpp import pprint
from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyOAuth

load_dotenv()

SPOTIFY_CLIENT_ID = os.getenv('SPOTIFY_CLIENT_ID')
SPOTIFY_CLIENT_SECRET = os.getenv('SPOTIFY_CLIENT_SECRET')
SPOTIFY_REDIRECT_URI = "https://example.com/callback"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(  # Creates a Spotify session object
    client_id=SPOTIFY_CLIENT_ID,                 # Note that cache_path is deprecated and uses .sqlite per default
    client_secret=SPOTIFY_CLIENT_SECRET,
    redirect_uri=SPOTIFY_REDIRECT_URI,
    scope="playlist-modify-private",  # Note that cache_path is deprecated and instead uses .sqlite per default
    )
)

current_user = sp.current_user()  # Gets the current user, necessary to create a playlist

# results = sp.current_user_saved_tracks(limit=50)  # Need "user-library-read" scope to check a user's liked songs
# for idx, item in enumerate(results['items']):
#     track = item['track']
#     print(idx, track['artists'][0]['name'], "—", track['name'])

# current_user = sp.current_user()
# print(current_user)

# artist_name = ' Sting Featuring Cheb Mami'

# def get_artist_id(artist_name):
#     results = sp.search(q='artist:' + artist_name, type='artist', limit=1)
#     items = results['artists']['items']
#     if len(items) > 0:
#         print(f"Artist: {items[0]['name']} ID: {items[0].get('id', None)}")
#         return items[0].get('id', None)
#     else:
#         return None

# def get_track_id(artist_name, track_name):
#     q = f"artist:{artist_name} track:{track_name}"
#     results = sp.search(q=q, type="track", limit=1)
#     # print(pprint(results))
#     items = results['tracks']['items']
#     if len(items) > 0:
#         print(f"Track: {items[0]['name']} ID: {items[0].get('id', None)}")
#         return items[0].get('id', None)
#     else:
#         print("No track found")
#         return None

def get_track_id(artist, track):
        q = f"artist:{artist.split('Featuring')} track:{track}"  # Search got messed up by the word 'Featuring'
        results = sp.search(q=q, type="track", limit=1)
        # print(pprint(results))
        items = results['tracks']['items']
        if items:
            print(f"{artist} — {track} ID: {items[0]['uri']}")
            return items[0]['uri']
        else:
            print(f"--- Could not find {artist} — {track} ---")
            return None

# get_track_id("Sisqo", "Incomplete")

def create_playlist(playlist_name):  # NB: Only run this once since Spotify allows multiple playlists with the same name
    """
    Creates a playlist with the given name for the current user and returns its ID.
    """
    global current_user
    results = sp.user_playlist_create(
        current_user['display_name'],
        name=playlist_name,
        public=False,
        collaborative=False,
        description=f"Welcome to the Time Machine, taking you way back to {playlist_name.split()[0]}~"
        )
    return results["id"]

def add_tracks(playlist_id, track_uris):
    """
    Adds tracks to a playlist with the given ID. Tracks must be supplied as a list of track URIs.
    """
    return sp.playlist_add_items(playlist_id, track_uris)
