"""dj_playlist URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path

from rest_framework import routers

from playlist.views import PlaylistModelViewSet, UserPlaylistSongModelViewSet, ShuffleOrderViewSet
from song.views import SongModelViewSet, SongDetailModelViewSet
from user.views import UserModelViewSet

from rest_framework_swagger.views import get_swagger_view
from rest_framework.authtoken import views


schema_view = get_swagger_view(title='DJPlaylist API')


router = routers.SimpleRouter()

router.register('songs/details', SongDetailModelViewSet, basename='song-details')
router.register('songs', SongModelViewSet, basename='songs')
router.register('playlist', PlaylistModelViewSet, basename='playlist')
router.register('user-playlist', UserPlaylistSongModelViewSet, basename='user-playlist')
router.register('shuffle/order', ShuffleOrderViewSet, basename='shuffle-order')
# router.register('shuffle/songs', ShuffleSongsViewSet, basename='shuffle-songs')
router.register('user', UserModelViewSet, basename='user')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api-token-auth/', views.obtain_auth_token, name='api-token-auth'),
    path('api/v1/', include(router.urls)),
    re_path(r'api/v1/docs', schema_view)
]

SITE_ID=1