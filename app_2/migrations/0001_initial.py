# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-08-06 14:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Model1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fchar', models.CharField(max_length=100)),
                ('fdate', models.DateField(blank=True, null=True)),
                ('fdatetime', models.DateTimeField(auto_now_add=True)),
                ('fbool', models.BooleanField()),
                ('fdeci', models.DecimalField(decimal_places=2, max_digits=6)),
                ('fint', models.IntegerField()),
                ('furl', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Model2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('f2char', models.CharField(max_length=100)),
                ('f2date', models.DateField(blank=True, null=True)),
                ('f2datetime', models.DateTimeField(auto_now_add=True)),
                ('f2bool', models.BooleanField()),
                ('f2deci', models.DecimalField(decimal_places=2, max_digits=6)),
                ('f2int', models.IntegerField()),
                ('f2url', models.URLField()),
            ],
        ),
    ]
