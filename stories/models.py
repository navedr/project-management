from django.db import models
from pm.models import TimeStampedModel
from django.contrib.auth.models import User
from multi_email_field.fields import MultiEmailField
from adminsortable.models import Sortable

STATE_CHOICES = (('Defined', 'Defined'),
                       ('In-Progress', 'In-Progress'),
                       ('Completed', 'Completed'),
                        ('Accepted', 'Accepted'),
                       ('User Accepted', 'User Accepted'),)
TESTCASE_TYPE_CHOICES = (('Acceptance', 'Acceptance'),
                       ('Functional', 'Functional'),
                       ('Performance', 'Performance'),
                        ('Regression', 'Regression'),
                       ('Usability', 'Usability'),
                        ('User Interface', 'User Interface'),)
TESTCASE_METHOD_CHOICES = (('Manual', 'Manual'),
                       ('Automated', 'Automated'),)
TESTCASE_PRIORITY_CHOICES = (('Useful', 'Useful'),
                       ('Important', 'Important'),
                        ('Critical', 'Critical'),)
TESTCASE_RISK_CHOICES = (('Low', 'Low'),
                       ('Medium', 'Medium'),
                        ('High', 'High'),)
DEFECT_STATE_CHOICES = (('Submitted', 'Submitted'),
                       ('Open', 'Open'),
                       ('Fixed', 'Fixed'),
                        ('Closed', 'Closed'),)
DEFECT_ENV_CHOICES = (('Development', 'Development'),
                       ('Test', 'Test'),
                       ('Staging', 'Staging'),
                        ('Production', 'Production'),)
DEFECT_PRIORITY_CHOICES = (('Resolve Immediately', 'Resolve Immediately'),
                       ('High Attention', 'High Attention'),
                       ('Normal', 'Normal'),
                        ('Low', 'Low'),)
DEFECT_SEVERITY_CHOICES = (('Crash/Data Loss', 'Crash/Data Loss'),
                       ('Major Problem', 'Major Problem'),
                       ('Minor Problem', 'Minor Problem'),
                        ('Cosmetic', 'Cosmetic'),)
DEFECT_RESOLUTION_CHOICES = (('Architecture', 'Architecture'),
                       ('Code Change', 'Code Change'),
                       ('Configuration Change', 'Configuration Change'),
                        ('Database Change', 'Database Change'),
                        ('Duplicate', 'Duplicate'),
                       ('Need More Information', 'Need More Information'),
                        ('Not a Defect', 'Not a Defect'),
                        ('Software Limitation', 'Software Limitation'),
                       ('User Interface', 'User Interface'),
                        ('Converted', 'Converted'),)
class Story(TimeStampedModel):
    iteration  = models.ForeignKey("releases.Iteration", null=True, blank=True)
    name = models.CharField(max_length=255, null=False, blank=False)
    tags = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    owner = models.ForeignKey(User, null=True, blank=True)
    project = models.ForeignKey("teams.Project", null=True, blank=True)
    state = models.CharField(max_length=255, null=False, blank=False, choices=STATE_CHOICES)
    release = models.ForeignKey("releases.Release", null=True, blank=True)
    points = models.IntegerField(null=True, blank=True)
    notes = models.TextField(null=True, blank=True)
    completion_date = models.DateField(null=True, blank=True)
    order = models.PositiveIntegerField(default=1)
    emails = MultiEmailField(null=True)
    email = models.CharField(max_length=1024, null=True)

    def __unicode__(self):
		return self.name

    class Meta:
        verbose_name_plural = 'Stories'

    def forwards(self, orm):
        for index, story in enumerate(orm.Story.objects.all()):
            story.order = index + 1
            story.save()

