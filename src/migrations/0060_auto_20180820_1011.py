# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-08-20 04:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('src', '0059_auto_20180820_0427'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registration',
            name='roll_number',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]
