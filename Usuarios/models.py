# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import AbstractUser

class Usuario(AbstractUser):
	is_medico = models.BooleanField(u'Soy Médico Externo',default=False)
	is_docente = models.BooleanField(u'Soy Docente',default=False)
	is_estudiante = models.BooleanField(u'Soy estudiante',default=False)
	class Meta:
		db_table = 'auth_user'


