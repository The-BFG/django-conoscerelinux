from django.urls import path

from . import views

app_name = "members"

urlpatterns = [
    path("", views.MemberListView.as_view(), name="member-list"),
    path("<int:pk>", views.MemberDetailView.as_view(), name="member-detail"),
    path("register", views.RegistrationView.as_view(), name="register"),
]
