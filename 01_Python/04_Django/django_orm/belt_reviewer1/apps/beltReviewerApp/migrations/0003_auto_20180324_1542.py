# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-03-24 22:42
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('beltReviewerApp', '0002_auto_20180324_1536'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='users',
            new_name='user',
        ),
    ]
