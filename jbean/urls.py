from django.conf.urls import patterns, include, url

from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from jbean.views import HomePage

admin.autodiscover()
from jbean import settings

urlpatterns = patterns(
    '',
    # Examples:
    url(r'^$', HomePage.as_view(), name='home'),
    url(r'^blog/', include('jbean.apps.blog.urls')),
    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^accounts/', include('jbean.apps.accounts.urls')),

    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

)

urlpatterns += staticfiles_urlpatterns()

if settings.DEBUG:
    urlpatterns += patterns(
        '',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT, }),
    )


