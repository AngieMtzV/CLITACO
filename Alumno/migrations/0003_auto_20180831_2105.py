# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-09-01 02:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Alumno', '0002_auto_20180818_1950'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perfilalumno',
            name='imagen_alumno',
            field=models.ImageField(blank=True, default='us_alumno.png', upload_to='imagen-alumnos', verbose_name='Foto de Perfil'),
        ),
    ]
