# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-02 01:59
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('typeeqs', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Description',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=140)),
                ('fktype', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='typeeqs.TypeEq')),
            ],
        ),
    ]
