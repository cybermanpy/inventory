# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-06 00:51
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('directions', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='direction',
            options={'ordering': ('id',), 'verbose_name': 'Direction', 'verbose_name_plural': 'Directions'},
        ),
    ]
