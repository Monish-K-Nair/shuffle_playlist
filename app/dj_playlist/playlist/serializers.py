from rest_framework import serializers

from playlist.models import UserPlaylistSong, Playlist



class PlaylistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Playlist
        fields = '__all__'


class UserPlaylistSongSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserPlaylistSong
        fields = ['id', 'playlist', 'song', 'order']
        read_only_fields = ['order', 'id']
