# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-29 04:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('judge', '0005_auto_20170928_0025'),
    ]

    operations = [
        migrations.RenameField(
            model_name='member',
            old_name='edit',
            new_name='update',
        ),
        migrations.AlterField(
            model_name='member',
            name='AC',
            field=models.IntegerField(default=0),
        ),
    ]
