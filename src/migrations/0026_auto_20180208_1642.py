# Generated by Django 2.0 on 2018-02-08 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('src', '0025_auto_20180208_0406'),
    ]

    operations = [
        migrations.AddField(
            model_name='inspirusus_gallery',
            name='caption',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='msweek_gallery',
            name='caption',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='rumble_gallery',
            name='caption',
            field=models.TextField(blank=True),
        ),
    ]
