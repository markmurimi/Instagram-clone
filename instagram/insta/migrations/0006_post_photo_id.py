# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-13 13:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('insta', '0005_auto_20180512_1749'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='photo_id',
            field=models.CharField(default=1, max_length=30),
            preserve_default=False,
        ),
    ]
