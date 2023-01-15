from django.db import models

# Create your models here.


class Movie(models.Model):
    name = models.CharField(max_length=250)
    genre = models.CharField(max_length=200)
    starring = models.CharField(max_length=350)

    def __str__(self):
        return self.name
