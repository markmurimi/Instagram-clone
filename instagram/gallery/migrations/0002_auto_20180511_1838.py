# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-11 15:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='editor',
            old_name='first_name',
            new_name='editor_name',
        ),
        migrations.RemoveField(
            model_name='editor',
            name='last_name',
        ),
        migrations.AddField(
            model_name='editor',
            name='profile_photo',
            field=models.ImageField(default=1, upload_to=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='editor',
            name='user_bio',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='editor',
            name='username',
            field=models.CharField(max_length=10, unique=True),
        ),
    ]
