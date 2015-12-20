# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-17 16:18
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('judge', '0045_auto_20151217_1812'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='problem',
            options={'ordering': ['-id'], 'permissions': (('retest_problem', 'Can start a retest'), ('change_visibility_of_problem', 'Can change the visibility of a problem'), ('see_hidden_problems', 'Can see hidden problems'), ('add_media_to_problem', 'Can upload media for a problem'), ('add_checker_to_problem', 'Can add a checker for a problem'))},
        ),
    ]