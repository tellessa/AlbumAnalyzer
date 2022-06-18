import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from spotipy.oauth2 import SpotifyOAuth


def get_current_user_saved_tracks():
    sp = _get_spotify_using_spotify_o_auth()

    results = sp.current_user_saved_tracks()
    for idx, item in enumerate(results['items']):
        track = item['track']
        print(idx, track['artists'][0]['name'], " – ", track['name'])


def get_all_user_playlists():
    sp = _get_spotify_using_client_credentials()
    playlists = sp.user_playlists('spotify')
    while playlists:
        for i, playlist in enumerate(playlists['items']):
            print("%4d %s %s" % (i + 1 + playlists['offset'], playlist['uri'],  playlist['name']))
        if playlists['next']:
            playlists = sp.next(playlists)
        else:
            playlists = None

# Here’s another example showing how to get 30 second samples and cover art for the top 10 tracks for Relient K:
    relient_k_uri = 'spotify:artist:3nJWBJvK7uGvfp4iZh9CkN'

    spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())
    results = spotify.artist_top_tracks(relient_k_uri)

    for track in results['tracks'][:10]:
        print('track    : ' + track['name'])
        print('audio    : ' + track['preview_url'])
        print('cover art: ' + track['album']['images'][0]['url'])
        print()


def _get_spotify_using_client_credentials():
    auth_manager = SpotifyClientCredentials()
    sp = spotipy.Spotify(auth_manager=auth_manager)
    return sp


def _get_spotify_using_spotify_o_auth():
    scope = "user-library-read"
    auth_manager = SpotifyOAuth(scope=scope)
    sp = spotipy.Spotify(auth_manager=auth_manager)
    return sp


if __name__ == "__main__":
    # get_all_user_playlists()
    get_current_user_saved_tracks()
