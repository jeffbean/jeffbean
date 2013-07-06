# Create your views here.
from django.views.generic.base import TemplateView


class BlogHome(TemplateView):
    template_name = 'blog_home.html'
