# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from Docente.models import DocenteAlumno, PerfilDocente
from Alumno.models import PerfilAlumno
from HistoriaClinica.models import HistoriaClinica, HistoriaClinicaControlado, HistoriaClinicaIntegral
from Docente.forms import FormularioDocenteForm, DocenteForm
from django.core.urlresolvers import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView
from django.shortcuts import render, get_object_or_404

class AlumnoSeguimiento(CreateView):
	model= DocenteAlumno
	form_class = FormularioDocenteForm
	template_name= 'docente_alumno.html'
	success_url = reverse_lazy('tabla_alumnos')

	def form_valid(self, form):
		alumno = get_object_or_404(PerfilAlumno, pk=self.kwargs['pk'])
		form.instance.alumno = alumno
		return super(AlumnoSeguimiento, self).form_valid(form)



class ListAlumnosDocente(ListView):
	context_object_name = 'tabla_alumnos'
	template_name = 'alumnos_calificacion.html'
	queryset = PerfilAlumno.objects.all()

	def get_context_data(self, **kwargs):
		context = super(ListAlumnosDocente, self).get_context_data(**kwargs)
		context['alumnos'] = self.queryset
		return context

class ListasHistorias(ListView):
    context_object_name = 'historias_docente'
    template_name = 'historias_docente.html'
    queryset = HistoriaClinica.objects.all()

    def get_context_data(self, **kwargs):
        context = super(ListasHistorias, self).get_context_data(**kwargs)
        context['controladas'] = HistoriaClinicaControlado.objects.all()
        context['integrales'] = HistoriaClinicaIntegral.objects.all()
        context['urgencias'] = self.queryset
        return context

class UrgenciaDetalle(DetailView):
	model = HistoriaClinica
	template_name= 'ver_urgencia.html' 