# Generated by Django 2.0 on 2018-02-06 20:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('src', '0015_remove_post_author'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='user',
        ),
        migrations.DeleteModel(
            name='UserProfile',
        ),
    ]
