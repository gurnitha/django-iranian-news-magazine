# apps/contact/views.py

# Django modules
from django.shortcuts import render

# Create your views here.

# Homepage view
def contact_page(request):
	return render(request, 'contact/contact_page.html')