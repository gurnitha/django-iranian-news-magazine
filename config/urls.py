# config/urls.py

# Django modules
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include



urlpatterns = [
    
    # Main app
    path('', include('apps.main.urls', namespace='main')),
    
    # About app
    path('about/', include('apps.about.urls', namespace='about')),
    
    # Contact app
    path('contact/', include('apps.contact.urls', namespace='contact')),
    
    # Admin app
    path('dashboard/', include('apps.dashboard.urls', namespace='dashboard')),

    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

