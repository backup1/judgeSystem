# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-08 15:44
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('judge', '0030_auto_20151206_1126'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='test',
            options={'ordering': ['-test_group', 'pk'], 'permissions': (('view_test', 'Can see input/output files'),)},
        ),
        migrations.AlterModelOptions(
            name='testgroup',
            options={'ordering': ['pk']},
        ),
        migrations.AlterField(
            model_name='test',
            name='test_group',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='judge.TestGroup'),
        ),
    ]
