import json
from django.contrib.auth.mixins import LoginRequiredMixin
# Using the built-in generics
# https://docs.djangoproject.com/en/4.2/topics/class-based-views/generic-display/
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views import View
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, JsonResponse
# from django.http import HttpResponse, HttpResponseRedirect, JsonResponse

import google.genai as genai
from google.api_core.exceptions import (
    GoogleAPIError, # Base class for most Google API errors
    InternalServerError,
    InvalidArgument,
    PermissionDenied,
    ResourceExhausted, # This is often for rate limits
)

from songs import spotipy_audio_features_for_track

from songs.models import Song

from plotly.offline import plot
import plotly.graph_objects as graphs

from songs.spotipy_audio_features_for_track import sp

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials


def react_example(request):
    return render(request, "songs/react-example.html")


def analyze_album_keys(request):
    query_string = request.GET.get('search', 'The Beautiful Letdown Switchfoot')

    matches: list = get_top_album_matches(query_string)
    # matches = matches[0:5]
    match: dict = matches[0]
    album_art_link = match["images"][0]["url"]
    artists = match["artists"]
    name = match["name"]

    match_uri = match['uri']
    artist_title = ", ".join([artist["name"] for artist in artists])
    tracks = sp.album_tracks(match_uri)["items"]
    song_names: list = [track["name"] for track in tracks]
    album_track_features: list = [get_track_features(track['uri']) for track in tracks]


    keys_plot_html = make_keys_plot(song_names, album_track_features)
    plots = [keys_plot_html]
    normed_features = [
        'danceability',
        'energy',
        # These 2 don't get y axis labels for some reason
        # 'speechiness',
        # 'liveness',
        'acousticness',
        'instrumentalness',
        'valence']
    for feature in normed_features:
        plot_html = make_normalized_plot(song_names, album_track_features, feature)
        plots.append(plot_html)

    context = {
        'plots': plots,
        'album_and_artist': f"{name} by {artist_title}",
        'search': query_string,
        'album_art_link': album_art_link,
    }
    return render(request, 'songs/analyze_keys_full_album.html', context)


def make_keys_plot(song_names, album_track_features):
    keys: list = [feature_set["key"] for feature_set in album_track_features]
    # Set the value for song danceability on Y-Axis
    # A list of alphabetical representations of musical keys, starting at C and ending at B.
    # I want my y axis to appear in this order
    possible_keys = spotipy_audio_features_for_track.KEYS
    y_axis_ticks = [possible_keys.index(key) for key in keys]

    # Create the scatter plot
    fig = graphs.Figure(data=graphs.Scatter(
    x=song_names,
    y=y_axis_ticks,  # Map keys to their indices in possible_keys
    # mode='markers',
    marker=dict(
        size=15,
        color='blue',
        symbol='circle'
    )
    ))

    # Customize the layout
    fig.update_layout(
    xaxis_title="Song Name",
    yaxis_title="Key",
    yaxis=dict(
        tickvals=list(range(len(possible_keys))),
        ticktext=possible_keys,
    ),
    font=dict(
        family="Arial",
        size=12
    )
    )

    # Generate a scatter plot HTML
    plot_html = plot(fig, output_type='div')
    return plot_html


def make_normalized_plot(song_names, album_track_features, feature):
    danceability_scores: list = [feature_set[feature] for feature_set in album_track_features]

    # Set the value for song danceability on Y-Axis
    # I want my y axis to appear in this order

    y_axis_ticks = [0, 0.2, 0.4, 0.6, 0.8, 1.0]

    # Create the scatter plot
    fig = graphs.Figure(data=graphs.Scatter(
    x=song_names,
    y=danceability_scores,  # Map keys to their indices in possible_keys
    # mode='markers',
    marker=dict(
        size=15,
        color='blue',
        symbol='circle'
    )
    ))

    # Customize the layout
    fig.update_layout(
    xaxis_title="Song Name",
    yaxis_title=feature.title(),
    yaxis=dict(
        tickvals=y_axis_ticks,
        ticktext=y_axis_ticks,
    ),
    font=dict(
        family="Arial",
        size=12
    )
    )

    # Generate a scatter plot HTML
    plot_html = plot(fig, output_type='div')
    return plot_html


def album_options_from_search(request):
    context = {}
    return render(request, 'songs/album_search_results.html', context)

def track_options_from_search(request):
    query_string = request.GET.get('search', 'Lean on Me Withers')
    matches: list = get_top_song_matches(query_string)
    matches = matches[0:5]
    # One option: add more info to this dictionary

    context = {
        # "matches": match_tuples,
        "matches": matches,
    }
    # TODO: Use Dj4e owned rows to allow users to save different analyses to their account
    # return render(request, 'songs/track_options_from_search.html', context)
    return render(request, 'songs/track_options_from_search.html', context)


def audio_features(request):

    query_string = request.GET.get('search', '6Rskc4RUqPgmcxkQic0a5G')
    track_uri = f'spotify:track:{query_string}'
    track_features: dict = get_track_features(track_uri)
    context = {
        'track_features': track_features
    }
    # TODO: Use Dj4e owned rows to allow users to save different analyses to their account
    return render(request, 'songs/audio_features.html', context)


