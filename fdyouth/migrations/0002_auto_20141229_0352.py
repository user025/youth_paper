# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('fdyouth', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='academy',
            name='location',
        ),
        migrations.RemoveField(
            model_name='news',
            name='location',
        ),
        migrations.RemoveField(
            model_name='overseas',
            name='location',
        ),
        migrations.AddField(
            model_name='academy',
            name='article',
            field=models.FileField(default=datetime.datetime(2014, 12, 29, 3, 52, 25, 11068, tzinfo=utc), upload_to=b'academy/'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='news',
            name='article',
            field=models.FileField(default=datetime.datetime(2014, 12, 29, 3, 52, 30, 707908, tzinfo=utc), upload_to=b'news/'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='overseas',
            name='article',
            field=models.FileField(default=datetime.datetime(2014, 12, 29, 3, 52, 36, 700115, tzinfo=utc), upload_to=b'overseas/'),
            preserve_default=False,
        ),
    ]
