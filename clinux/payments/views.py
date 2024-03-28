from django.views.generic import DetailView, ListView

from .models import Member


class MemberDetailView(DetailView):
    model = Member
    context_object_name = "member"
    template_name = "members/member.html"


class MemberListView(ListView):
    model = Member
    context_object_name = "members"
