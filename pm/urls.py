from django.conf.urls import patterns, include, url
import forms_builder.forms.urls
from django.contrib.admin import site
import adminactions.actions as actions

# register all adminactions
actions.add_to_site(site)
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'pm.views.home', name='home'),
    # url(r'^pm/', include('pm.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^grappelli/', include('grappelli.urls')),
    url(r'^select2/', include('django_select2.urls')),
    url(r'^forms/', include(forms_builder.forms.urls)),
    url(r'^explorer/', include('explorer.urls')),
    url(r'^stories/', include('stories.urls')),
    (r'^adminactions/', include('adminactions.urls')),
)

import settings

if settings.DEBUG:
    urlpatterns = patterns('',
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
    url(r'', include('django.contrib.staticfiles.urls')),
) + urlpatterns