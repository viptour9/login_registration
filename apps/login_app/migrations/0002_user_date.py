# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-24 20:49
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='date',
            field=models.DateField(blank=True, default=datetime.datetime(2017, 10, 24, 20, 49, 46, 211707), verbose_name='YYYY-MM-DD'),
        ),
    ]