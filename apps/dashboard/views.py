# apps/dashboard/views.py

# Django modules
from django.shortcuts import render

# Create your views here.

# Homepage view
def home_page_dashboard(request):
	return render(request, 'dashboard/home_page_dashboard.html')