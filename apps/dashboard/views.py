# apps/dashboard/views.py

# Django modules
from django.shortcuts import render

# Django locals
from apps.news.models import News
# Create your views here.

# Homepage view
def dashboard(request):
	return render(request, 'dashboard/dashboard.html')


def news_list(request):
	news_lists = News.objects.all()
	print(news_lists)
	context = {
		'news_lists':news_lists
	}
	return render(request, 'dashboard/news_list.html', context)


def news_add(request):

	return render(request, 'dashboard/news_add.html')