# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-08-31 22:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HistoriaClinica', '0006_auto_20180830_1639'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historiaclinica',
            name='aut_docente',
            field=models.BooleanField(default=False, editable=False, verbose_name='Autorizaci\xf3n del Docente'),
        ),
    ]