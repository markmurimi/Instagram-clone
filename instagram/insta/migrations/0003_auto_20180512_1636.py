# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-12 13:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('insta', '0002_auto_20180512_1556'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='post',
            field=models.ImageField(default=1, upload_to='Posts/'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='profile_pic',
            field=models.ImageField(default=1, upload_to='Profiles/'),
            preserve_default=False,
        ),
    ]
