from django.shortcuts import render
from .models import News_post

# Create your views here.

def news(request):
	news = News_post.objects.all()
	return render(request, 'DJ03/news.html', {'news': news})