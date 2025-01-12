from django.contrib.admin.templatetags.admin_list import admin_actions
from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class News_post(models.Model):
    title = models.CharField('Название новости', max_length=50)
    short_description = models.CharField('Краткое описание новости', max_length=200)
    text = models.TextField('Новость')
    pub_date = models.DateTimeField('Дата публикации', auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор')

    def __str__(self):  # Исправлено название метода
        return self.title

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'