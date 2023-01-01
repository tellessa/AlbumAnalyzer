import spotipy
from spotipy.oauth2 import SpotifyOAuth
from spotipy.oauth2 import SpotifyClientCredentials

# Error: HTTP Error for GET to https://api.spotify.com/v1/me/tracks with Params: {'limit': 20, 'offset': 0, 'market': None} returned 401 due to Missing token on method call current_user_saved_tracks()


def main():
    scope = "user-library-read"

    auth_manager = SpotifyClientCredentials()
    sp = spotipy.Spotify(auth_manager=auth_manager)

    results = sp.current_user_saved_tracks()
    for idx, item in enumerate(results['items']):
        track = item['track']
        print(idx, track['artists'][0]['name'], " – ", track['name'])


if __name__ == "__main__":
    main()
