from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from .main_app import *
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('api/v1/', include('rest_1.urls')),
    path('api/temp/', include('rest_1.urls')),
]

urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
