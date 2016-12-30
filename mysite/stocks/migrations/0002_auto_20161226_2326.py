# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stocks', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='stocks',
            old_name='name',
            new_name='comanyname',
        ),
        migrations.RemoveField(
            model_name='stocks',
            name='d_close',
        ),
        migrations.RemoveField(
            model_name='stocks',
            name='d_open',
        ),
    ]
