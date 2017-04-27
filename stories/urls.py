from django.conf.urls import url
import views

urlpatterns = [
    url(r'^$', views.home, name='index'),
    url(r'^contact_form/$', views.contact_form, name='contact_form')
]
