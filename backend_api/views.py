from django.shortcuts import render
from .models import Movie, Song
from .serializers import MovieSerializer, SongSerializer
from rest_framework import viewsets

# Create your views here.


class MovieViewSet(viewsets.ModelViewSet):
    serializer_class = MovieSerializer
    queryset = Movie.objects.all()


class SongViewSet(viewsets.ModelViewSet):
    serializer_class = SongSerializer
    queryset = Song.objects.all()
