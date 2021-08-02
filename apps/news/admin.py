# apps/news/admin.py

# Django modules
from django.contrib import admin

# Django locals
from apps.news.models import News

# Register your models here.
admin.site.register(News)