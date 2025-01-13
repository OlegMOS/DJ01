from django.shortcuts import render, redirect
from .models import News_post
from .forms import News_postForm

def news(request):
    news = News_post.objects.all()
    return render(request, 'DJ03/news.html', {'news': news})

def create_news(request):
    error = ""
    if request.method == 'POST':
        form = News_postForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('news')  # Перенаправление на страницу новостей после сохранения
        else:
            error = "Данные были заполнены некорректно"
    form = News_postForm()
    return render(request, 'DJ03/add_new_post.html', {'form': form, 'error': error})