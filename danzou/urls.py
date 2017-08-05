from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from core.views import HomeView


urlpatterns = [

    # Core
    url(r'^admin/', admin.site.urls),

    # Home
    url(r'^$', HomeView.as_view(), name='home'),

    # API Rest
    url(r'^api/', include('core.api.urls')),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
