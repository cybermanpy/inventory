# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-06 23:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TypeTransfer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('destypetransfer', models.CharField(max_length=50)),
            ],
            options={
                'ordering': ('id',),
                'verbose_name': 'Types Tranfers',
            },
        ),
    ]