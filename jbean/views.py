from django.views.generic.base import TemplateView

__author__ = 'Jeffrey'


class HomePage(TemplateView):
    template_name = 'home.html'