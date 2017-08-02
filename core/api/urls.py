from django.conf.urls import url
from core.api.views import AnimeList, AnimeDetail


helper_patterns = [
    url(r'^animes/$', AnimeList.as_view(), name='animes'),
    url(r'^anime/(?P<pk>[0-9]+)/$', AnimeDetail.as_view(), name='anime')
]

urlpatterns = helper_patterns
