# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-27 16:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('judge', '0002_member_edit'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='AC',
            field=models.TextField(blank=True, default='[]'),
        ),
        migrations.AlterField(
            model_name='member',
            name='overview',
            field=models.CharField(blank=True, default='', max_length=500),
        ),
        migrations.AlterField(
            model_name='member',
            name='pphone',
            field=models.CharField(blank=True, default='', max_length=10),
        ),
    ]