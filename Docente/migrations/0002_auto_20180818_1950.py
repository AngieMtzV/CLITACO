# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-08-19 00:50
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Alumno', '0002_auto_20180818_1950'),
        ('Docente', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='perfildocente',
            name='perfil_docente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_docente', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='docentealumno',
            name='alumno',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Alumno.PerfilAlumno'),
        ),
    ]