def get_top_song_matches(track_search_term_from_user: str):
    # Example from spotipy docs;
    # results = spotify.search(q='artist:' + name, type='artist')
    # items = results['artists']['items']
    # if len(items) > 0:
    # artist = items[0]
    # print(artist['name'], artist['images'][0]['url'])
    # Here we limit it to the tracks that were returned by the query
    matches = spotipy_audio_features_for_track.search(track_search_term_from_user)['tracks']['items']
    return matches


def get_top_album_matches(track_search_term_from_user: str):
    # Example from spotipy docs;
    # results = spotify.search(q='artist:' + name, type='artist')
    # items = results['artists']['items']
    # if len(items) > 0:
    # artist = items[0]
    # print(artist['name'], artist['images'][0]['url'])
    # Here we limit it to the tracks that were returned by the query
    matches = spotipy_audio_features_for_track.search(track_search_term_from_user, type="album")["albums"]["items"]
    return matches


def get_track_features(track_uri: str):
    features = spotipy_audio_features_for_track.get_audio_features(track_uri)
    return features


class MainView(LoginRequiredMixin, View):
    def get(self, request):
        song_list = Song.objects.all()

        ctx = {'song_list': song_list}
        return render(request, 'songs/song_list.html', ctx)


class SongCreate(LoginRequiredMixin, CreateView):
    model = Song
    fields = '__all__'
    success_url = reverse_lazy('songs:all')


class SongUpdate(LoginRequiredMixin, UpdateView):
    model = Song
    fields = '__all__'
    success_url = reverse_lazy('songs:all')


class SongDelete(LoginRequiredMixin, DeleteView):
    model = Song
    fields = '__all__'
    success_url = reverse_lazy('songs:all')


class SongListView(generic.ListView):
    model = Song


def add_to_favorites(request, *args, **kwargs):
    """This is working to accept data from the previous request and to create new song objects in the db!
    What a journey it's been trying to figure that out!"""
    # Access data from the request.POST dictionary
    # Create the song object
    song_to_save = Song.objects.create(
        name=request.POST.get('name').replace("_", " "),
        danceability=request.POST.get("danceability", 0),
        energy=request.POST.get("energy", 0),
        key=request.POST.get("key", "N/A"),
        loudness= request.POST.get("loudness", 0),
        mode=request.POST.get("mode", 0),
        speechiness=request.POST.get("speechiness", 0),
        acousticness=request.POST.get("acousticness", 0),
        instrumentalness=request.POST.get("instrumentalness", 0),
        liveness=request.POST.get("liveness", 0),
        valence= request.POST.get("valence", 0),
        tempo=request.POST.get("tempo", 0),
        spotify_id=request.POST.get("id", 0),
        uri=request.POST.get("uri", "example.com"),
        track_href=request.POST.get("track_href", "N/A"),
        analysis_url=request.POST.get("analysis_url", "N/A"),
        duration_in_ms=request.POST.get("duration_ms", "N/A"),
        time_signature=request.POST.get("time_signature", "N/A")
        # TODO: consider including popularity
    )
    song_to_save.save()

    return HttpResponseRedirect(reverse_lazy('songs:all'))


# @csrf_exempt
def generate_text_view(request):
    if request.method == 'POST':
        try:
            prompt = request.POST.get('prompt')

            if not prompt:
                return JsonResponse({"error": "No prompt provided"}, status=400)

            client = genai.Client()
            response = client.models.generate_content(
                model='gemini-1.5-flash', # Or 'gemini-1.5-pro', etc.
                contents=prompt
            )

            generated_text = response.text
            context = {"generated_text": generated_text}
            return render(request, 'songs/generate_text.html', context)

        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON"}, status=400)
        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON in request body."}, status=400)
        except ResourceExhausted as e: # Catch rate limit errors specifically
            return JsonResponse({"error": f"Gemini API Rate Limit Exceeded: {str(e)}. Please try again later."}, status=429)
        except PermissionDenied as e: # Catch API key or permission issues
            return JsonResponse({"error": f"Gemini API Permission Denied: {str(e)}. Check your API key and project settings."}, status=403)
        except InvalidArgument as e: # Catch malformed requests or invalid parameters
            return JsonResponse({"error": f"Gemini API Invalid Argument: {str(e)}. Check your prompt or model configuration."}, status=400)
        except InternalServerError as e: # Catch server-side errors on Google's end
            return JsonResponse({"error": f"Gemini API Internal Server Error: {str(e)}. Google's servers might be experiencing issues."}, status=500)
        except (GoogleAPIError, Exception) as e: # Catch any other API errors or general exceptions
            return JsonResponse({"error": f"An unexpected error occurred with the Gemini API: {str(e)}"}, status=500)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)
    return render(request, 'songs/generate_text.html') # Or whatever your template is

