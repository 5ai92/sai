# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stocks', '0002_auto_20161226_2326'),
    ]

    operations = [
        migrations.RenameField(
            model_name='stocks',
            old_name='comanyname',
            new_name='companyname',
        ),
    ]
