from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def index(request):
    return render(request, 'main/index.html')
def blok(request):
    return render(request, 'main/blok.html')
def data(request):
    return render(request, 'main/data.html')
def test(request):
    return render(request, 'main/test.html')
def news (request):
    return render(request, 'DJ03/news.html')