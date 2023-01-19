from django.contrib import admin
from .models import Movie, Song

# Register your models here.


class MovieAdmin(admin.ModelAdmin):
    list = ('name', 'genre', 'starring')

    admin.site.register(Movie)


class SongAdmin(admin.ModelAdmin):
    list = ('name', 'genre', 'artist', 'album')

    admin.site.register(Song)
