# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-08-21 07:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('src', '0066_auto_20180821_0157'),
    ]

    operations = [
        migrations.CreateModel(
            name='contact_request',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact_name', models.CharField(blank=True, max_length=200)),
                ('contact_email', models.EmailField(blank=True, max_length=200)),
                ('content', models.TextField(null=True)),
            ],
        ),
    ]
