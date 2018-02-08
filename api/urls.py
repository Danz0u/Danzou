from django.urls import path

from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path('animes/', views.AnimeList.as_view(), name='animes'),
    path('animes/ep/<int:pk>/', views.AnimeEpDetail.as_view(), name='ep-detail'),
    path('animes/category/<int:pk>/', views.AnimeCategoryDetail.as_view(), name='category-detail'),
    path('eps/', views.EpList.as_view(), name='eps'),
    path('categorys/', views.CategoryList.as_view(), name='categorys'),

]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
