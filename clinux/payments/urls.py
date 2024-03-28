from django.urls import path

from . import views

app_name = "events"

urlpatterns = [
    path("", views.EventListView.as_view(), name="payment-list"),
    path("<int:pk>", views.EventDetailView.as_view(), name="payment-detail"),
    path("sessions", views.EventSessionListView.as_view(), name="session-list"),
    path(
        "sessions/<int:pk>",
        views.EventSessionDetailView.as_view(),
        name="session-detail",
    ),
]
