# -*- coding: utf-8 -*-
# Generated by Django 1.11b1 on 2018-03-24 21:28
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('src', '0050_auto_20180325_0252'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event_registration',
            old_name='tech_quiz',
            new_name='a',
        ),
    ]
