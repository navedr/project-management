# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-04-27 07:46
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('releases', '__first__'),
        ('teams', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Defect',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255)),
                ('tags', models.CharField(blank=True, max_length=255, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('state', models.CharField(choices=[(b'Submitted', b'Submitted'), (b'Open', b'Open'), (b'Fixed', b'Fixed'), (b'Closed', b'Closed')], max_length=255)),
                ('environment', models.CharField(blank=True, choices=[(b'Development', b'Development'), (b'Test', b'Test'), (b'Staging', b'Staging'), (b'Production', b'Production')], max_length=255, null=True)),
                ('priority', models.CharField(blank=True, choices=[(b'Resolve Immediately', b'Resolve Immediately'), (b'High Attention', b'High Attention'), (b'Normal', b'Normal'), (b'Low', b'Low')], max_length=255, null=True)),
                ('severity', models.CharField(blank=True, choices=[(b'Crash/Data Loss', b'Crash/Data Loss'), (b'Major Problem', b'Major Problem'), (b'Minor Problem', b'Minor Problem'), (b'Cosmetic', b'Cosmetic')], max_length=255, null=True)),
                ('resolution', models.CharField(blank=True, choices=[(b'Architecture', b'Architecture'), (b'Code Change', b'Code Change'), (b'Configuration Change', b'Configuration Change'), (b'Database Change', b'Database Change'), (b'Duplicate', b'Duplicate'), (b'Need More Information', b'Need More Information'), (b'Not a Defect', b'Not a Defect'), (b'Software Limitation', b'Software Limitation'), (b'User Interface', b'User Interface'), (b'Converted', b'Converted')], max_length=255, null=True)),
                ('notes', models.TextField(blank=True, null=True)),
                ('owner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('project', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='teams.Project')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='DefectAttachment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('file', models.FileField(upload_to=b'attachments/defects/%Y/%m/%d')),
                ('defect', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stories.Defect')),
            ],
            options={
                'verbose_name': 'Attachment',
                'verbose_name_plural': 'Attachments',
            },
        ),
        migrations.CreateModel(
            name='Story',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255)),
                ('tags', models.CharField(blank=True, max_length=255, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('state', models.CharField(choices=[(b'Defined', b'Defined'), (b'In-Progress', b'In-Progress'), (b'Completed', b'Completed'), (b'Accepted', b'Accepted'), (b'User Accepted', b'User Accepted')], max_length=255)),
                ('points', models.IntegerField(blank=True, null=True)),
                ('notes', models.TextField(blank=True, null=True)),
                ('completion_date', models.DateField(blank=True, null=True)),
                ('order', models.PositiveIntegerField(default=1)),
                ('emails', models.EmailField(max_length=254, null=True)),
                ('email', models.CharField(max_length=1024, null=True)),
                ('iteration', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='releases.Iteration')),
                ('owner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('project', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='teams.Project')),
                ('release', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='releases.Release')),
            ],
            options={
                'verbose_name_plural': 'Stories',
            },
        ),
        migrations.CreateModel(
            name='StoryAttachment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('file', models.FileField(upload_to=b'attachments/stories/%Y/%m/%d')),
                ('story', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stories.Story')),
            ],
            options={
                'verbose_name': 'Attachment',
                'verbose_name_plural': 'Attachments',
            },
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255)),
                ('tags', models.CharField(blank=True, max_length=255, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('state', models.CharField(choices=[(b'Defined', b'Defined'), (b'In-Progress', b'In-Progress'), (b'Completed', b'Completed'), (b'Accepted', b'Accepted'), (b'User Accepted', b'User Accepted')], max_length=255)),
                ('estimated_hours', models.FloatField(blank=True, null=True)),
                ('todo_hours', models.FloatField(blank=True, null=True)),
                ('actual_hours', models.FloatField(blank=True, null=True)),
                ('notes', models.TextField(blank=True, null=True)),
                ('completion_date', models.DateField(blank=True, null=True)),
                ('position', models.PositiveSmallIntegerField(verbose_name=b'Position')),
                ('owner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('story', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stories.Story')),
            ],
            options={
                'ordering': ['position'],
            },
        ),
        migrations.CreateModel(
            name='TaskAttachment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('file', models.FileField(upload_to=b'attachments/tasks/%Y/%m/%d')),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stories.Task')),
            ],
            options={
                'verbose_name': 'Attachment',
                'verbose_name_plural': 'Attachments',
            },
        ),
        migrations.CreateModel(
            name='TestCase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255)),
                ('tags', models.CharField(blank=True, max_length=255, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('type', models.CharField(blank=True, choices=[(b'Acceptance', b'Acceptance'), (b'Functional', b'Functional'), (b'Performance', b'Performance'), (b'Regression', b'Regression'), (b'Usability', b'Usability'), (b'User Interface', b'User Interface')], max_length=255, null=True)),
                ('method', models.CharField(blank=True, choices=[(b'Manual', b'Manual'), (b'Automated', b'Automated')], max_length=255, null=True)),
                ('priority', models.CharField(blank=True, choices=[(b'Useful', b'Useful'), (b'Important', b'Important'), (b'Critical', b'Critical')], max_length=255, null=True)),
                ('risk', models.CharField(blank=True, choices=[(b'Low', b'Low'), (b'Medium', b'Medium'), (b'High', b'High')], max_length=255, null=True)),
                ('pre_conditions', models.TextField(blank=True, null=True)),
                ('validation_input', models.TextField(blank=True, null=True)),
                ('validation_expected_result', models.TextField(blank=True, null=True)),
                ('post_conditions', models.TextField(blank=True, null=True)),
                ('notes', models.TextField(blank=True, null=True)),
                ('owner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('project', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='teams.Project')),
                ('story', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='stories.Story')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TestCaseAttachment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('file', models.FileField(upload_to=b'attachments/testcases/%Y/%m/%d')),
                ('testcase', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stories.TestCase')),
            ],
            options={
                'verbose_name': 'Attachment',
                'verbose_name_plural': 'Attachments',
            },
        ),
        migrations.AddField(
            model_name='defect',
            name='story',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='stories.Story'),
        ),
        migrations.AddField(
            model_name='defect',
            name='submitted_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='submitted_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='defect',
            name='task',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='stories.Task'),
        ),
    ]
