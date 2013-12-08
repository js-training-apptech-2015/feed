# -*- coding: utf-8 -*-
from django.db import models


class Entry(models.Model):
    title = models.CharField(verbose_name=u'Заголовок', max_length=255)
    link = models.URLField(verbose_name=u'Ссылка')
    picture = models.URLField(verbose_name=u'Картинка')
    summary = models.TextField(verbose_name=u'Содержимое')
    published = models.DateTimeField(verbose_name=u'Дата публикации')
