# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from news.views import EntryList, EntryDetail
from views import EntryList

urlpatterns = patterns('',
    url(r'^$', EntryList.as_view(), name='entry_list'),
    url(r'^(?P<pk>[\d]+)/', EntryDetail.as_view(), name='entry_detail'),
)
