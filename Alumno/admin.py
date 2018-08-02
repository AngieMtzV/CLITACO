# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from Alumno.models import PerfilAlumno,Semestre,Grupo,Modulo ,Turno

admin.site.register(PerfilAlumno)
admin.site.register(Semestre)
admin.site.register(Grupo)
admin.site.register(Modulo)
admin.site.register(Turno)



