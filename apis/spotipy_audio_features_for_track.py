# shows acoustic features for tracks for the given artist

import os    # (at top of module)
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


def _get_audio_features_timed(sp, TRACK_URI):
    start = time.time()
    features: dict = _get_audio_features(sp, TRACK_URI)
    delta = time.time() - start
    print("features retrieved in %.2f seconds" % (delta,))
    return features, delta


def _get_audio_features(sp, TRACK_URI):
    features = sp.audio_features(TRACK_URI)[0]
    return features


def get_whole_album_features(sp, ALBUM_URI):
    # Get a list of URI's for the album
    # run the similar logic to single track on each one
    album_tracks = sp.album_tracks(ALBUM_URI)
    items = album_tracks["items"]
    features_by_track = []
    for item in items:
        # spotify:track:2md2i5QvelRFnafpnd6LOg
        uri = item["uri"]
        features = _get_audio_features_timed(sp, uri)[0]
        features_by_track.append(features)
        print(features)
    return features_by_track


def write_to_file(features, path):
    counter = 1  # tracks start at 1 not 0
    if not os.path.exists(path):
        os.mkdir(path)
    for entry in features:
        with open(path + f"/track {counter}.json", "w") as outfile:
            outfile.write(entry)
        counter += 1


def get_album_features():
    # get_fire_on_the_cathedral_features(sp, )
    THE_BEAUTIFUL_LETDOWN_DELUXE = "spotify:album:2mIYia4lSO1NCSFGGGGNR9"
    beautiful_letdown_features = get_whole_album_features(sp, THE_BEAUTIFUL_LETDOWN_DELUXE)
    write_to_file(beautiful_letdown_features, "switchfoot_results")


def get_fire_on_the_cathedral_features():
    # Fire on the Cathedral URI
    TRACK_URI = "spotify:track:6Rskc4RUqPgmcxkQic0a5G"
    features = _get_audio_features_timed(sp, TRACK_URI)
    return features


def get_audio_features_timed(TRACK_URI):
    return _get_audio_features_timed(sp, TRACK_URI)


def get_audio_features(TRACK_URI):
    return _get_audio_features(sp, TRACK_URI)


if __name__ == "__main__":
    get_album_features()
