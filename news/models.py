# -*- coding: utf-8 -*-
from django.db import models

class Feed(models.Model):

    class Meta:
        verbose_name = u'Фид'
        verbose_name_plural = u'Фиды'

    title = models.CharField(verbose_name=u'Название', max_length=255)
    link = models.URLField(verbose_name=u'Ссылка')
    description = models.CharField(verbose_name=u'Описание', max_length=255)

    def __unicode__(self):
        return self.title

class Entry(models.Model):

    class Meta:
        verbose_name = u'Пост'
        verbose_name_plural = u'Посты'

    title = models.CharField(verbose_name=u'Заголовок', max_length=255)
    link = models.URLField(verbose_name=u'Ссылка')
    picture = models.URLField(verbose_name=u'Картинка')
    summary = models.TextField(verbose_name=u'Содержимое')
    published = models.DateTimeField(verbose_name=u'Дата публикации')
    feed = models.ForeignKey('Feed', null=True)

    def __unicode__(self):
        return self.title
