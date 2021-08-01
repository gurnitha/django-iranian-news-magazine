# apps/about/views.py

# Django modules
from django.shortcuts import render

# Create your views here.

# Homepage view
def about_page(request):
	return render(request, 'about/about_page.html')