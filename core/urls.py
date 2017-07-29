from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static


from core.views import *

urlpatterns = [

    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^lista-de-animes', AnimeListView.as_view(), name='anime-list'),
    url(r'^anime/(?P<slug>[\w-]+)/$',
        AnimeDetailView.as_view(), name='anime-detail'),
    url(r'^anime', AnimeSearchList.as_view(), name='search-anime'),
    url(r'^reportar/bugs', RelatedBugsView.as_view(), name='reported'),
    url(r'^obrigado', ThanksView.as_view(), name='thanks'),

]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
