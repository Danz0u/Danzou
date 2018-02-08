from rest_framework import serializers

from . import models


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Category

        fields = ('__all__')


class AnimeSerializer(serializers.ModelSerializer):

    ep = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='ep-detail'
    )

    category = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='category-detail'
    )

    class Meta:
        model = models.Anime

        fields = [
            'id', 'name', 'category', 'ep', 'sinopse',
            'card_img_url', 'slug', 'created_at', 'updated_at'
        ]


class EpSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Ep

        fields = ('__all__')
