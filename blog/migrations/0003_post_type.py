# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-29 10:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('blog', '0002_auto_20161228_2133'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='type',
            field=models.IntegerField(choices=[(0, 'Post'), (1, 'Page')], default=0),
        ),
    ]
