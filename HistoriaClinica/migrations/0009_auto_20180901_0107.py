# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-09-01 06:07
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('HistoriaClinica', '0008_auto_20180901_0055'),
    ]

    operations = [
        migrations.AddField(
            model_name='planejecucion',
            name='plan_tratamiento',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='HistoriaClinica.PlanTratamiento'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='plantratamiento',
            name='historiaControlada',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='HistoriaClinica.HistoriaClinicaControlado'),
            preserve_default=False,
        ),
    ]
