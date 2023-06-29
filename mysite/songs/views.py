from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views import View
from django.urls import reverse_lazy
from django.shortcuts import render
from django.http import HttpResponse

from songs import spotipy_audio_features_for_track

from songs.models import Song


def react_example(request):
    return render(request, "songs/react-example.html")


def track_options_from_search(request):
    # TODO: turn into CBV
    # Sway by Callum J. Wright
    # 7pYX4pGboc1Fvwd0MinOFD
    # What Side of Love by Parachute
    # 6SwBFQFjgwdYomUy6kLTrH
    query_string = request.GET.get('search', 'Lean on Me Withers')

    matches: list = get_top_song_matches(query_string)

    first_match: dict = matches[0]
    top_two = matches[0:2]
    matches = top_two
    top_match_uri = first_match['uri']
    track_features: dict = get_track_features(top_match_uri)
    context = {
        'match': first_match,
        'img_source': first_match['album']['images'][0]['url'],
        'track_features': track_features
    }
    # TODO: give the user a button that will save their
    # favorite song analyses to the database
    # TODO: Use Dj4e owned rows to allow users to save different analyses to their account
    return render(request, 'songs/track_options_from_search.html', context)


def audio_features(request):
    # TODO: turn into CBV and make get track features a method
    # Sway by Callum J. Wright
    # 7pYX4pGboc1Fvwd0MinOFD
    # What Side of Love by Parachute
    # 6SwBFQFjgwdYomUy6kLTrH
    query_string = request.GET.get('search', '6Rskc4RUqPgmcxkQic0a5G')
    track_uri = f'spotify:track:{query_string}'
    track_features: dict = get_track_features(track_uri)
    context = {
        'track_features': track_features
    }
    # TODO: display the image
    # TODO: give the user a button that will save their
    # favorite song analyses to the database
    # TODO: Use Dj4e owned rows to allow users to save different analyses to their account
    return render(request, 'songs/audio_features.html', context)


def get_top_song_matches(track_search_term_from_user: str):
    # Example from spotipy docs;
    # results = spotify.search(q='artist:' + name, type='artist')
    # items = results['artists']['items']
    # if len(items) > 0:
    # artist = items[0]
    # print(artist['name'], artist['images'][0]['url'])
    matches = spotipy_audio_features_for_track.search(track_search_term_from_user)['tracks']['items']
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
