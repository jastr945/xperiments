# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-23 04:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('searchapp', '0006_auto_20171022_0018'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='author',
            field=models.CharField(default='', max_length=255, null=True),
        ),
    ]