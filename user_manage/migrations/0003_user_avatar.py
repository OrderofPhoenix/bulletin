# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-15 12:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_manage', '0002_auto_20170514_0937'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='avatar',
            field=models.ImageField(default='/img/icon.png', height_field=128, upload_to='img', width_field=128),
        ),
    ]
