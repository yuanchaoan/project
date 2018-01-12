from rest_framework import serializers

from movie.models import movies, comments


class moviesserializers(serializers.ModelSerializer):
    class Meta:
        model = movies
        fields = ('title','cover','director','m_actors','type','country','date','hits',)

class commentsserializers(serializers.ModelSerializer):
    class Meta:
        model = comments
        fields = ('content','date','movie',)

