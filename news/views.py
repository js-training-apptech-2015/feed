# -*- coding: utf-8 -*-
from django.views.generic import ListView, DetailView
from models import Entry


class EntryList(ListView):
    model = Entry


class EntryDetail(DetailView):
    model = Entry
