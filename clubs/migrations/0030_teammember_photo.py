# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-06-07 06:09
# flake8: noqa
from __future__ import unicode_literals

import clublink.base.utils
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clubs', '0029_auto_20170607_0139'),
    ]

    operations = [
        migrations.AddField(
            model_name='teammember',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to=clublink.base.utils.RandomizedUploadPath('team_member')),
        ),
    ]
