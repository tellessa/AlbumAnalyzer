# shows acoustic features for tracks for the given artist

from __future__ import print_function    # (at top of module)
from spotipy.oauth2 import SpotifyClientCredentials
import json
import spotipy
import time
import sys


client_credentials_manager = SpotifyClientCredentials()
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
sp.trace = True


def get_audio_features_with_command_line_args():
    if len(sys.argv) > 1:
        tids = sys.argv[1:]
        print(tids)

        start = time.time()
        features = sp.audio_features(tids)
        delta = time.time() - start
        print(json.dumps(features, indent=4))
        print("features retrieved in %.2f seconds" % (delta,))


def get_audio_features_timed(sp, TRACK_URI):
    start = time.time()
    features = get_audio_features(sp, TRACK_URI)
    delta = time.time() - start
    print("features retrieved in %.2f seconds" % (delta,))
    return features, delta


def get_audio_features(sp, TRACK_URI):
    features = sp.audio_features(TRACK_URI)
    features_json_string = json.dumps(features, indent=4)
    return features_json_string


def get_fire_on_the_cathedral_features(sp, get_audio_features_timed):
    # Fire on the Cathedral
    TRACK_URI = "spotify:track:6Rskc4RUqPgmcxkQic0a5G"
    features = get_audio_features_timed(sp, TRACK_URI)[0]
    print(features)


get_fire_on_the_cathedral_features(sp, get_audio_features_timed)
