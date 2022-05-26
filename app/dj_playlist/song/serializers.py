from rest_framework import serializers

from song.models import Song, SongDetail

class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ['title']

class SongDetailSerializer(serializers.ModelSerializer):
    song = serializers.PrimaryKeyRelatedField(
        read_only=False,
        queryset=Song.objects.all()
    )

    class Meta:
        model = SongDetail
        fields = ['song', 'description', 'genre', 'duration', 'year', 'artist'] 
        # read_only_fields = ['song']
