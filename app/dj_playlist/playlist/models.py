from django.db import models
from django.conf import settings


class Playlist(models.Model):
    name = models.CharField(max_length=40)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ManyToManyField(settings.AUTH_USER_MODEL)

class UserPlaylistSong(models.Model):
    playlist = models.ForeignKey('playlist.Playlist', on_delete=models.CASCADE)
    song = models.ManyToManyField('song.Song')
    order = models.IntegerField(blank=True, null=True)

    def save(self, *args, **kwargs):
        self.order = UserPlaylistSong.objects.count() + 1
        super().save(*args, **kwargs)
