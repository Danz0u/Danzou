from rest_framework import serializers
from core.models import Anime


class AnimeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Anime

        depth = 1

        fields = ['id', 'title', 'img', 'sinopse', 'file_size',
                  'duration', 'file_format', 'file_audio', 'file_subtitles', 'url', 'slug']
