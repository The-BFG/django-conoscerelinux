from django.views.generic import DetailView

from .models import Member


class MemberDetailView(DetailView):
    model = Member
    context_object_name = "member"
    template_name = "members/member.html"
