# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-11 16:17
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0002_auto_20180511_1838'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_name', models.CharField(max_length=30)),
                ('post_caption', models.TextField()),
                ('post', models.ImageField(upload_to='')),
                ('editor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gallery.Editor')),
            ],
        ),
    ]
