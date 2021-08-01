# apps/main/views.py

# Django modules
from django.shortcuts import render

# Create your views here.

# Homepage view
def home_page(request):
	return render(request, 'main/home_page.html')