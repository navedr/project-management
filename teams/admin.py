__author__ = 'rangwaln'
from django.contrib import admin
from .models import Team, Project

admin.site.register(Team)
admin.site.register(Project)