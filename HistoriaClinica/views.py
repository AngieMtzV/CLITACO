# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, render_to_response, get_object_or_404
from django.db.models import Q
from django.http import HttpResponse, Http404
from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView
from HistoriaClinica.forms import HistoriaClinica_Form, Historia_Clinica_Controlado, Plan_TratamientoForm, Plan_EjecucionForm, Historia_Clinica_IntegralForm
from HistoriaClinica.models import HistoriaClinica, HistoriaClinicaControlado, PlanTratamiento, PlanEjecucion, HistoriaClinicaIntegral, BaseHistoriaClinica


''' Renderiza el formulario para una nueva Historia Clinica'''
def nueva_historia_clinica(request):
	if not request.user.is_authenticated():
		raise Http404

	if request.method == 'POST':
		form = HistoriaClinica_Form(request.POST)
		if form.is_valid():
			instance = form.save(commit=False)
			instance.usuario = request.user
			instance.save()
			form.save()
		return redirect('listas')
	else:
		form = HistoriaClinica_Form()
	return render(request,'historiaClinica_Form.html',{'form':form})


def historia_clinica_edit(request, pk):
	if not request.user.is_authenticated():
		raise Http404

	urgencia = get_object_or_404(HistoriaClinica, pk=pk)
	if request.method == 'GET':
		form = HistoriaClinica_Form(instance=urgencia)
	else:
		form = HistoriaClinica_Form(request.POST, instance=urgencia)
		if form.is_valid():
			instance = form.save(commit=False)
			instance.usuario = request.user
			instance.save()
			form.save()
		return redirect('listas')
	return render(request, 'historiaClinica_Form.html', {'form':form})



#Método para editar una historia clinica controlada ya creada
def historia_clinica_controlado_edit(request, pk):
	if not request.user.is_authenticated():
		raise Http404

	controlado = get_object_or_404(HistoriaClinicaControlado, pk=pk)
	if request.method == 'GET':
		form = Historia_Clinica_Controlado(instance=controlado)
	else:
		form = Historia_Clinica_Controlado(request.POST, instance=controlado)
		if form.is_valid():
			instance = form.save(commit=False)
			instance.usuario = request.user
			instance.save()
			form.save()	
		return redirect('listas')
	return render(request, 'historiaClinicaControlada_Form.html', {'form':form})

#Método para crear una historia clinica controlada
def nueva_historia_clinica_controlada(request):
	if not request.user.is_authenticated():
		raise Http404
	if request.method == 'POST':
		form = Historia_Clinica_Controlado(request.POST)
		if form.is_valid():
			instance = form.save(commit=False)
			instance.usuario = request.user
			instance.save()
			form.save()
		return redirect('clitaco/listado/historiasClinicas')
	else:
		form = Historia_Clinica_Controlado()
	return render(request,'historiaClinicaControlada_Form.html',{'form':form},)

#Método para crear una historia clinica integral
def nueva_historia_clinica_integral(request):
	if not request.user.is_authenticated():
		raise Http404

	if request.method == 'POST':
		form = Historia_Clinica_IntegralForm(request.POST)
		if form.is_valid():
			instance = form.save(commit=False)
			instance.usuario = request.user
			instance.save()
			form.save()
		return redirect('listas')
	else:
		form = Historia_Clinica_IntegralForm()
	return render(request,'historia_clinica_integral.html',{'form':form})

def historia_clinica_integral_edit(request, pk):
	if not request.user.is_authenticated():
		raise Http404

	integral = get_object_or_404(HistoriaClinicaIntegral, pk=pk)
	if request.method == 'GET':
		form = Historia_Clinica_IntegralForm(instance=integral)
	else:
		form = Historia_Clinica_IntegralForm(request.POST, instance=integral)
		if form.is_valid():
			instance = form.save(commit=False)
			instance.usuario = request.user
			instance.save()
			form.save()	
		return redirect('listas')
	return render(request, 'historia_clinica_integral.html', {'form':form})




''' Muestra todas las historias de todos los usuarios'''
class ListasHistorias(ListView):
    context_object_name = 'listas'
    template_name = 'lista_historias.html'
    queryset = HistoriaClinica.objects.all()

    def get_context_data(self, **kwargs):
        context = super(ListasHistorias, self).get_context_data(**kwargs)
        context['controladas'] = HistoriaClinicaControlado.objects.all()
        context['integrales'] = HistoriaClinicaIntegral.objects.all()
        context['urgencias'] = self.queryset
        return context



class ListasHistoriasPorUser(ListView):
	context_object_name='listas' 
	template_name ='lista_historias.html'


	def get_queryset(self):
		return HistoriaClinica.objects.filter(usuario =self.request.user)

	def get_context_data(self, **kwargs):
		context = super(ListasHistoriasPorUser, self).get_context_data(**kwargs)
		context['controladas'] = HistoriaClinicaControlado.objects.filter(usuario =self.request.user)
		context['integrales'] = HistoriaClinicaIntegral.objects.filter(usuario =self.request.user)
		context['urgencias'] =  HistoriaClinica.objects.filter(usuario =self.request.user)

		return context

	#Metodo para la busqueda de pacientes por CURP
	def busqueda():
		query = request.GET.get("q")
		if query:
			queryset_list = queryset_list.filter(curp__icontains=query)




class Plan_TratamientoHC(CreateView):
	model= PlanTratamiento
	form_class = Plan_TratamientoForm
	template_name= 'plan_actividades.html'
	success_url = reverse_lazy('plan-ejecucion')

class Plan_EjecucionHC(CreateView):
	model= PlanEjecucion
	form_class = Plan_EjecucionForm
	template_name= 'plan-ejecucion.html'
	success_url = '/clitaco/historiaClinica/planejecucion'
	queryset= PlanEjecucion.objects.all()		

	def get_context_data (self, **kwargs):
		context =super(Plan_EjecucionHC, self).get_context_data(**kwargs)
		context['listaactividades'] =self.queryset
		return context



