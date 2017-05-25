# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-05-25 19:37
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('assets', '0011_auto_20161013_1308'),
        ('owners', '0001_initial'),
        ('departments', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AssetLend',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fkasset', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='assets.Asset')),
            ],
            options={
                'ordering': ('id',),
                'verbose_name': 'Asset Lend',
                'verbose_name_plural': 'Asset Loans',
            },
        ),
        migrations.CreateModel(
            name='Lend',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reason', models.CharField(max_length=50)),
                ('datelend', models.DateField()),
                ('lastlend', models.BooleanField()),
                ('devolution', models.DateField(blank=True, null=True)),
                ('formlend', models.FileField(blank=True, null=True, upload_to='loans/%Y/%m/%d/')),
                ('details', models.ManyToManyField(through='loans.AssetLend', to='assets.Asset')),
                ('fkdepartment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='departments.Department')),
                ('fkowner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='owners.Owner')),
            ],
            options={
                'ordering': ('id',),
                'verbose_name': 'Lend',
                'verbose_name_plural': 'Loans',
            },
        ),
        migrations.AddField(
            model_name='assetlend',
            name='fklend',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='loans.Lend'),
        ),
    ]