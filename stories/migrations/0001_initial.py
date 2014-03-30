# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Story'
        db.create_table(u'stories_story', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('tags', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('owner', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('project', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['teams.Project'], null=True)),
            ('state', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('release', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['releases.Release'], null=True)),
            ('points', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('estimated_hours', self.gf('django.db.models.fields.FloatField')(null=True)),
            ('todo_hours', self.gf('django.db.models.fields.FloatField')(null=True)),
            ('actual_hours', self.gf('django.db.models.fields.FloatField')(null=True)),
            ('notes', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('completion_date', self.gf('django.db.models.fields.DateField')(null=True)),
        ))
        db.send_create_signal(u'stories', ['Story'])

        # Adding model 'Task'
        db.create_table(u'stories_task', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('story', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['stories.Story'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('tags', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('owner', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('state', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('estimated_hours', self.gf('django.db.models.fields.FloatField')(null=True)),
            ('todo_hours', self.gf('django.db.models.fields.FloatField')(null=True)),
            ('actual_hours', self.gf('django.db.models.fields.FloatField')(null=True)),
            ('notes', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('completion_date', self.gf('django.db.models.fields.DateField')(null=True)),
        ))
        db.send_create_signal(u'stories', ['Task'])

        # Adding model 'TestCase'
        db.create_table(u'stories_testcase', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('story', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['stories.Story'], null=True)),
            ('project', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['teams.Project'], null=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('tags', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('owner', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('type', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('method', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('priority', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('risk', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('pre_conditions', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('validation_input', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('validation_expected_result', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('post_conditions', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('notes', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'stories', ['TestCase'])

        # Adding model 'Defect'
        db.create_table(u'stories_defect', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('story', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['stories.Story'], null=True)),
            ('project', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['teams.Project'], null=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('tags', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('owner', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('state', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('environment', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('priority', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('severity', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('submitted_by', self.gf('django.db.models.fields.related.ForeignKey')(related_name='submitted_by', to=orm['auth.User'])),
            ('resolution', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('task', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['stories.Task'], null=True)),
            ('notes', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'stories', ['Defect'])


    def backwards(self, orm):
        # Deleting model 'Story'
        db.delete_table(u'stories_story')

        # Deleting model 'Task'
        db.delete_table(u'stories_task')

        # Deleting model 'TestCase'
        db.delete_table(u'stories_testcase')

        # Deleting model 'Defect'
        db.delete_table(u'stories_defect')


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'releases.release': {
            'Meta': {'object_name': 'Release'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'}),
            'production_date': ('django.db.models.fields.DateField', [], {'null': 'True'}),
            'project': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['teams.Project']", 'null': 'True'}),
            'stage_date': ('django.db.models.fields.DateField', [], {'null': 'True'})
        },
        u'stories.defect': {
            'Meta': {'object_name': 'Defect'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'environment': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'notes': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"}),
            'priority': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'project': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['teams.Project']", 'null': 'True'}),
            'resolution': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'severity': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'story': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['stories.Story']", 'null': 'True'}),
            'submitted_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'submitted_by'", 'to': u"orm['auth.User']"}),
            'tags': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'task': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['stories.Task']", 'null': 'True'})
        },
        u'stories.story': {
            'Meta': {'object_name': 'Story'},
            'actual_hours': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'completion_date': ('django.db.models.fields.DateField', [], {'null': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'estimated_hours': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'notes': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"}),
            'points': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'project': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['teams.Project']", 'null': 'True'}),
            'release': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['releases.Release']", 'null': 'True'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'tags': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'todo_hours': ('django.db.models.fields.FloatField', [], {'null': 'True'})
        },
        u'stories.task': {
            'Meta': {'object_name': 'Task'},
            'actual_hours': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'completion_date': ('django.db.models.fields.DateField', [], {'null': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'estimated_hours': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'notes': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'story': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['stories.Story']"}),
            'tags': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'todo_hours': ('django.db.models.fields.FloatField', [], {'null': 'True'})
        },
        u'stories.testcase': {
            'Meta': {'object_name': 'TestCase'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'method': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'notes': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"}),
            'post_conditions': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'pre_conditions': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'priority': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'project': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['teams.Project']", 'null': 'True'}),
            'risk': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'story': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['stories.Story']", 'null': 'True'}),
            'tags': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'validation_expected_result': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'validation_input': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'})
        },
        u'teams.project': {
            'Meta': {'object_name': 'Project'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'})
        }
    }

    complete_apps = ['stories']