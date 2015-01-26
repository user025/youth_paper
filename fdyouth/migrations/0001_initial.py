# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='academy',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255)),
                ('date', models.DateTimeField()),
                ('author', models.CharField(max_length=255)),
                ('field', models.CharField(max_length=255)),
                ('keyword', models.CharField(max_length=255)),
                ('issue', models.IntegerField()),
                ('location', models.CharField(max_length=255)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='news',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255)),
                ('date', models.DateTimeField()),
                ('keyword', models.CharField(max_length=255)),
                ('issue', models.IntegerField()),
                ('location', models.CharField(max_length=255)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='overseas',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255)),
                ('date', models.DateTimeField()),
                ('author', models.CharField(max_length=255)),
                ('place', models.CharField(max_length=255)),
                ('field', models.CharField(max_length=255)),
                ('keyword', models.CharField(max_length=255)),
                ('issue', models.IntegerField()),
                ('location', models.CharField(max_length=255)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
