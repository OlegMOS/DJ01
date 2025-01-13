from .models import News_post
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea, Select
from django.contrib.auth.models import User
from django import forms

class News_postForm(ModelForm):
    class Meta:
        model = News_post
        fields = ['title', 'short_description', 'text', 'author']
        widgets = {
            'title': TextInput(attrs={'class': 'form-control', 'placeholder': 'Название фильма'}),
            'short_description': TextInput(attrs={'class': 'form-control', 'placeholder': 'Описание фильма'}),
            'text': Textarea(attrs={'class': 'form-control', 'placeholder': 'Рецензия на фильм'}),
            'author': Select(attrs={'class': 'form-control'})  # Используем Select для выбора автора
            # Не добавляем pub_date, так как оно не редактируемое
        }