from jbean.apps.blog.views import BlogHome

__author__ = 'Jeffrey'
from django.conf.urls import url, patterns
urlpatterns = patterns(
    'jbean.apps.blog.views',
    url(r'^$', BlogHome.as_view(), name='blog-home'),

)
