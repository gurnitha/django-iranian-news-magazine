# config/urls.py

# Django modules
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include



urlpatterns = [
    path('', include('apps.main.urls', namespace='main')),
    path('about/', include('apps.about.urls', namespace='about')),
    path('contact/', include('apps.contact.urls', namespace='contact')),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

