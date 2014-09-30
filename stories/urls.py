from django.conf.urls import patterns, url
import views

urlpatterns = patterns('',
    url(r'^$', views.home, name='index'),
    url(r'^contact_form/$', views.contact_form, name='contact_form')
)