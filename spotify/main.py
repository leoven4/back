from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials, SpotifyOAuth
from pprint import pprint
from constants import constants

page_root = constants['page_root']
DATE = constants['DATE']
CLIENT_ID = constants['CLIENT_ID']
CLIENT_SECRET = constants['CLIENT_SECRET']
URI = constants['URI']
USER_ID = constants['USER_ID']

response = requests.get(page_root + DATE)
soup = BeautifulSoup(response.text, 'html.parser')

tags = soup.find_all(class_='o-chart-results-list-row-container')

titles = [title.h3.getText().replace('\n', '').replace('\t', '') for title in tags]
artists = [artist.h3.find_next().getText().replace('\n', '').replace('\t', '') for artist in tags]

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID,
                                               client_secret=CLIENT_SECRET,
                                               redirect_uri=URI,
                                               scope="playlist-modify-private",
                                               show_dialog=True,
                                               cache_path="../token.txt"))

pprint(sp.current_user())

counter = 0
tracks = []

for title in titles:
    track_list = sp.search(limit=1, q='artist:' + artists[counter] + ' track:' + titles[counter], type='track')
    counter = counter + 1
    try:
        track_uri = track_list['tracks']['items'][0]['uri']
        tracks.append(track_uri)
    except:
        continue

playlist = sp.user_playlist_create(USER_ID, 'my_new_playlist', public=False, description='')
pprint(playlist)
playlist_id = playlist['id']
playlist_uri = playlist['uri']


sp.playlist_add_items(playlist_id, tracks, position=0)
pprint(playlist)

