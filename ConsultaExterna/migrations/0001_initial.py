# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-08-02 16:59
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='avanceRapido',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('diagnostico_AR', models.TextField(verbose_name='Diagnostico')),
                ('peso_AR', models.IntegerField(verbose_name='Peso:')),
                ('talla_AR', models.IntegerField(verbose_name='Talla:')),
                ('imc_AR', models.IntegerField(verbose_name='IMC:')),
                ('ta_AR1', models.IntegerField(verbose_name='TA:')),
                ('ta_AR2', models.IntegerField(verbose_name='TA:')),
                ('fc_AR', models.IntegerField(verbose_name='FC:')),
                ('fr_AR', models.IntegerField(verbose_name='FR:')),
                ('bioquimicos_AR', models.TextField(verbose_name='Bioquimicos de Relevancia')),
            ],
        ),
        migrations.CreateModel(
            name='evolucionConsultaExterna',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateTimeField(auto_now_add=True, verbose_name='Fecha')),
                ('signos', models.TextField(verbose_name='Signos')),
            ],
        ),
        migrations.CreateModel(
            name='medicoExterno',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagen_alumno', models.ImageField(default='us_alumno.png', upload_to='imagen-medicos', verbose_name='Foto de Perfil')),
                ('avances_rapidos', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='ConsultaExterna.avanceRapido')),
                ('evoluciones', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='ConsultaExterna.evolucionConsultaExterna')),
            ],
        ),
        migrations.CreateModel(
            name='refContraRef',
            fields=[
                ('no_control', models.BigAutoField(primary_key=True, serialize=False, verbose_name='No.Control')),
                ('urgencia', models.CharField(max_length=2, verbose_name='Urgencia')),
                ('fecha', models.DateTimeField(auto_now_add=True, verbose_name='Fecha y Hora')),
                ('unidad_a_referir', models.CharField(max_length=60, verbose_name='Unidad a la que se refiere:')),
                ('servicio', models.TextField(verbose_name='Servicio al que se le envia:')),
                ('temperatura', models.IntegerField(verbose_name='Temperatura')),
                ('motivo', models.TextField(verbose_name='Motivo de la Referencia:')),
                ('impresion', models.TextField(verbose_name='Impresion Diagnostica:')),
            ],
        ),
        migrations.CreateModel(
            name='valoracionInicial',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateTimeField(auto_now_add=True, verbose_name='Fecha')),
                ('nombre_paciente_VI', models.CharField(max_length=30, verbose_name='Nombre del Paciente')),
                ('edad', models.IntegerField(verbose_name='Edad')),
                ('nota_medica', models.TextField(null=True, verbose_name='Nota M\xe9dica')),
                ('peso_CE', models.IntegerField(verbose_name='Peso:')),
                ('talla_CE', models.IntegerField(verbose_name='Talla:')),
                ('imc_CE', models.IntegerField(verbose_name='IMC:')),
                ('cintura_CE', models.IntegerField(verbose_name='Cintura:')),
                ('icc_CE', models.IntegerField(verbose_name='ICC:')),
                ('peso_ideal_CE', models.IntegerField(verbose_name='Peso Ideal:')),
                ('fc_CE', models.IntegerField(verbose_name='FC:')),
                ('fr_CE', models.IntegerField(verbose_name='FR:')),
                ('ta_CE1', models.IntegerField(verbose_name='TA:')),
                ('ta_CE2', models.IntegerField(verbose_name='TA:')),
                ('diagnostico_CE', models.TextField(verbose_name='Diagnostico')),
                ('bioquimicos_VI', models.TextField(verbose_name='Bioquimicos de Relevancia')),
                ('plan_CE', models.TextField(verbose_name='Plan')),
                ('consentimiento_info', models.ImageField(blank=True, null=True, upload_to='imagen-consultaE', verbose_name='Consentimiento Informado')),
            ],
        ),
        migrations.AddField(
            model_name='refcontraref',
            name='paciente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ConsultaExterna.valoracionInicial'),
        ),
    ]
