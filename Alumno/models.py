# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from Usuarios.models import Usuario
from HistoriaClinica.models import HistoriaClinica, HistoriaClinicaControlado, HistoriaClinicaIntegral

class Semestre(models.Model):
	sem = models.CharField(u'Semestre', max_length=2)
	def __unicode__(self):
		return self.sem

class Grupo(models.Model):
	group= models.CharField(u'Grupo',max_length=1)

	def __unicode__(self):
		return self.group

class Modulo(models.Model):
	modulo = models.CharField(u'Modulo', max_length=150)

	def __unicode__(self):
		return self.modulo

class Turno(models.Model):
	turn = models.CharField(u'Turno', max_length=1)

	def __unicode__(self):
		return self.turn



class PerfilAlumno(models.Model):
	imagen_alumno = models.ImageField(u'Foto de Perfil', upload_to='imagen-alumnos',blank=True)
	perfil =models.ForeignKey(Usuario, related_name='user_alumnol')
	semestre = models.ForeignKey(Semestre)
	grupo = models.ForeignKey(Grupo)
	modulo = models.ForeignKey(Modulo)
	unidad = models.CharField(u'Unidad', max_length=30)
	turno =models.ForeignKey(Turno)

	def __unicode__(self):
		 return unicode(self.perfil)
