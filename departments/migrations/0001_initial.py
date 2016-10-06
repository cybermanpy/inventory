# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-06 00:51
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('directions', '0002_auto_20161006_0051'),
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('acronym', models.CharField(max_length=50)),
                ('depname', models.CharField(max_length=140)),
                ('depnumber', models.IntegerField()),
                ('fkdirection', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='directions.Direction')),
            ],
            options={
                'ordering': ('id',),
                'verbose_name': 'Department',
                'verbose_name_plural': 'Departments',
            },
        ),
    ]
