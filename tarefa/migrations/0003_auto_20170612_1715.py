# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-06-12 20:15
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tarefa', '0002_auto_20170612_1659'),
    ]

    operations = [
        migrations.RenameField(
            model_name='projeto',
            old_name='Nome',
            new_name='nome',
        ),
        migrations.RenameField(
            model_name='tarefa',
            old_name='Nome',
            new_name='nome',
        ),
    ]