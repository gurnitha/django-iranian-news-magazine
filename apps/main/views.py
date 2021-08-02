# apps/main/views.py

# Django modules
from django.shortcuts import render

# Django locals
from apps.news.models import News

# Create your views here.

# Homepage view
def home_page(request):
	news_lists = News.objects.all()
	context = {
		'news_lists':news_lists
	}
	return render(request, 'main/home_page.html', context)