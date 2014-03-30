from django.db import models
from pm.models import TimeStampedModel

class Release(TimeStampedModel):
    name = models.CharField(max_length=255, null=False, blank=False,
                             unique=True)
    stage_date = models.DateField(null=True, blank=True)
    production_date = models.DateField(null=True, blank=True)
    project = models.ForeignKey("teams.Project", null=True, blank=True)

    def __unicode__(self):
		return self.name


class Iteration(TimeStampedModel):
    name = models.CharField(max_length=255, null=False, blank=False,
                             unique=True)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    release = models.ForeignKey(Release, null=True, blank=True)
    project = models.ForeignKey("teams.Project", null=True, blank=True)
    team = models.ForeignKey("teams.Team", null=True, blank=True)

    def __unicode__(self):
		return self.name
