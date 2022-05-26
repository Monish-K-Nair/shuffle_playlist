
from playlist.models import UserPlaylistSong
import numpy as np

class ShuffleClass:
    def __init__(self, qs) -> None:
        self.queryset = qs

    def shuffle_order(self):
        self.shuffle('order')

    # def shuffle_songs(self):
    #     self.shuffle('song')

    def shuffle(self, order):
        array = list(self.queryset.values_list(order, flat=True))
        np.random.shuffle(array)
        for index, playlist in enumerate(self.queryset):
            playlist.order = array[index]
        UserPlaylistSong.objects.bulk_update(self.queryset, fields=[order])
