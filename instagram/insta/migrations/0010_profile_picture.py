# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-14 11:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('insta', '0009_profile_profile_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='picture',
            field=models.ImageField(default=1, upload_to='profiles/'),
            preserve_default=False,
        ),
    ]