def interactive_python_concept(request):
    result = None
    num1 = None
    num2 = None
    error_message = None
    context = {
        'num1': num1,
        'num2': num2,
        'result': result,
        'error_message': error_message,
    }

    if request.method == 'POST':
        try:
            num1_str = request.POST.get('num1')
            num2_str = request.POST.get('num2')

            num1 = float(num1_str)
            num2 = float(num2_str)

            result = num1 + num2
            context['num1'] = num1
            context['num2'] = num2
            context['result'] = result

        except (ValueError, TypeError):
            error_message = "Please enter valid numbers for both fields."
            # Update context with error message (and potentially keep original nums if they were partially valid)
            context['error_message'] = error_message
            # It's good practice to also put back the string versions for num1/num2
            # so the user doesn't lose their potentially invalid input
            context['num1'] = num1_str
            context['num2'] = num2_str
        except Exception as e: # Catch any other unexpected errors
            error_message = f"An unexpected error occurred: {e}"
            context['error_message'] = error_message
            # Keep original strings for user
            context['num1'] = num1_str
            context['num2'] = num2_str

    return render(
        request,
        'songs/interactive.html',
        context
    )
def about(request):
    dynamic_data = "abc"

    return render(request, 'songs/about.html', {'dynamic_data': dynamic_data})

def playlists(request):
    auth_manager = SpotifyClientCredentials()
    sp = spotipy.Spotify(auth_manager=auth_manager)

    playlists = sp.user_playlists('spotify')
    playlists_string = ""
    while playlists:
        for i, playlist in enumerate(playlists['items']):
            print(f"{i + 1 + playlists['offset']:4d} {playlist['uri']} {playlist['name']}")
            playlists_string += f"\n{i + 1 + playlists['offset']:4d} {playlist['uri']} {playlist['name']}"
        if playlists['next']:
            playlists = sp.next(playlists)
        else:
            playlists = None

    return render(request, 'songs/playlists.html', {'playlists_string': playlists_string})

def analyze(request):
    songs = Song.objects.all()
    song_titles = [song.name for song in songs]
    danceability_list = [0 for _ in range(len(songs))]
    # Set the value for song danceability on Y-Axis
    for idx, song in enumerate(songs):
        danceability_list[idx] = song.danceability
    scatter = graphs.Scatter(x=song_titles, y=danceability_list)
    # Generate a scatter plot HTML
    figure = graphs.Figure()
    figure.add_trace(scatter)
    figure.update_layout(xaxis_title="Song", yaxis_title="Danceability")

    plot_html = plot(figure, output_type='div')

    return render(request, 'songs/analyze.html', {'danceability_list_plot': plot_html})


def analyze_keys(request):
    songs = Song.objects.all()
    song_names = [song.name for song in songs]
    keys = []
    # Set the value for song danceability on Y-Axis
    for idx, song in enumerate(songs):
        keys.append(song.key)

    # A list of alphabetical representations of musical keys, starting at C and ending at B.
    # I want my y axis to appear in this order
    possible_keys = spotipy_audio_features_for_track.KEYS

    # features["key"] = KEYS[features["key"]]

    y_axis_ticks = [possible_keys.index(key) for key in keys]

    # Create the scatter plot
    fig = graphs.Figure(data=graphs.Scatter(
    x=song_names,
    y=y_axis_ticks,  # Map keys to their indices in possible_keys
    # mode='markers',
    marker=dict(
        size=15,
        color='blue',
        symbol='circle'
    )
    ))

    # Customize the layout
    fig.update_layout(
    title="Musical Keys of My Songs",
    xaxis_title="Song Name",
    yaxis_title="Key",
    yaxis=dict(
        tickvals=list(range(len(possible_keys))),
        ticktext=possible_keys,
    ),
    font=dict(
        family="Arial",
        size=12
    )
    )

    # Generate a scatter plot HTML
    plot_html = plot(fig, output_type='div')

    return render(request, 'songs/analyze_keys.html', {'danceability_list_plot': plot_html})


class AddToFavorites(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        # new_song = Song(1, "song", 0.0, 0.0, "a", 0.0, 1, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 120.0, "abc",
        #                 "https://www.url.com", "https://www.analysis.com", 300000, 3)
        if args:
            artist = args[0]
        new_song = Song(3, "song3", 0.0, 0.0, "a", 0.0, 1, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 120.0, "abc",
                        "https://www.url.com", "https://www.analysis.com", 300000, 3)
        songs = Song.objects.all()
        new_song.save()
        return HttpResponseRedirect(reverse_lazy('songs:all'))

    def post(self, request, *args, **kwargs):
        # new_song = Song()
        # new_song.save()
        # return HttpResponseRedirect(reverse_lazy('songs:all'))
        if args:
            artist = args[0]
        new_song = Song(3, "song3", 0.0, 0.0, "a", 0.0, 1, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 120.0, "abc",
                        "https://www.url.com", "https://www.analysis.com", 300000, 3)
        songs = Song.objects.all()
        new_song.save()
        return HttpResponseRedirect(reverse_lazy('songs:all'))
