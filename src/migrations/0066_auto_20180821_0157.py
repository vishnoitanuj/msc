# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-08-20 20:27
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('src', '0065_auto_20180821_0153'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event_registration',
            name='a',
        ),
        migrations.RemoveField(
            model_name='registration',
            name='c',
        ),
    ]
