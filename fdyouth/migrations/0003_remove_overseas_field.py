# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fdyouth', '0002_auto_20141229_0352'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='overseas',
            name='field',
        ),
    ]
