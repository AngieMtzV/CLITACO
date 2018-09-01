# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from Alumno.models import PerfilAlumno
from Usuarios.models import Usuario
from django.db import models

class DocenteAlumno(models.Model):

	alumno = models.ForeignKey(PerfilAlumno)
	dias = models.IntegerField(u'Días de Trabajo', default=0)
	asistencia = models.IntegerField(u'Asistencia', default=0)
	calificacion = models.IntegerField(u'Calificacion', default=0)



class PerfilDocente(models.Model):
	imagen_docente = models.ImageField(u'Foto de Perfil', upload_to='imagen-docente', default='us_alumno.png')
	perfil_docente =models.ForeignKey(Usuario, related_name='user_docente')

	def __unicode__(self):
		return unicode(self.perfil_docente)

