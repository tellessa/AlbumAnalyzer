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

KEYS = ["C", "C#/D♭", "D", "D#/E♭", "E", "F",
        "F#/G♭", "G", "G#/A♭", "A", "A#/B♭", "B"]


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


def _search(sp, q, type=None):
    """Returns a dict where the keys are various nouns involved in music (e.g. tracks, albums, etc).
    The values are dicts. For a track
    {
        "href": str,
        "items": list[dict],
        "limit": int,
        "next": str,
        "offset": int,
        "previous": Union[None, str],
        "total": int
    }
    ***items in detail:
        {
            album: ...,
            artists: ...,
            available markets: ...,
            disc_number: int,
            duration_ms: int,
            "explicit": bool,
            "external_ids: dict,
            external_urls: dict,
            href: str,
            id: str,
            "is_local": bool,
            "name": str,
            "popularity": int,
            "preview_url": str,
            "track_number": int,
            "type": "track",
            "uri": str
        }
    """
    """Using this data structure, we can figure out how
    to show our app's users the names and artists of the n (10+) tracks that best match their search"""
    """In the tracks dict, I care most about the items key."""
    result: dict

    if type is None:
        fields_of_interest = sp.search(q)
    elif type == "track":
        fields_of_interest = {}
        # parse track results
        result = sp.search(q, type=type)
        track: dict
        track_items: list = result["tracks"]["items"]
        # hardcode to only return one for now
        # for track in track_items[0]:
        track = track_items[0]
        track_artists = track["artists"]
        combined_artists_name: str = track_artists[0]["name"]
        # add a comma and space before additional artists
        for artist in track_artists[1:]:
            artist_name = artist["name"]
            combined_artists_name += f", {artist_name}"
        track_name: str = track["name"]
        track_uri: str = track["uri"]
        track_id: str = track["id"]
        album_art_url: str = track["album"]["images"][0]["url"]
        track_url = track["external_urls"]["spotify"]
        track_preview_url = track["preview_url"]
        track_popularity = track["popularity"]

        fields_of_interest["name"] = track_name
        fields_of_interest["artists"] = combined_artists_name
        fields_of_interest["album art url"] = album_art_url
        fields_of_interest["uri"] = track_uri
        fields_of_interest["id"] = track_id
        fields_of_interest["url"] = track_url
        # begins playing on opening
        fields_of_interest["preview url"] = track_preview_url
        fields_of_interest["popularity"] = track_popularity

    else:
        fields_of_interest = sp.search(q, type=type)
    return fields_of_interest


def _get_audio_features(sp, TRACK_URI):
    features = sp.audio_features(TRACK_URI)[0]
    # Use the key as an index to pitches, zero-indexed
    features["key"] = KEYS[features["key"]]
    features["duration_formatted"] = _format_duration(features["duration_ms"])
    return features


def _format_duration(duration_ms):
    duration_s = int(duration_ms / 1000)
    minutes = duration_s // 60
    seconds_leftover = duration_s % 60
    if seconds_leftover < 10:
        formatted_duration = f"{minutes}:0{seconds_leftover}"
    else:
        formatted_duration = f"{minutes}:{seconds_leftover}"
    return formatted_duration
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
    beautiful_letdown_features = get_whole_album_features(
        sp, THE_BEAUTIFUL_LETDOWN_DELUXE)
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


def search(q, type=None):
    return _search(sp, q, type=type)


def get_available_devices(sp):
    """returns a 404 for invalid user"""
    devices = sp.devices()
    print(devices)


if __name__ == "__main__":
    # get_album_features()
    # search_results = _search(sp, "Have Yourself A Merry Little Christmas")
    search_results = _search(sp, "Tim McGraw", type="track")
    # available_devices = get_available_devices(sp)
