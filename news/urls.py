# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from news.views import EntryList, EntryDetail, FeedList

urlpatterns = patterns('',
    url(r'^$', EntryList.as_view(), name='entry_list'),
    url(r'^feed/(?P<feed>[\d]+)/$', FeedList.as_view(), name='entry_feed_list'),
    url(r'^(?P<pk>[\d]+)/', EntryDetail.as_view(), name='entry_detail'),
)
