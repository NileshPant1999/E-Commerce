from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import include, url
from django.contrib import admin
from django.urls import path, include

from core.views import (
        ItemListAPIView,
        ItemRetrieveAPIView,
    )

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', include('core.urls', namespace='core')),
    path('api/v1/', include('core.urls')),
]

urlpatterns += [
    url(r'^api/categories/$', ItemListAPIView.as_view(), name='items_api'),
    url(r'^api/categories/(?P<pk>\d+)/$', ItemRetrieveAPIView.as_view(), name='items_detail_api'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
