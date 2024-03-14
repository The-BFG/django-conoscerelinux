from django.utils import timezone
from django.shortcuts import render
from events.models import Event
from django.db.models import Max


def index(request):
    events = Event.objects.annotate(start=Max("sessions__start")).filter(start__gte=timezone.now())
    context = {
        'message': 'World!',
        'object_list': events
    }
    return render(request, "index.html", context)
