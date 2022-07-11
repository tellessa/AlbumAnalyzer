# shows acoustic features for tracks for the given artist

from __future__ import print_function    # (at top of module)
from spotipy.oauth2 import SpotifyClientCredentials
import json
import spotipy
import time
# import sys


client_credentials_manager = SpotifyClientCredentials()
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
sp.trace = True

# if len(sys.argv) > 1:
#     tids = sys.argv[1:]
#     print(tids)

#     start = time.time()
#     features = sp.audio_features(tids)
#     delta = time.time() - start
#     print(json.dumps(features, indent=4))
#     print("features retrieved in %.2f seconds" % (delta,))
# Fire on the Cathedral
TRACK_URI = "spotify:track:6Rskc4RUqPgmcxkQic0a5G"

if len(TRACK_URI) > 1:
    print(TRACK_URI)

    start = time.time()
    features = sp.audio_features(TRACK_URI)
    delta = time.time() - start
    print(json.dumps(features, indent=4))
    print("features retrieved in %.2f seconds" % (delta,))
