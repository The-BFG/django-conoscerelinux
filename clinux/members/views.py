from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView

from .models import Member


class MemberDetailView(DetailView):
    model = Member
    context_object_name = "member"
    template_name = "members/member.html"


class MemberListView(ListView):
    model = Member
    context_object_name = "members"

'''
class RegistrationForm(forms.Form):
    name = forms.CharField()
    surname = forms.CharField(widget=forms.Textarea)
    

    def send_email(self):
        # send email using the self.cleaned_data dictionary
        pass
'''

class RegistrationView(CreateView):
    model = Member
    template_name = "members/registration.html"
    fields = "__all__"