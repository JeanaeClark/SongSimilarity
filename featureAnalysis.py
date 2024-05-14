import spotipy
from spotipy.oauth2 import SpotifyClientCredentials, SpotifyOAuth
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

cid = '0cad5195dfd04884b84ba221fe400bff'
secret = '212724fad9f6414fb40a0d2caf57f4ee'
scope = "playlist-modify-public"
client_credentials_manager = SpotifyClientCredentials(client_id=cid, client_secret=secret)
auth_manager = SpotifyOAuth(scope=scope, client_id=cid, client_secret=secret, redirect_uri="http://localhost")
sp = spotipy.Spotify(client_credentials_manager = client_credentials_manager, auth_manager=auth_manager)

sadSong = "2BOqDYLOJBiMOXShCV1neZ"
happySong = "3koCCeSaVUyrRo3N2gHrd8"

featuresSadSong = sp.audio_features(sadSong)
featuresHappySong = sp.audio_features(happySong)

# print(featuresSadSong)
print("Features for 'Let's Groove' by Earth, Wind, and Fire:\n")
data = pd.DataFrame(featuresHappySong)
print(data.T)