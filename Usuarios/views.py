# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from Usuarios.models import Usuario


@login_required
def docente_Medico(request):
	if request.Usuario.is_medico:
		return redirect('medico_index')
		if request.Usuario.is_docente:
			return redirect('docente_index')
	else:
		return redirect('alumno/index')

		return render(request,'docente_index.html')
	return render(request, 'medico_index.html')

	 	
