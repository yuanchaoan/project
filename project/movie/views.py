from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets

from rest_framework import permissions
from movie.models import movies, comments
from movie.permissions import IsOwnerOrReadOnly,IsAdminOrReadOnly
from movie.serializers import moviesserializers, commentsserializers


class moviesViewSet(viewsets.ModelViewSet):
    queryset = movies.objects.all()
    serializer_class = moviesserializers
    permission_classes = (IsAdminOrReadOnly,)

class commentsViewSet(viewsets.ModelViewSet):
    queryset = comments.objects.all()
    serializer_class = commentsserializers
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)