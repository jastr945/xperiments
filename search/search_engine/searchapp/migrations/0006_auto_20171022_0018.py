# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-22 00:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('searchapp', '0005_auto_20171021_2326'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='body',
            field=models.TextField(default='', max_length=100000, null=True),
        ),
    ]