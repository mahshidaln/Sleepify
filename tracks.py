import json
import urllib
import spotipy
import spotipy.util as util
from spotipy.oauth2 import SpotifyClientCredentials



""" loading client id and secret and setting up a authorized connection """

with open("config.json") as json_file:
    config = json.load(json_file)
   
cid = config["spotify_auth"]["cid"]
secret = config["spotify_auth"]["secret"]
redirect_uri = config["spotify_auth"]["redirect_uri"]
audio_dir = config["path"]["audio"]

client_credentials_manager = SpotifyClientCredentials(client_id=cid, client_secret=secret) 
token = client_credentials_manager.get_access_token()
sp = spotipy.Spotify(token)
#sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
#token = util.prompt_for_user_token(username='mahshid_aln', client_id=cid, client_secret=secret,redirect_uri=redirect_uri)

""" getting tracks of sleep playlist """

sleep_id = "spotify:playlist:37i9dQZF1DWZd79rJ6a7lp"
sleep_playlist = sp.user_playlist(user=None, playlist_id=sleep_id, fields="tracks")
sleep_size = sleep_playlist['tracks']['total']
offset_no = int(sleep_size/100)
tracks_items = []
tracks_uri = []
tracks_name = []
tracks_preview = []
tracks_addedAt = []
analysis_urls = []

for i in range(0, offset_no+1):
    tracks = sp.user_playlist_tracks(user=None, playlist_id=sleep_id, limit=100, offset=i*100)
    tracks_items.extend(tracks['items'])

for i in range(len(tracks_items)):
    tracks_name.append(tracks_items[i]['track']['name'])
    tracks_uri.append(tracks_items[i]['track']['uri'])
    tracks_preview.append(tracks_items[i]['track']['preview_url'])
    tracks_addedAt.append(tracks_items[i]['added_at'])
    analysis_urls.append(sp.audio_features(tracks_uri[i])[0]['analysis_url'])