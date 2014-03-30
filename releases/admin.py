__author__ = 'rangwaln'
from django.contrib import admin
from .models import Release, Iteration

admin.site.register(Release)
admin.site.register(Iteration)