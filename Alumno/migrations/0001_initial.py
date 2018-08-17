# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-08-16 22:53
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Grupo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group', models.CharField(max_length=1, verbose_name='Grupo')),
            ],
        ),
        migrations.CreateModel(
            name='Modulo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('modulo', models.CharField(max_length=150, verbose_name='Modulo')),
            ],
        ),
        migrations.CreateModel(
            name='PerfilAlumno',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagen_alumno', models.ImageField(default='us_alumno.png', upload_to='imagen-alumnos', verbose_name='Foto de Perfil')),
                ('unidad', models.CharField(max_length=30, verbose_name='Unidad')),
                ('grupo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Alumno.Grupo')),
                ('modulo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Alumno.Modulo')),
            ],
        ),
        migrations.CreateModel(
            name='Semestre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sem', models.CharField(max_length=2, verbose_name='Semestre')),
            ],
        ),
        migrations.CreateModel(
            name='Turno',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('turn', models.CharField(max_length=1, verbose_name='Turno')),
            ],
        ),
    ]
