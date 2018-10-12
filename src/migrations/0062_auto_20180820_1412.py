# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-08-20 08:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('src', '0061_auto_20180820_1100'),
    ]

    operations = [
        migrations.DeleteModel(
            name='registration',
        ),
        migrations.AlterField(
            model_name='event_registration',
            name='contact',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='event_registration',
            name='email',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='event_registration',
            name='name',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='event_registration',
            name='year',
            field=models.CharField(max_length=200),
        ),
    ]
