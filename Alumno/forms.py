from django import forms
from models import PerfilAlumno
from Usuarios.models import Usuario
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm



class AlumnoForm(forms.ModelForm):

	class Meta:
		model = PerfilAlumno 

		fields = (
			'imagen_alumno',
			'semestre',
			'grupo',
			'modulo',
			'unidad',
			'turno',
			)


class RegistroAlumnoForm(UserCreationForm):
	class Meta: 
		model = Usuario

		fields = (
			'username',
			'first_name',
			'last_name',
			'email',
			'is_estudiante',
			'is_medico',
			)

	def save(self,commit=True):
		usuario = super(RegistroAlumnoForm, self).save(commit=False)
		usuario.username = self.cleaned_data['username']
		usuario.first_name = self.cleaned_data['first_name']
		usuario.last_name = self.cleaned_data['last_name']
		usuario.email = self.cleaned_data['email']

		if commit:
			usuario.save()

		return usuario

