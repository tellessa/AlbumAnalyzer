from django.urls import path
from . import views
from django.views.generic import TemplateView

# https://docs.djangoproject.com/en/3.0/topics/http/urls/
app_name = 'songs'
urlpatterns = [
    path('', views.MainView.as_view(), name='all'),
    path('generate_text', views.generate_text_view, name='generate_text_name'),
    path('interactive', views.interactive_python_concept, name='interactive_python_concept_name'),
    path('about', views.about, name='about_name'),

    path('playlists', views.playlists, name='playlists_name'),
    # Still works locally, is impressive and uses plotly. On PythonAnywhere it has no data to display but does show a graph.
    path('analyze/', views.analyze, name='song_analyze_name'),
    # Still works, and is probably the most impressive page. Depends on my database. Does it work in deployed version?
    path('analyze_keys/', views.analyze_keys, name='song_analyze_keys'),
    # Was yielding 403, is now functioning again to produce nice, shadowed icons, a helpful release date, Album name and artist.
    # when "add to favorites" is clicked, "/songs/add_to_favorites" is triggered.
    # path('track_options_from_search/', views.track_options_from_search, name='track_options_from_search_name'),
    # Works but is just an arbitrary ability to fill out data fields that are no longer able to be automatically filled in.
    path('main/create/', views.SongCreate.as_view(), name='song_create'),
    path('main/<int:pk>/update/', views.SongUpdate.as_view(), name='song_update'),
    path('main/<int:pk>/delete/', views.SongDelete.as_view(), name='song_delete'),
    # Not tested or developed yet
    # path('audio_features/', views.audio_features, name='track_options_from_search_name'),
    # path('react-example/', views.react_example),
    # path('add_to_favorites_cbv/', views.AddToFavorites.as_view(), name='add_to_favorites_name'),
    # fails for a Python error when calling .replace()
    # path('add_to_favorites/', views.add_to_favorites, name='song_favorite'),
    # Yields 403
    # path('album_options_from_search/', views.analyze_album_keys, name='album_options_from_search_name'),
]
