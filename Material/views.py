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
		return redirect('material_listas')
	else:
		form = MaterialForm()
	return render(request,'materialnuevo_form.html',{'form':form})

class ListaMaterial(ListView):
    context_object_name = 'material_listas'
    template_name = 'lista_material.html'
    queryset = MaterialEnfermeria.objects.all()