# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-12-09 22:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clubs', '0079_club_use_corp_styles'),
    ]

    operations = [
        migrations.AddField(
            model_name='club',
            name='sales_email',
            field=models.EmailField(blank=True, help_text='Override email for membership inquiries.  Otherwise, it uses the generic one on the server.', max_length=254, null=True),
        ),
    ]
