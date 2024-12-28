from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1>Это главная страница</h1>")
def data(request):
    return HttpResponse("<h1>Это страница Data моего проекта на Django</h1>")
def test(request):
    return HttpResponse("<h1>Это страница Test моего проекта на Django</h1>")