from pyexpat import model
from django.db import models


class Song(models.Model):
    title = models.CharField(max_length=20, null=False, blank=False)

class SongDetail(models.Model):
    song = models.ForeignKey('song.Song', on_delete=models.CASCADE)
    description = models.CharField(max_length=20, blank=True, null=True)
    genre = models.CharField(max_length=30, blank=True, null=True)
    duration = models.CharField(max_length=10, blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)
    artist = models.CharField(max_length=100, blank=True, null=True)
