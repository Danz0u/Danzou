from rest_framework import generics

from core.models import Anime
from core.api.serializer import AnimeSerializer


class AnimeList(generics.ListCreateAPIView):
    queryset = Anime.objects.all()
    serializer_class = AnimeSerializer


class AnimeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Anime.objects.all()
    serializer_class = AnimeSerializer
