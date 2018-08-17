# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from django.views.generic import ListView
from forms import MaterialForm
from models import MaterialEnfermeria

#Método para crear un objeto de material por día
def material_view(request):
	
	if not request.user.is_authenticated():
		raise Http404

	if request.method == 'POST':
		form = MaterialForm(request.POST)
		if form.is_valid():
			instance = form.save(commit=False)
			instance.usuario_material = request.user
			instance.save()
			form.save()
		return redirect('material_lista')
	else:
		form = MaterialForm()
	return render(request,'materialnuevo_form.html',{'form':form})

class ListaMaterial(ListView):
    context_object_name = 'material_lista'
    template_name = 'lista_material.html'

    def get_queryset(self):
    	return MaterialEnfermeria.objects.filter(usuario_material =self.request.user)

	def get_context_data(self, **kwargs):
		context = super(ListaMaterial,  self).get_context_data(**kwargs)
		context['materiales'] = MaterialEnfermeria.objects.filter(usuario_material =self.request.user)
		
		return context