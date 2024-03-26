from django.utils import timezone
from django.views.generic import DetailView
from django.views.generic.list import ListView

from . import models


class EventDetailView(DetailView):
    model = models.Event
    context_object_name = "event"


class EventSessionDetailView(DetailView):
    model = models.EventSession
    context_object_name = "session"


class EventListView(ListView):
    model = models.Event
    context_object_name = "events"
    paginate_by = 5  # if pagination is desired


class EventSessionListView(ListView):
    model = models.EventSession
    context_object_name = "sessions"
    paginate_by = 5  # if pagination is desired
