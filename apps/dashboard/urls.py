# apps/dashboard/urls.py

# Django modules
from django.urls import path

# Django locals
from apps.dashboard.views import dashboard, news_list

app_name = 'dashboard'

urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('news_list/', news_list, name='news_list'),
]
