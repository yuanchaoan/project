from django.contrib.auth.models import User
from rest_framework import serializers

from movie.models import movies, comments


class moviesserializers(serializers.ModelSerializer):
    class Meta:
        model = movies
        fields = ('title','cover','director','m_actors','type','country','date','hits',)

class commentsserializers(serializers.ModelSerializer):
    class Meta:
        model = comments
        fields = ('content','date','movie','owner')

    owner = serializers.ReadOnlyField(source='owner.username')

class Userserializers(serializers.ModelSerializer):
    comments = serializers.PrimaryKeyRelatedField(many=True, queryset=comments.objects.all())
    class Meta:
        model = User
        fields = ('id', 'username', 'comments')