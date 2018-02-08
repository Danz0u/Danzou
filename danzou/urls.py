from django.contrib import admin

from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

from django.views import generic


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('api-auth/', include('rest_framework.urls'), name='api_auth'),
    path('', generic.TemplateView.as_view(template_name='base.html')),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
