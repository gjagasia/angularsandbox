# -*- coding: utf-8 -*-
# Generated by Django 1.11b1 on 2017-12-07 17:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foodpledge', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='food',
            name='food_picture',
            field=models.URLField(blank=True, max_length=1024, null=True),
        ),
    ]
