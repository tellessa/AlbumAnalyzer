from django.urls import path
from . import views
from django.views.generic import TemplateView

# https://docs.djangoproject.com/en/3.0/topics/http/urls/
app_name = 'songs'
urlpatterns = [
    path('', views.MainView.as_view(), name='all'),
    path('add_to_favorites/', views.add_to_favorites, name='song_favorite'),
    path('analyze/', views.analyze, name='song_analyze_name'),
    path('analyze_keys/', views.analyze_keys, name='song_analyze_keys'),
    path('main/create/', views.SongCreate.as_view(), name='song_create'),
    path('main/<int:pk>/update/', views.SongUpdate.as_view(), name='song_update'),
    path('main/<int:pk>/delete/', views.SongDelete.as_view(), name='song_delete'),
    path('track_options_from_search/', views.track_options_from_search, name='track_options_from_search_name'),
    path('album_options_from_search/', views.analyze_album_keys, name='album_options_from_search_name'),
    # Not tested or developed yet
    # path('audio_features/', views.audio_features, name='track_options_from_search_name'),
    # path('react-example/', views.react_example),
    # path('add_to_favorites_cbv/', views.AddToFavorites.as_view(), name='add_to_favorites_name'),
]
