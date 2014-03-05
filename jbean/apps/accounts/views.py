# coding=utf-8
from django.contrib.auth import get_user_model
from django.views.generic import DetailView


class AccountProfileView(DetailView):
    model = get_user_model()
    template_name = 'registration/profile.html'
    context_object_name = 'user'

    def get_context_data(self, **kwargs):
        context = super(AccountProfileView, self).get_context_data(**kwargs)
        return context
