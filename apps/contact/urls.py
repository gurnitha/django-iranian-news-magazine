# apps/contact/urls.py

# Django modules
from django.urls import path

# Django locals
from apps.contact.views import contact_page

app_name = 'contact'

urlpatterns = [
    path('', contact_page, name='contact_page'),
]
