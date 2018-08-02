# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import AbstractUser

class Usuario(AbstractUser):
	is_medico = models.BooleanField(default=False)
	is_docente = models.BooleanField(default=False)
	class Meta:
		db_table = 'auth_user'


