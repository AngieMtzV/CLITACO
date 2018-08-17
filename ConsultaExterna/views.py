# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponseRedirect
from django.views.generic import  CreateView, ListView, DetailView, UpdateView
from ConsultaExterna.forms import  ValoracionInicialForm, AvanceRapidoForm, EvolConsultaExterna, ValoracionEditForm, ReferenciaForm
from ConsultaExterna.models import valoracionInicial, evolucionConsultaExterna, avanceRapido, refContraRef


class ValoracionInicialCreate(CreateView):
	model= valoracionInicial
	form_class = ValoracionInicialForm
	template_name= 'valoracion_inicial.html'
	success_url = reverse_lazy('listas_externa')

	def form_valid(self, form):
	 instance = form.save(commit = False)
	 instance.usuario = self.request.user
	 return super(ValoracionInicialCreate, self).form_valid(form)


class ListaConsultaExterna(ListView):
	context_object_name='listas_externa' 
	template_name ='lista_externas.html'

	def get_queryset(self):
		return valoracionInicial.objects.filter(usuario =self.request.user)

	def get_context_data(self, **kwargs):
		context = super(ListaConsultaExterna, self).get_context_data(**kwargs)
		context['externas'] = valoracionInicial.objects.filter(usuario =self.request.user)

		return context

class TablaEvolucion(CreateView):
	model= evolucionConsultaExterna
	form_class = EvolConsultaExterna
	template_name= 'evolucion_consulta.html'
	success_url = 'evolucion'
	queryset= evolucionConsultaExterna.objects.all()

	def get_context_data(self, **kwargs):
		context =super(TablaEvolucion, self).get_context_data(**kwargs)
		context['evoluciones'] =self.queryset
		return context

	def form_valid(self, form):
		valoracion = get_object_or_404(valoracionInicial, pk=self.kwargs['pk'])
		form.instance.valoracion = valoracion
		return super(TablaEvolucion, self).form_valid(form)
		
class CuadroAvanceRapido(CreateView):
	model= avanceRapido
	form_class = AvanceRapidoForm
	template_name= 'avance_rapido.html'
	success_url = 'avance_rapido'
	queryset= avanceRapido.objects.all()		

	def get_context_data (self, **kwargs):
		context =super(CuadroAvanceRapido, self).get_context_data(**kwargs)
		context['avances'] =self.queryset
		return context

class DetallesConsultaExterna(DetailView):
	model = valoracionInicial
	template_name= 'externa_detalles.html' 

class DetallesReferencia(DetailView):
	model = refContraRef
	template_name = 'referencia_detalles.html'

class ValoracionEdit(UpdateView):
	form_class = ValoracionEditForm
	template_name = 'valoracion_edit.html'
	success_url = reverse_lazy('listas_externa') 

class ReferenciaContraReferencia(CreateView):
	model = refContraRef
	form_class = ReferenciaForm
	template_name = 'referencia.html'
	success_url =reverse_lazy('listas_externa')

	def get_context_data(self, **kwargs):
		paciente = get_object_or_404(valoracionInicial, pk=self.kwargs['pk'])
		kwargs['paciente']= paciente
		return super(ReferenciaContraReferencia, self).get_context_data(**kwargs)

	def form_valid(self, form):
		paciente = get_object_or_404(valoracionInicial, pk=self.kwargs['pk'])
		form.instance.paciente = paciente
		return super(ReferenciaContraReferencia, self).form_valid(form)





#Agregar busqueda de por curp para pacientes recurrentes y no recurrentes