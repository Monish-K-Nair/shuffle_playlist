from django.shortcuts import render

from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated


from playlist.models import Playlist, UserPlaylistSong
from playlist.serializers import UserPlaylistSongSerializer, PlaylistSerializer

from utils.shuffler import ShuffleClass


class PlaylistModelViewSet(viewsets.ModelViewSet):
    queryset = Playlist.objects.all()
    serializer_class = PlaylistSerializer


class UserPlaylistSongModelViewSet(viewsets.ModelViewSet):

    serializer_class = UserPlaylistSongSerializer
    permission_classes = [IsAuthenticated]
    filter_fields = ['playlist']
    def get_queryset(self):
        return UserPlaylistSong.objects.filter(playlist__user=self.request.user).order_by('order')


class ShuffleOrderViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]

    def list(self, request):
        queryset = UserPlaylistSong.objects.filter(
            playlist__user=self.request.user)
        ShuffleClass(queryset).shuffle_order()
        return Response(status=status.HTTP_200_OK)


# class ShuffleSongsViewSet(viewsets.ViewSet):
#     permission_classes = [IsAuthenticated]

#     def list(self, request):
#         queryset = UserPlaylistSong.objects.filter(
#             playlist__user=self.request.user)
#         ShuffleClass(queryset).shuffle_songs()
#         return Response(status=status.HTTP_200_OK)
