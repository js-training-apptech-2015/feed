# -*- coding: utf-8 -*-
from django.views.generic import ListView, DetailView
from models import Entry, Feed


class EntryList(ListView):
    model = Entry

    def get_queryset(self):
        return super(EntryList, self).get_queryset().order_by('published')

class FeedList(ListView):
    model = Entry
    template_name = 'entry_feed_list.html'

    def get_queryset(self):
        return super(FeedList, self).get_queryset().filter(feed=self.kwargs['feed'])

    def get_context_data(self, **kwargs):
        context = super(FeedList, self).get_context_data(**kwargs)
        context['feed'] = Feed.objects.get(id=self.kwargs['feed'])
        return context

class EntryDetail(DetailView):
    model = Entry
