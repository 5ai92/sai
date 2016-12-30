# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stocks', '0003_auto_20161226_2335'),
    ]

    operations = [
        migrations.RenameField(
            model_name='stocks',
            old_name='companyname',
            new_name='company',
        ),
        migrations.RenameField(
            model_name='stocks',
            old_name='ticker',
            new_name='symbol',
        ),
    ]
