# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Release'
        db.create_table(u'releases_release', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=255)),
            ('stage_date', self.gf('django.db.models.fields.DateField')(null=True)),
            ('production_date', self.gf('django.db.models.fields.DateField')(null=True)),
            ('project', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['teams.Project'], null=True)),
        ))
        db.send_create_signal(u'releases', ['Release'])

        # Adding model 'Iteration'
        db.create_table(u'releases_iteration', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=255)),
            ('start_date', self.gf('django.db.models.fields.DateField')(null=True)),
            ('end_date', self.gf('django.db.models.fields.DateField')(null=True)),
            ('release', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['releases.Release'], null=True)),
            ('project', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['teams.Project'], null=True)),
        ))
        db.send_create_signal(u'releases', ['Iteration'])


    def backwards(self, orm):
        # Deleting model 'Release'
        db.delete_table(u'releases_release')

        # Deleting model 'Iteration'
        db.delete_table(u'releases_iteration')


    models = {
        u'releases.iteration': {
            'Meta': {'object_name': 'Iteration'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'end_date': ('django.db.models.fields.DateField', [], {'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'}),
            'project': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['teams.Project']", 'null': 'True'}),
            'release': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['releases.Release']", 'null': 'True'}),
            'start_date': ('django.db.models.fields.DateField', [], {'null': 'True'})
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
        u'teams.project': {
            'Meta': {'object_name': 'Project'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'})
        }
    }

    complete_apps = ['releases']