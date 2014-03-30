from django.db import models
from pm.models import TimeStampedModel

class Team(TimeStampedModel):
    name = models.CharField(max_length=255, null=False, blank=False,
                             unique=True)

    def __unicode__(self):
		return self.name


class Project(TimeStampedModel):
    name = models.CharField(max_length=255, null=False, blank=False,
                             unique=True)
    team = models.ForeignKey(Team, null=True, blank=True)

    def __unicode__(self):
		return self.name