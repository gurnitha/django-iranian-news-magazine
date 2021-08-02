# apps/news/models.py

# Django modules
from __future__ import unicode_literals
from django.db import models

# Django locals

# Create your models here.

class News(models.Model):

    title = models.CharField(max_length=150, blank=False)
    short_txt = models.TextField()
    body_txt = models.TextField()
    date = models.CharField(max_length=12)
    pic = models.TextField()
    writer = models.CharField(max_length=50)

    class Meta:
    	verbose_name = "News"
    	verbose_name_plural = "News"

    def __str__(self):
        return self.title
  

     