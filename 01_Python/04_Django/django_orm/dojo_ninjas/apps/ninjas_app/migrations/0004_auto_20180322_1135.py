# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-03-22 18:35
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ninjas_app', '0003_dojo_desc'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ninja',
            old_name='dojo_id',
            new_name='dojo',
        ),
    ]
