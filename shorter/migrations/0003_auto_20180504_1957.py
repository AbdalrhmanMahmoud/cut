# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-05-04 17:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shorter', '0002_cuturl_shortcode'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cuturl',
            name='shortCode',
            field=models.CharField(max_length=15, unique=True),
        ),
    ]
