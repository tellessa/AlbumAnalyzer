from django.db import models
from django.core.validators import MinLengthValidator

# class Artist(models.Model):
#     name = models.CharField(
#             max_length=200,
#             validators=[MinLengthValidator(2, "Artist must be greater than 1 character")]
#     )

#     def __str__(self):
#         return self.name


class Song(models.Model):
    name = models.CharField(
        max_length=200,
        validators=[MinLengthValidator(
            2, "Name must be greater than 1 character")]
    )
    # TODO: make sure the float fields are between 0 and 1
    danceability = models.FloatField()
    energy = models.FloatField()
    key = models.CharField(max_length=3)
    loudness = models.FloatField()
    mode = models.IntegerField()
    speechiness = models.FloatField()
    acousticness = models.FloatField()
    instrumentalness = models.FloatField()
    liveness = models.FloatField()
    valence = models.FloatField()
    tempo = models.FloatField()
    spotify_id = models.CharField(max_length=25)
    uri = models.CharField(max_length=45)
    track_href = models.URLField()
    analysis_url = models.URLField()
    duration_in_ms = models.PositiveIntegerField()
    time_signature = models.PositiveIntegerField()

    def __str__(self):
        return self.name
