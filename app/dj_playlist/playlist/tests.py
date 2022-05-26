from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from playlist.models import Playlist, UserPlaylistSong


# class playlistAPITests(APITestCase):
#     def __init__(self) -> None:
#         self.url = reverse('songs')
#         super().__init__()

#     def test_playlist_get(self):
#         response = self.client.get(self.url)
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
    
#     def test_playlist_create(self):
#         data = {'name': 'playlist_1'}
#         response = self.client.post(self.url, data, format='json')
#         self.assertEqual(response.status_code, status.HTTP_201_CREATED)
#         self.assertEqual(Playlist.objects.count(), 1)
#         self.assertEqual(Playlist.objects.get().name, 'playlist_1')


