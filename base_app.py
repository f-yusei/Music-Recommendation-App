import pandas as pd
import spotipy
import webbrowser
import time
from transformers import pipeline, AutoModelForSequenceClassification, BertJapaneseTokenizer
from mlask import MLAsk
from spotipy.oauth2 import SpotifyClientCredentials
import re

# 自作のモジュール
import get_spotify_data
import judge_emotional
import emotional_MLAsk
import Open_track_url

# idのデフォルトは37i9dQZEVXbKXQ4mDTEBXq?si=7a1f8a1ad31e4a5e
input_playlist_id = input('好きなプレイリストのidを入力してください:')
playlist_id = [input_playlist_id]
# プレイリストに入っている曲のid
track_ids = get_spotify_data.getTrackIDs(playlist_id)
# 曲の情報をcsvで出力
get_spotify_data.Output_track_data(track_ids)
# 今の感情を入力
emotional_text = input('今の感情を書いてください:')
Current_Emotions = [emotional_text]
# ネガポジ分析
judged_score = judge_emotional.judge_emotion(Current_Emotions)

# 感情分析
Current_Emotion = emotional_MLAsk.Judge_emotion(Current_Emotions)

# 曲の情報をDataFrame型で読み込む
song_df = pd.read_csv(
    './spotify_data/spotify_music_data.csv', encoding='utf-8')

# 感情にあった曲を選出
df_track_id = []

if judged_score[0] == 'ポジティブ' and Current_Emotion == 'ポジティブな激しさ':
    # 条件に合う曲を抽出
    df = song_df[(song_df["danceability"] < judged_score[1] + 0.1) &
                 (song_df["danceability"] > judged_score[1] - 0.2)]
    df_random = df.sample()
    # 曲のurlを取得して開く
    df_track_id.append(df_random.iloc[0, 11])
    url = get_spotify_data.Get_Track_url(df_track_id)
    Open_track_url.trans_word(url)

elif judged_score[0] == 'ポジティブ' and Current_Emotion == 'ポジティブな落ち着き':
    # 条件に合う曲を抽出
    df = song_df[(song_df["energy"] < judged_score[1] + 0.3) &
                 (song_df["energy"] > judged_score[1] - 0.3)]
    df_random = df.sample()
    # 曲のurlを取得して開く
    df_track_id.append(df_random.iloc[0, 11])
    url = get_spotify_data.Get_Track_url(df_track_id)
    Open_track_url.trans_word(url)

elif judged_score[0] == 'ネガティブ' and Current_Emotion == 'ネガティブな激しさ':
    # 条件に合う曲を抽出
    df = song_df[(song_df["energy"] < 1.0) & (
        song_df["energy"] > judged_score[1] + 0.8)]
    df_random = df.sample()
    # 曲のurlを取得して開く
    df_track_id.append(df_random.iloc[0, 11])
    url = get_spotify_data.Get_Track_url(df_track_id)
    Open_track_url.trans_word(url)

elif judged_score[0] == 'ネガティブ' and Current_Emotion == 'ネガティブな落ち着き':
    # 条件に合う曲を抽出
    df = song_df[(song_df["energy"] < judged_score[1] + 0.4) &
                 (song_df["energy"] > judged_score[1] - 0.2)]
    df_random = df.sample()
    # 曲のurlを取得して開く
    df_track_id.append(df_random.iloc[0, 11])
    url = get_spotify_data.Get_Track_url(df_track_id)
    Open_track_url.trans_word(url)
else:
    print("文章の分析に失敗しました。感情表現がある文章を再度入力してください。")
