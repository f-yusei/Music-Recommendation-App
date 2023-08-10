import pandas as pd
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import time

from dotenv import load_dotenv
import os

load_dotenv()

client_id = os.getenv('CLIENT_ID')
client_secret = os.getenv('CLIENT_SECRET')

client_credentials_manager = SpotifyClientCredentials(client_id, client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)


# プレイリストIDから曲のIDを抽出
def getTrackIDs(playlist_ids):
    track_ids = []

    for playlist_id in playlist_ids:
        playlist = sp.playlist(playlist_id)
        while playlist['tracks']['next']:
            for item in playlist['tracks']['items']:
                track = item['track']
                if not track['id'] in track_ids:
                    track_ids.append(track['id'])
            playlist['tracks'] = sp.next(playlist['tracks'])
        else:
            for item in playlist['tracks']['items']:
                track = item['track']
                if not track['id'] in track_ids:
                    track_ids.append(track['id'])
    return track_ids
# playlist_ids = ['37i9dQZEVXbKXQ4mDTEBXq?si=19fc3e3d34144845']  # 日本トップ50プレイリストのid
#track_ids = getTrackIDs(playlist_ids)
# print(len(track_ids))
# 曲の情報を取得


def getTrackFeatures(id):
    meta = sp.track(id)
    features = sp.audio_features(id)
    name = meta['name']
    album = meta['album']['name']
    artist = meta['album']['artists'][0]['name']
    danceability = features[0]['danceability']
    acousticness = features[0]['acousticness']
    energy = features[0]['energy']
    instrumentalness = features[0]['instrumentalness']
    liveness = features[0]['liveness']
    loudness = features[0]['loudness']
    valence = features[0]['valence']
    track = [name, album, artist, danceability, acousticness,
             energy, instrumentalness, liveness, loudness, valence, id]
    return track


def Output_track_data(track_ids):
    tracks = []

    for track_id in track_ids:
        time.sleep(0.03)
        track = getTrackFeatures(track_id)
        tracks.append(track)

    df = pd.DataFrame(tracks, columns=['name', 'album', 'artist', 'danceability',
                      'acousticness', 'energy', 'instrumentalness', 'liveness', 'loudness', 'valence', 'id'])
    df.to_csv('./spotify_data/spotify_music_data.csv', sep=',')
    return 0


def Get_Track_url(id):
    track_url_dict = sp.track(id[0])
    track_url = track_url_dict['external_urls']['spotify']
    return track_url


if __name__ == '__main__':
    getTrackIDs()
    getTrackFeatures()
    Output_track_data()
    Get_Track_url()
