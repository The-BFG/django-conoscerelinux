from django.urls import path

from . import views

app_name = "events"

urlpatterns = [
    # path("", views.index, name="index"),
    path("", views.EventListView.as_view(), name="event-list"),
]
