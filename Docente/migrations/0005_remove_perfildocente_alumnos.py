# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-08-17 06:27
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Docente', '0004_auto_20180817_0126'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='perfildocente',
            name='alumnos',
        ),
    ]