class Task(TimeStampedModel):
    story = models.ForeignKey(Story)
    name = models.CharField(max_length=255, null=False, blank=False)
    tags = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    owner = models.ForeignKey(User, null=True, blank=True)
    state = models.CharField(max_length=255, null=False, blank=False, choices=STATE_CHOICES)
    estimated_hours = models.FloatField(null=True, blank=True)
    todo_hours = models.FloatField(null=True, blank=True)
    actual_hours = models.FloatField(null=True, blank=True)
    notes = models.TextField(null=True, blank=True)
    completion_date = models.DateField(null=True, blank=True)
    position = models.PositiveSmallIntegerField("Position")

    class Meta:
        ordering = ['position']

    def __unicode__(self):
        return self.name


class TestCase(TimeStampedModel):
    story = models.ForeignKey(Story, null=True, blank=True)
    project = models.ForeignKey("teams.Project", null=True, blank=True)
    name = models.CharField(max_length=255, null=False, blank=False)
    tags = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    owner = models.ForeignKey(User, null=True, blank=True)
    type = models.CharField(max_length=255, null=True, blank=True, choices=TESTCASE_TYPE_CHOICES)
    method = models.CharField(max_length=255, null=True, blank=True, choices=TESTCASE_METHOD_CHOICES)
    priority = models.CharField(max_length=255, null=True, blank=True, choices=TESTCASE_PRIORITY_CHOICES)
    risk = models.CharField(max_length=255, null=True, blank=True, choices=TESTCASE_RISK_CHOICES)
    pre_conditions = models.TextField(null=True, blank=True)
    validation_input = models.TextField(null=True, blank=True)
    validation_expected_result = models.TextField(null=True, blank=True)
    post_conditions = models.TextField(null=True, blank=True)
    notes = models.TextField(null=True, blank=True)

    def __unicode__(self):
        return self.name


class Defect(TimeStampedModel):
    story = models.ForeignKey(Story, null=True, blank=True)
    project = models.ForeignKey("teams.Project", null=True, blank=True)
    name = models.CharField(max_length=255, null=False, blank=False)
    tags = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    owner = models.ForeignKey(User, null=True, blank=True)
    state = models.CharField(max_length=255, null=False, blank=False, choices=DEFECT_STATE_CHOICES)
    environment = models.CharField(max_length=255, null=True, blank=True, choices=DEFECT_ENV_CHOICES)
    priority = models.CharField(max_length=255, null=True, blank=True, choices=DEFECT_PRIORITY_CHOICES)
    severity = models.CharField(max_length=255, null=True, blank=True, choices=DEFECT_SEVERITY_CHOICES)
    submitted_by = models.ForeignKey(User, related_name='submitted_by')
    resolution = models.CharField(max_length=255, null=True, blank=True, choices=DEFECT_RESOLUTION_CHOICES)
    task = models.ForeignKey(Task, null=True, blank=True)
    notes = models.TextField(null=True, blank=True)

    def __unicode__(self):
        return self.name


class StoryAttachment(TimeStampedModel):
    story = models.ForeignKey(Story)
    file = models.FileField(upload_to='attachments/stories/%Y/%m/%d')

    class Meta:
		verbose_name = "Attachment"
		verbose_name_plural = 'Attachments'

class TaskAttachment(TimeStampedModel):
    task = models.ForeignKey(Task)
    file = models.FileField(upload_to='attachments/tasks/%Y/%m/%d')

    class Meta:
		verbose_name = "Attachment"
		verbose_name_plural = 'Attachments'

class TestCaseAttachment(TimeStampedModel):
    testcase = models.ForeignKey(TestCase)
    file = models.FileField(upload_to='attachments/testcases/%Y/%m/%d')

    class Meta:
		verbose_name = "Attachment"
		verbose_name_plural = 'Attachments'


class DefectAttachment(TimeStampedModel):
    defect = models.ForeignKey(Defect)
    file = models.FileField(upload_to='attachments/defects/%Y/%m/%d')

    class Meta:
		verbose_name = "Attachment"
		verbose_name_plural = 'Attachments'