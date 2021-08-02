# apps/dashboard/views.py

# Django modules
from django.shortcuts import render

# Create your views here.

# Homepage view
def dashboard(request):
	return render(request, 'dashboard/dashboard.html')

def news_list(request):
	return render(request, 'dashboard/news_list.html')