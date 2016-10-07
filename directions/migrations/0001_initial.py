# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-04 00:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Direction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('acronym', models.CharField(max_length=50)),
                ('dirname', models.CharField(max_length=140)),
                ('dirnumber', models.IntegerField()),
            ],
            options={
                'verbose_name': 'Direction',
                'verbose_name_plural': 'Directions',
            },
        ),
    ]
