from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets

from movie.models import movies, comments
from movie.serializers import moviesserializers, commentsserializers


class moviesViewSet(viewsets.ModelViewSet):

    queryset = movies.objects.all()
    serializer_class = moviesserializers

class commentsViewSet(viewsets.ModelViewSet):
    queryset = comments.objects.all()
    serializer_class = commentsserializers