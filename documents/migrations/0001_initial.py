# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-06 20:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('desdocument', models.CharField(max_length=140)),
            ],
            options={
                'ordering': ('id',),
                'verbose_name': 'Document',
                'verbose_name_plural': 'Documents',
            },
        ),
    ]
