from django.shortcuts import render

from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser

from django.contrib.auth.models import User

from user.serializers import UserSerializer


class UserModelViewSet(viewsets.ModelViewSet):
    permission_classes=IsAdminUser,
    queryset = User.objects.all()
    serializer_class = UserSerializer
