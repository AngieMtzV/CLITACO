# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-08-30 21:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HistoriaClinica', '0003_auto_20180830_1614'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historiaclinica',
            name='Motivo_Consulta',
            field=models.TextField(default='', verbose_name='Motivo de Consulta'),
        ),
    ]