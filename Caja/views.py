# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse_lazy
from django.views.generic import CreateView
from Caja.models import Venta
from Caja.forms import Venta_Form



class CajaClitaco(CreateView):
	model= Venta
	form_class = Venta_Form
	template_name= 'caja_clitaco.html'
	success_url = reverse_lazy('caja')
	queryset = Venta.objects.all()

	def get_context_data (self, **kwargs):
		context =super(CajaClitaco, self).get_context_data(**kwargs)
		context['ventas'] =self.queryset
		return context