# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-29 10:54
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('blog', '0003_post_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='type',
        ),
    ]
