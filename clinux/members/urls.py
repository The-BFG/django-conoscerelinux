from django.urls import path

from . import views

app_name = "members"

urlpatterns = [
    path("<int:pk>", views.MemberDetailView.as_view(), name="members"),
]
