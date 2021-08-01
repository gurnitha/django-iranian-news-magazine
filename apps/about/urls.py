# apps/about/urls.py

# Django modules
from django.urls import path

# Django locals
from apps.about.views import about_page

app_name = 'about'

urlpatterns = [
    path('', about_page, name='about_page'),
]
