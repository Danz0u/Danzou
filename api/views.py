from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

#from django_filters.rest_framework import DjangoFilterBackend

from . import serializer
from . import models


class AnimeList(generics.ListAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = serializer.AnimeSerializer
    queryset = models.Anime.objects.all().order_by('name')


class AnimeEpDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = serializer.EpSerializer
    queryset = models.Ep.objects.all()


class AnimeCategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = serializer.CategorySerializer
    queryset = models.Category.objects.all()


class EpList(generics.ListAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = serializer.EpSerializer
    queryset = models.Ep.objects.all().order_by('-created_at')


class CategoryList(generics.ListAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = serializer.CategorySerializer
    queryset = models.Category.objects.all().order_by('name')
