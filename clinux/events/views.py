from django.shortcuts import render
from django.utils import timezone
from django.views.generic.list import ListView

from . import models

# Create your views here.


class EventListView(ListView):
    model = models.Event
    paginate_by = 5  # if pagination is desired

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["now"] = timezone.now()
        return context


class EventSessionListView(ListView):
    model = models.EventSession
    paginate_by = 5  # if pagination is desired

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["now"] = timezone.now()
        return context
