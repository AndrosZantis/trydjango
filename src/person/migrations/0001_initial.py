# -*- coding: utf-8 -*-
# Generated by Django 1.11.25 on 2019-10-07 21:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('surname', models.TextField()),
                ('dob', models.TextField()),
                ('description', models.TextField()),
            ],
        ),
    ]
