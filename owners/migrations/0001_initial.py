# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-06 00:51
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('statuses', '0001_initial'),
        ('positions', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Owner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=140)),
                ('identy', models.IntegerField()),
                ('fkposition', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='positions.Position')),
                ('fkstatus', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='statuses.Status')),
            ],
            options={
                'ordering': ('id',),
                'verbose_name': 'Owner',
                'verbose_name_plural': 'Owners',
            },
        ),
    ]
