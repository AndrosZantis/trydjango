# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2019-10-08 09:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('person', '0003_auto_20191007_2151'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='employed',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
    ]