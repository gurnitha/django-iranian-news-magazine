# apps/dashboard/urls.py

# Django modules
from django.urls import path

# Django locals
from apps.dashboard.views import dashboard, news_list, news_add

app_name = 'dashboard'

urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('news/list', news_list, name='news_list'),
    path('news/add', news_add, name='news_add'),
]
