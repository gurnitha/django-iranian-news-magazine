# apps/dashboard/urls.py

# Django modules
from django.urls import path

# Django locals
from apps.dashboard.views import home_page_dashboard

app_name = 'dashboard'

urlpatterns = [
    path('', home_page_dashboard, name='home_page_dashboard'),
]
