__author__ = 'rangwaln'
import reversion
from django.contrib import admin
from .models import Story, Task, TestCase, Defect, \
    StoryAttachment, TaskAttachment
from django.db.models import Sum
from django.core.urlresolvers import reverse
from django.utils.safestring import mark_safe
from suit.admin import SortableModelAdmin
from suit_redactor.widgets import RedactorWidget
from django import forms
from django.forms import ModelForm
from adminsortable.admin import SortableAdmin
import os.path


class TaskInlineForm(ModelForm):
    class Meta:
        widgets = { 'estimated_hours': forms.TextInput(attrs={'size': 10})
        }

class TaskInline(admin.TabularInline):
    def edit_link(self, instance):
        if instance.id:
            url = reverse('admin:%s_%s_change' % (
                                    instance._meta.app_label,
                                    instance._meta.module_name),
                                    args=[instance.id])
            return mark_safe(u'<a href="{u}">Edit</a>'.format(u=url))
        else:
            return None
    model = Task
    extra = 0
    fields = ['edit_link', 'name', 'owner', 'state', 'estimated_hours', 'todo_hours', 'actual_hours']
    readonly_fields = ('edit_link',)
    suit_classes = 'suit-tab suit-tab-tasks'
    form = TaskInlineForm


class TestCaseInline(admin.TabularInline):
    def edit_link(self, instance):
        if instance.id:
            url = reverse('admin:%s_%s_change' % (
                                    instance._meta.app_label,
                                    instance._meta.module_name),
                                    args=[instance.id])
            return mark_safe(u'<a href="{u}">Edit</a>'.format(u=url))
        else:
            return None
    model = TestCase
    extra = 0
    fields = ['edit_link', 'name', 'owner', 'type', 'priority', 'risk']
    readonly_fields = ('edit_link',)
    suit_classes = 'suit-tab suit-tab-testcases'



class DefectInline(admin.TabularInline):
    def edit_link(self, instance):
        if instance.id:
            url = reverse('admin:%s_%s_change' % (
                                    instance._meta.app_label,
                                    instance._meta.module_name),
                                    args=[instance.id])
            return mark_safe(u'<a href="{u}">Edit</a>'.format(u=url))
        else:
            return None
    model = Defect
    extra = 0
    fields = ['edit_link', 'name', 'owner', 'state', 'priority', 'submitted_by']
    readonly_fields = ('edit_link',)
    suit_classes = 'suit-tab suit-tab-defects'

class StoryAttachmentInline(admin.TabularInline):
    def uploaded_file(self, instance):
        url = "/admin/%s"%instance.file.name
        return mark_safe(u'<a href="{u}">{v}</a>'.format(
            u=url,v=os.path.basename(instance.file.name)))
    model = StoryAttachment
    extra = 1
    suit_classes = 'suit-tab suit-tab-story'
    fields = ['uploaded_file', 'file']
    readonly_fields = ('uploaded_file',)

class StoryForm(ModelForm):
    class Meta:
        widgets = {
            'description': RedactorWidget(editor_options={'lang': 'en'}),
            'notes': RedactorWidget(editor_options={'lang': 'en'})
        }

class StoryAdmin(reversion.VersionAdmin):
    def estimated_hours(self, instance):
        return Task.objects.filter(story=instance).aggregate(total_hours=Sum('estimated_hours'))['total_hours']
    def actual_hours(self, instance):
        return Task.objects.filter(story=instance).aggregate(total_hours=Sum('actual_hours'))['total_hours']
    def todo_hours(self, instance):
        return Task.objects.filter(story=instance).aggregate(total_hours=Sum('todo_hours'))['total_hours']
    list_filter = ['iteration', 'state', 'owner']
    list_display = ['name', 'state', 'owner', 'points', 'estimated_hours', 'todo_hours', 'actual_hours']
    inlines = [TaskInline,TestCaseInline,DefectInline,StoryAttachmentInline,]
    search_fields = ['name']
    fieldsets = (
        (None, {
            'classes': ('suit-tab suit-tab-story',),
            'fields': ('name', 'tags', 'description', 'iteration',
                       ('owner', 'state',), ('project',
                       'release',), ('points', 'actual_hours',),
                       ('estimated_hours', 'todo_hours'), 'notes')
        }),
    )
    readonly_fields = ('actual_hours', 'estimated_hours', 'todo_hours',)
    # sortable = 'order'
    suit_form_tabs = (('story', 'Story'), ('tasks', 'Tasks'), ('testcases', 'Test Cases'), ('defects', 'Defects'))
    form = StoryForm

class TaskAttachmentInline(admin.TabularInline):
    def uploaded_file(self, instance):
        url = "/admin/%s"%instance.file.name
        return mark_safe(u'<a href="{u}">{v}</a>'.format(
            u=url,v=os.path.basename(instance.file.name)))
    model = TaskAttachment
    extra = 1
    suit_classes = 'suit-tab suit-tab-story'
    fields = ['uploaded_file', 'file']
    readonly_fields = ('uploaded_file',)

class TaskForm(ModelForm):
    class Meta:
        widgets = {
            'description': RedactorWidget(editor_options={'lang': 'en'}),
            'notes': RedactorWidget(editor_options={'lang': 'en'})
        }

class TaskAdmin(reversion.VersionAdmin):
    inlines = [TaskAttachmentInline,]
    form = TaskForm
    readonly_fields = ('story',)

admin.site.register(Story, StoryAdmin)
admin.site.register(Task, TaskAdmin)
admin.site.register(TestCase)
admin.site.register(Defect)
