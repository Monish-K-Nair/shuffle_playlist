from django.shortcuts import render

from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser

from song.models import Song, SongDetail
from song.serializers import SongSerializer, SongDetailSerializer

class SongModelViewSet(viewsets.ModelViewSet):
    permission_classes=[IsAdminUser]
    queryset = Song.objects.all()
    serializer_class = SongSerializer

class SongDetailModelViewSet(viewsets.ModelViewSet):
    permission_classes=[IsAdminUser]
    queryset = SongDetail.objects.all()
    serializer_class = SongDetailSerializer
