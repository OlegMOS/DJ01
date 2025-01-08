from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', views.index, name='home'), path('data', views.data, name='page3'), path('test', views.test, name='page4'),
    path('blok', views.blok, name='page2')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)