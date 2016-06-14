# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-13 09:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vstream', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Videoinfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=100)),
                ('url', models.TextField(max_length=100)),
                ('description', models.TextField(max_length=500, null=True)),
                ('videodate', models.DateField(null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='video_info',
        ),
    ]