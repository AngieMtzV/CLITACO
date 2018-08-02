 # -*- coding: utf-8 -*-
from __future__ import unicode_literals
from Usuarios.models import Usuario
from django.db import models


#class MedicoExterno(models.Model):
	#externo_imagen = models.ImageField(u'Foto de Perfil', upload_to='imagen-externos', default='us_alumno.png')
	#perfil_externo =models.OneToOneField(User, related_name='user_medico', on_delete=models.CASCADE)	
class valoracionInicial(models.Model):
	usuario = models.ForeignKey(Usuario, related_name='user_externa')
	fecha = models.DateTimeField(u'Fecha', auto_now_add=True)
	nombre_paciente_VI = models.CharField(u'Nombre del Paciente', max_length=30)
	edad = models.IntegerField(u'Edad')
	nota_medica = models.TextField(u'Nota Médica', null=True)
	'''Signos Vitales'''
	peso_CE = models.IntegerField(u'Peso:')
	talla_CE = models.IntegerField(u'Talla:')
	imc_CE = models.IntegerField(u'IMC:')
	cintura_CE = models.IntegerField(u'Cintura:')
	icc_CE = models.IntegerField(u'ICC:')
	peso_ideal_CE = models.IntegerField(u'Peso Ideal:')
	fc_CE = models.IntegerField(u'FC:')
	fr_CE = models.IntegerField(u'FR:')
	ta_CE1 = models.IntegerField(u'TA:')
	ta_CE2 = models.IntegerField(u'TA:')
	diagnostico_CE = models.TextField(u'Diagnostico', null=False)
	bioquimicos_VI = models.TextField(u'Bioquimicos de Relevancia', null=False)
	plan_CE= models.TextField(u'Plan', null=False)
	consentimiento_info = models.ImageField(u'Consentimiento Informado', upload_to='imagen-consultaE', null=True, blank=True)
	def __str__(self):
		return self.nombre_paciente_VI 

class evolucionConsultaExterna(models.Model):
	fecha = models.DateTimeField(u'Fecha', auto_now_add=True)
	signos = models.TextField(u'Signos', null=False)
	valoracion = models.ForeignKey(valoracionInicial)
	def __str__(self):
		return"%s %s" (self.fecha, self.signos)
		
class avanceRapido(models.Model):
	diagnostico_AR = models.TextField(u'Diagnostico', null=False)
	peso_AR = models.IntegerField(u'Peso:')
	talla_AR = models.IntegerField(u'Talla:')
	imc_AR = models.IntegerField(u'IMC:')
	ta_AR1 = models.IntegerField(u'TA:')
	ta_AR2 = models.IntegerField(u'TA:')
	fc_AR = models.IntegerField(u'FC:')
	fr_AR = models.IntegerField(u'FR:')
	bioquimicos_AR = models.TextField(u'Bioquimicos de Relevancia', null=False)
	valoracionInicial = models.ForeignKey(valoracionInicial)
	def __str__(self):
		return"%s %s" (self.diagnostico_AR, self.bioquimicos_AR)

	
class medicoExterno(models.Model):
	imagen_alumno = models.ImageField(u'Foto de Perfil', upload_to='imagen-medicos', default='us_alumno.png')
	user_med = models.OneToOneField(Usuario, related_name='user_med')
	valoraciones_iniciales = models.ForeignKey(valoracionInicial, null=True)
	evoluciones = models.ForeignKey(evolucionConsultaExterna, null=True)
	avances_rapidos = models.ForeignKey(avanceRapido, null=True)

class refContraRef(models.Model):

	no_control = models.BigAutoField(u'No.Control', primary_key=True)
	paciente = models.ForeignKey(valoracionInicial)
	urgencia = models.CharField(u'Urgencia', max_length=2)
	fecha = models.DateTimeField(u'Fecha y Hora', auto_now_add=True)
	unidad_a_referir = models.CharField(u'Unidad a la que se refiere:', max_length=60)
	servicio = models.TextField(u'Servicio al que se le envia:', null=False)
	temperatura = models.IntegerField(u'Temperatura')
	motivo = models.TextField(u'Motivo de la Referencia:', null=False)
	impresion = models.TextField(u'Impresion Diagnostica:', null=False)
	


	









