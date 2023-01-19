from django.db import models

# Create your models here.


class Movie(models.Model):
    name = models.CharField(max_length=250)
    genre = models.CharField(max_length=200)
    starring = models.CharField(max_length=350)

    def __str__(self):
        return self.name


class Song(models.Model):
    name = models.CharField(max_length=250)
    genre = models.CharField(max_length=200)
    artist = models.CharField(max_length=350)
    album = models.CharField(max_length=350)
    # danceability = models.DecimalField(decimal_places=4, help_text="High danceability means you can dance to it")
    # energy = models.DecimalField(decimal_places=4, help_text="High energy means it's upbeat")
    # # TODO: utilize the "choices" kwarg for key
    # key = models.CharField(max_length=4, help_text="The musical key of a song")
    # loudness = models.DecimalField(decimal_places=4, help_text="Loudness means ?")
    # mode = models.IntegerField(help_text="Major is represented by 1 and minor by 0")
    # speechiness = models.DecimalField(decimal_places=4, help_text="Major is represented by 1 and minor by 0")
    # acousticness = models.DecimalField(decimal_places=4, help_text="Major is represented by 1 and minor by 0")
    # instrumentalness = models.DecimalField(decimal_places=4, help_text="Major is represented by 1 and minor by 0")
    # liveness = models.DecimalField(decimal_places=4, help_text="Major is represented by 1 and minor by 0")
    # valence = models.DecimalField(decimal_places=4, help_text="Major is represented by 1 and minor by 0")
    # tempo = models.DecimalField(decimal_places=4, help_text="Major is represented by 1 and minor by 0")
    # duration = models.CharField(max_length=10, help_text="Major is represented by 1 and minor by 0")
    # time_signature = models.SmallIntegerField(help_text="Major is represented by 1 and minor by 0")

    def __str__(self):
        return self.name
