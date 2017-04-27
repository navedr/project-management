from django.conf.urls import include, url
import forms_builder.forms.urls
from django.contrib.admin import site
import adminactions.actions as actions

# register all adminactions
actions.add_to_site(site)
# Uncomment the next two lines to enable the admin:
from django.contrib import admin

admin.autodiscover()

urlpatterns = [
    url(r'^jet/', include('jet.urls', 'jet')),
    url(r'^jet/dashboard/', include('jet.dashboard.urls', 'jet-dashboard')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^select2/', include('django_select2.urls')),
    url(r'^forms/', include(forms_builder.forms.urls)),
    url(r'^explorer/', include('explorer.urls')),
    url(r'^stories/', include('stories.urls')),
    url(r'^adminactions/', include('adminactions.urls')),
]

# import settings

# if settings.DEBUG:
#     urlpatterns = [
#                       url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
#                           {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
#                       url(r'', include('django.contrib.staticfiles.urls')),
#                   ] + urlpatterns
