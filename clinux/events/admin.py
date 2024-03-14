from django.contrib import admin

from .models import Event, EventSession


@admin.register(EventSession)
class EventSessionAdmin(admin.ModelAdmin):
    list_display = ["event", "start", "end"]


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ["slug", "title", "subtitle", "description"]
