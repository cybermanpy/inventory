# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-06 23:47
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0008_auto_20161006_2214'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='asset',
            options={'ordering': ('id',), 'verbose_name': 'Asset', 'verbose_name_plural': 'Assets'},
        ),
    ]
