# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponse, Http404
from django.views.generic import CreateView, DetailView, TemplateView
from Usuarios.models import Usuario

from Alumno.forms import AlumnoForm, RegistroAlumnoForm
from HistoriaClinica.models import HistoriaClinica
from Alumno.models import PerfilAlumno
#from weasyprint import HTML
from django.template.loader import render_to_string, get_template
from django.core.files.storage import FileSystemStorage
import tempfile
#from django_weasyprint import WeasyTemplateResponseMixin

def error_404(request):
	data = {}
	return render(request,'alumno/perfil/404_perfil.html', data)

def index(request):
	return render(request,'index.html')

''' Renderiza el formulario de Registro del Alumno como Usuario
def alumno(request):
	if request.method == 'POST':
		user_form = RegistroAlumnoForm(request.POST)
		if user_form.is_valid():
			usuario = user_form.save()
		return redirect('index')
	else:
		user_form = RegistroAlumnoForm(request.POST)
		return render(request,'alumno_form.html',{'user_form':user_form})'''

class RegistroAlumno(CreateView):
	model=Usuario
	template_name='alumno_form.html'
	form_class = RegistroAlumnoForm
	success_url = reverse_lazy('alumno_index')


'''Renderiza la información de la clinica'''
def info_clitaco(request):
	return render(request,'info.html')

"""def genera_pdf(request):
	#Modelo de datos
	pacientes_urgencia = HistoriaClinica.objects.all()
	#Renderizar
	html_string =  render_to_string('pdf_alumno.html',{'pacientes_urgencia':pacientes_urgencia})
	html = HTML(string=html_string)
	'''result = html.write_pdf()

	response = HttpResponse(content_type='application/pdf;')
	response['Content-Disposition'] = 'inline; filename= informacion_alumno'
	response['Content-Transfer-Encoding'] = 'binary'
	with tempfile.NamedTemporaryFile( delete=True) as output:
		output.write(result)
		output.flush()
		output2 =output.name
		response.write(output2)'''
	html.write_pdf(target='C:/Users/angie/AppData/Local/Temp/pdf_alumno.pdf')
	fs = FileSystemStorage('C:/Users/angie/AppData/Local/Temp')
	with fs.open('pdf_alumno.pdf') as pdf:
		response =HttpResponse(pdf,content_type='application/pdf')
		response['Content-Disposition'] = 'attachment; filename="pdf_alumno.pdf"'
		return response
	
	return response"""
	#Agregar el turno del alumno, y la localidad del paciente y sexo
class Perfil(CreateView):
	model=PerfilAlumno
	template_name='perfil_form.html'
	form_class = AlumnoForm
	success_url = reverse_lazy('alumno_index')

	def form_valid(self, form):
		form.instance.perfil = self.request.user
		return super(Perfil, self).form_valid(form)


class AlumnoPerfil(DetailView):
	model = PerfilAlumno
	template_name= 'ver_perfil.html' 

	def get(self, request, *args, **kwargs):
		try:
			self.object = self.get_object()
		except Http404:
			return redirect('404_perfil')
		context = self.get_context_data(object=self.object)
		return self.render_to_response(context)

def view404perfil(request):
	return render(request,'404_perfil.html')

