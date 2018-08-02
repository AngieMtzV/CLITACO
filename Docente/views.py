# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from Docente.models import DocenteAlumno
from Docente.forms import FormularioDocenteForm
from django.core.urlresolvers import reverse_lazy
from django.views.generic import CreateView
from django.shortcuts import render

class AlumnoSeguimiento(CreateView):
	model= DocenteAlumno
	form_class = FormularioDocenteForm
	template_name= 'docente_alumno.html'
	success_url = reverse_lazy('seguimiento_alumnos')


