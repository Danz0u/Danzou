from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static


from core.views import *

urlpatterns = [

    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^report/bugs', RelatedBugsView.as_view(), name='reported'),
    url(r'^thanks', ThanksView.as_view(), name='thanks'),

]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
