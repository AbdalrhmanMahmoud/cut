# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-05-10 18:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('analytics', '0002_auto_20180510_0102'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clickevent',
            name='count',
            field=models.IntegerField(default=2),
        ),
    ]