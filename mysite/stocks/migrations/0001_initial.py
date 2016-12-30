# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Stocks',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ticker', models.CharField(max_length=20)),
                ('name', models.CharField(max_length=100)),
                ('d_open', models.FloatField()),
                ('d_close', models.FloatField()),
            ],
        ),
    ]
