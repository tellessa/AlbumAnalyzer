from django.urls import path
from . import views
from django.views.generic import TemplateView

# https://docs.djangoproject.com/en/3.0/topics/http/urls/
app_name = 'songs'
urlpatterns = [
    path('', views.MainView.as_view(), name='all'),
    path('main/create/', views.SongCreate.as_view(), name='song_create'),
    path('main/<int:pk>/update/', views.SongUpdate.as_view(), name='song_update'),
    path('main/<int:pk>/delete/', views.SongDelete.as_view(), name='song_delete'),
    path('audio_features/', views.audio_features, name='audio_features'),
    path('track_options_from_search/', views.track_options_from_search, name='audio_features'),
    path('react-example/', views.react_example)
]
