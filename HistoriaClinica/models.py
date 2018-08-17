# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from Usuarios.models import Usuario
from django.db import models 

class Civil(models.Model):
	estado= models.CharField(u'Estado Civil', max_length=25)
	def __unicode__(self):
		return self.estado

class Estado(models.Model):
	estado_estado= models.CharField(u'Estado del Paciente', max_length=30)
	def __unicode__(self):
		return self.estado_estado

class Sexo(models.Model):
	sex= models.CharField(u'Sexo', max_length=15)
	def __unicode__(self):
		return self.sex

class TipoInterrogatorio(models.Model):
	inte= models.CharField(u'Interrogatorio', max_length=15)
	def __unicode__(self):
		return self.inte

class TipoCraneo(models.Model):
	craneo = models.CharField(u'Tipo de Craneo', max_length=13)
	def __unicode__(self):
		return self.craneo

class Perfil(models.Model):
	perfil_cabeza = models.CharField(u'Perfil', max_length=13)
	def __unicode__(self):
		return self.perfil_cabeza

class PlanTratamiento(models.Model):
	fecha = models.DateTimeField(u'Fecha', auto_now_add=True)
	actividades = models.TextField(u'Lista de Actividades',null=False, default='')
	autorizacion = models.BooleanField(u'Autorizado', default = False)

class PlanEjecucion(models.Model):
	cita = models.IntegerField(u'Cita', default=1)
	fecha= models.DateField(u'Fecha',auto_now= False)
	act= models.TextField(u'Actividades', default='')
	vo_bo= models.CharField(u'Vo. Bo', default='', max_length=15)


class BaseHistoriaClinica(models.Model):
	folio = models.BigAutoField(u'Folio', primary_key=True)
	fecha = models.DateTimeField(u'Fecha', auto_now_add=True)
	nommbre_paciente = models.CharField(u'Nombre del Paciente', max_length=50)
	edad = models.IntegerField(u'Edad')
	Sexo = models.ForeignKey(Sexo)
	Estado_Civil = models.ForeignKey(Civil)
	Tel = models.CharField(u'Telefono', max_length=15)
	Ocupacion = models.CharField(u'Ocupacion', max_length=25)
	Domicilio = models.CharField(u'Domicilio', max_length=255)
	curp = models.CharField(u'CURP', max_length=18, unique=True)
	estado = models.ForeignKey(Estado)
	

	class Meta:
		abstract = True


class HistoriaClinica(BaseHistoriaClinica):
	'''Urgencia'''
	Motivo_Consulta = models.TextField(u'Motivo de Consulta',null = True)
	Signos_Sintomas = models.TextField(u'Signos y Sintomas que refiere el Paciente', null = True)
	Ante_Pato = models.TextField(u'Antecedentes no Patologicos', null = True)
	ultimos_meses = models.BooleanField(u'¿Ha recibido Atencion Odontologica en los ultimos 3 meses?', default=False)
	tipo_atencion = models.TextField(u'¿De que tipo?', null = True)
	alergico = models.BooleanField(u'¿Es alergico a Farmacos y/o Alimentos', default=False)
	tipo_alergia = models.TextField(u'¿Cual tipo de alergia?', null = True)
	cardio = models.BooleanField(u'Cardiopatias', default=False)
	diabetes = models.BooleanField(u'Diabetes', default=False)
	hipertencion = models.BooleanField(U'Hipertencion', default=False)
	otras_enfermedades = models.TextField(u'Otras:', null= True)
	medicamentos = models.BooleanField(U'¿Actualmente está tomando algún medicamento?', default=False)
	medi_cual =models.TextField(u'¿Cual(es)?', null = True)
	medi_motivo = models.TextField(u'Motivo', null = True)
	t_arterial = models.IntegerField(u'T.Arterial', default=0)
	pulso = models.IntegerField(u'Pulso', default=0)
	temperatura = models.IntegerField(u'Temperatura(Grados Celsius', default=0)
	f_respiratoria = models.IntegerField(u'Frecuencia Respiratoria', default=0)
	peso = models.DecimalField(u'Peso(Kg)', max_digits=5, decimal_places =3, default=0.0)
	talla = models.IntegerField(u'Talla', default=0)
	hallazgo_dientes = models.TextField(u'Dientes', null= False, default='No registrado', editable=True)
	hallazgo_tejidos = models.TextField(u'Tejidos Blandos', null= False, default='No registrado', editable=True)
	hallazgo_piel_an = models.TextField(u'Piel y Anexos', null= False, default='No registrado', editable=True)
	radiografico = models.BooleanField(u'Radiografico', default=False)
	#Aqui va la opcion de tipo de radiografico [radiobuttons]
	interpretacion_radio = models.TextField(u'Interpretacion Radiografica', blank= True)
	diagnostico = models.TextField(u'Diagnostico', null= False, default= 'No se Agrego aún un diagnostico', editable= True)
	pronostico = models.TextField(u'Pronostico', null=False, default='No registrado', editable=True)
	tratamiento_seguimiento = models.TextField(u'Tratamiento que se propone y secuencia del mismo', null=False, default='No registrado', editable=True)
	costo = models.IntegerField(u'Costo del Tratamiento', null=False, default= 0)
	aut_docente = models.BooleanField(u'Autorización del Docente', default=False)
	descrip_act = models.TextField(u'Descripcion de Actividad', null=True)
	descrip_notas = models.TextField(u'Descripción de Notas de Actividades', null= True)
	usuario = models.ForeignKey(Usuario, related_name='user_urgencia')

	def __unicode__(self):
		return self.nommbre_paciente


class HistoriaClinicaControlado(BaseHistoriaClinica):

	padecimiento = models.TextField(u'Padecimiento Actual',null = False,default='No registrado', editable=True)
	
	antecedentes = models.TextField(u'Antecedentes Heredo Familiares',null = False, default='No registrado', editable=True)
	''' Bloque III Antecedentes personales no patologicos'''
	np_domiciliarios = models.TextField(u'Servicios Domiciliarios', null = False, default='No registrado', editable=True)
	np_higiene_vivienda = models.TextField(u'Higiene de Vivienda', null = True)
	np_higiene_personal = models.TextField(u'Higiene Personal', null= True)
	np_higiene_bucal = models.TextField(u'Higiene Bucal', null = False, default='No registrado', editable=True)
	np_alimentacion = models.TextField(u'Alimentacion', null=False,default='No registrado', editable=True)
	#Grupo Sanguineo
	#RH
	inmunizaciones = models.CharField(u'Inmunizaciones', max_length=50)
	'''Bloque IV Antecedentes Personales Patologicos'''
	pp_nutricionales = models.TextField(u'Nutricionales', null=False,default='No registrado', editable=True)
	pp_cardiacos = models.TextField(u'Cardiacos', null=False, default='No registrado', editable=True)
	pp_hepaticos = models.TextField(u'Hepaticos', null=False, default='No registrado', editable=True)
	pp_trans_sexual = models.TextField(u'Enfermedades de Transmision Sexual(SIDA)', null=False, default='No registrado', editable=True)
	''' Antecedentes Alergicos'''
	aa_medicamentos = models.BooleanField(u'Medicamentos', default=False)
	cuales_medicamentos =  models.TextField(u'¿Cual(es)?', null= True)
	aa_alimentos = models.BooleanField(u'Alimentos', default=False)
	cuales_alimentos =  models.TextField(u'¿Cual(es)?', null= True)
	aa_entorno = models.BooleanField(u'Al Entorno Ambiental', default=False)
	anestesia = models.BooleanField(u'¿Le han administrado anestesia general y/o local', default=False)
	anestesia_especificacion = models.TextField(u'Especifique', null= True) 
	reaccion_adversa = models.BooleanField(u'¿Tuvo alguna reaccion adversa', default=False)
	reaccion_especificacion = models.TextField(u'Especifique', null= True)
	#Adicciones
	''' Antecedentes Medicos y Quirurgicos'''
	ultimos_meses_medicos = models.BooleanField(u'¿Ha estado sometico a tratamiento medico en los ultimos 2 meses?', default=False)
	motivo_medicos = models.TextField(u'Motivo', null= True) 
	ultimos_meses_hospi = models.BooleanField(u'¿Ha sido hospitalizado en los ultimos 2 meses?', default=False)
	motivo_hospi = models.TextField(u'Motivo', null= True) 
	tomando_medicamento = models.BooleanField(u'¿Está tomando actualmente algun medicamento?', default=False)
	medi_cuales = models.TextField(u'¿Cual(es)?', null= True) 
	medi_motivo = models.TextField(u'Motivo', null= True) 
	'''Antecedentes Hemorragicos'''
	trans_sangre = models.BooleanField(u'¿Le han transfundido sangre o algun derivado de la misma?', default=False)
	tras_sangre_motivo = models.TextField(u'Motivo', null= True)
	trans_sangre_fecha = models.DateField(u'Fecha')
	'''Antecedentes Gineco-Hemorragicos (Si es Mujer)'''
	num_embarazos = models.IntegerField(u'No. de Embarazos', null=True)
	num_partos = models.IntegerField(u'No. de Partos', null=True)
	cesareas = models.IntegerField(u'Cesareas', null=True)
	abortos = models.IntegerField(u'Abortos', null=True)
	complicaciones = models.TextField(u'Complicaciones', null= True) 
	'''Interrogatorio por aparatos y sistemas'''
	inter_digestivo = models.TextField(u'Digestivo', null= False, default='No registrado', editable=True)
	inter_respiratorio = models.TextField(u'Respiratorio', null= False, default='No registrado', editable=True)
	inter_cardio = models.TextField(u'Cardiovascular', null= False, default='No registrado', editable=True)
	inter_geni = models.TextField(u'Genitourinario', null= False, default='No registrado', editable=True)
	inter_endo = models.TextField(u'Endocrino', null= False, default='No registrado', editable=True)
	inter_tegu = models.TextField(u'Tegumentario', null= False, default='No registrado', editable=True)
	inter_mus_esque = models.TextField(u'Musculo-Esqueletico', null= False, default='No registrado', editable=True)
	inter_nervioso = models.TextField(u'Nervioso', null= False, default='No registrado', editable=True)
	'''Exploracion Fisica'''
	peso = models.IntegerField(u'Peso', default=50)
	pulso = models.IntegerField(u'Pulso', default= 100)
	#P.A
	frec_cardiaca =models.IntegerField(u'F.C', default= 100)
	frec_resp =models.IntegerField(u'F.R', default= 15)
	temperatura = models.IntegerField(u'Temperatura(Grados Celsius)', default=0)
	talla = models.DecimalField(u'Talla',max_digits=3, decimal_places =2, default=0.0 )
	i_m_c = models.DecimalField(u'I.M.C',max_digits=4, decimal_places =2, default=0.0, editable=False )
	'''EXAMEN DE CABEZA'''
	tipo_craneo = models.ForeignKey(TipoCraneo, default='')
	cabeza_perfil = models.ForeignKey(Perfil, default='')
	cara = models.TextField(u'Cara',null = False, default= 'No registrado')
	'''ARTICULACION CRANEOMANDIBULAR'''
	dolor_masticar = models.BooleanField(u'Dolor al masticar o al hablar', default= False)
	dm_tipo = models.TextField(u'Tipo', null =False, default= 'No registrado')
	dm_duracion= models.IntegerField(u'Duración', default=0)
	dificultad_hablar = models.BooleanField(u'Dificultad al masticar o al hablar', default= False)
	dh_motivo = models.TextField(u'Motivo', null =True)
	ruido_abertura = models.BooleanField(u'Ruido Articular a la Abertura', default=False)
	ruido_cierre = models.BooleanField(u'Ruido Articular al Cierre', default=False)
	patron_recto = models.IntegerField(u'Recto', default=0) #Especificar
	otras_observaciones = models.TextField(u'Otras Observaciones', null= True)
	labios = models.TextField(u'Labios', null=False, default= 'No registrado')
	'''CUELLO'''
	ganglios= models.TextField(u'Ganglios', null=False, default='')
	cervicales= models.TextField(u'Cervicales', null=False, default='')
	submaxilares= models.TextField(u'Submaxilares', null=False, default='')
	submentonianos= models.TextField(u'Submentonianos', null=False, default='')
	parotideos= models.TextField(u'Parotideos', null=False, default='')
	preauriculares= models.TextField(u'Preauriculares', null=False, default='')
	auriculares_post= models.TextField(u'Auriculares Post', null=False, default='')
	'''VII EXAMEN INTRABUCAL'''
	mucosas= models.TextField(u'Mucosas', null=False, default='')
	mejillas= models.TextField(u'Mejillas', null=False, default='')	
	lengua= models.TextField(u'Lengua', null=False, default='')
	piso_boca= models.TextField(u'Piso de Boca', null=False, default='')
	region_retromolar= models.TextField(u'Retromolar', null=False, default='')
	paladar= models.TextField(u'Paladar', null=False, default='')
	orofaringe= models.TextField(u'Orofaringe', null=False, default='')
	encias= models.TextField(u'Encias', null=False, default='')
	itsmo_fauces= models.TextField(u'Ismo de las Fauces', null=False, default='')
	'''VIII GLANDULAS SALIVALES'''
	g_parotidas = models.TextField(u'Parotidas', null=False, default='')
	g_submaximales = models.TextField(u'Maximales', null=False, default='')
	g_sublinguales = models.TextField(u'Parotidas', null=False, default='')
	usuario = models.ForeignKey(Usuario, related_name='user_controlado')
	

	def __unicode__(self):
		return self.nommbre_paciente



class HistoriaClinicaIntegral(BaseHistoriaClinica):

	ipadecimiento = models.TextField(u'Padecimiento Actual',null = False,default='No registrado', editable=True)
	
	iantecedentes = models.TextField(u'Antecedentes Heredo Familiares',null = False, default='No registrado', editable=True)
	''' Bloque III Antecedentes personales no patologicos'''
	inp_domiciliarios = models.TextField(u'Servicios Domiciliarios', null = False, default='No registrado', editable=True)
	inp_higiene_vivienda = models.TextField(u'Higiene de Vivienda', null = True)
	inp_higiene_personal = models.TextField(u'Higiene Personal', null= True)
	inp_higiene_bucal = models.TextField(u'Higiene Bucal', null = False, default='No registrado', editable=True)
	inp_alimentacion = models.TextField(u'Alimentacion', null=False,default='No registrado', editable=True)
	#Grupo Sanguineo
	#RH
	iinmunizaciones = models.CharField(u'Inmunizaciones', max_length=50)
	'''Bloque IV Antecedentes Personales Patologicos'''
	ipp_nutricionales = models.TextField(u'Nutricionales', null=False,default='No registrado', editable=True)
	ipp_cardiacos = models.TextField(u'Cardiacos', null=False, default='No registrado', editable=True)
	ipp_hepaticos = models.TextField(u'Hepaticos', null=False, default='No registrado', editable=True)
	ipp_trans_sexual = models.TextField(u'Enfermedades de Transmision Sexual(SIDA)', null=False, default='No registrado', editable=True)
	''' Antecedentes Alergicos'''
	iaa_medicamentos = models.BooleanField(u'Medicamentos', default=False)
	icuales_medicamentos =  models.TextField(u'¿Cual(es)?', null= True)
	iaa_alimentos = models.BooleanField(u'Alimentos', default=False)
	icuales_alimentos =  models.TextField(u'¿Cual(es)?', null= True)
	iaa_entorno = models.BooleanField(u'Al Entorno Ambiental', default=False)
	ianestesia = models.BooleanField(u'¿Le han administrado anestesia general y/o local', default=False)
	ianestesia_especificacion = models.TextField(u'Especifique', null= True) 
	ireaccion_adversa = models.BooleanField(u'¿Tuvo alguna reaccion adversa', default=False)
	ireaccion_especificacion = models.TextField(u'Especifique', null= True)
	#Adicciones
	''' Antecedentes Medicos y Quirurgicos'''
	iultimos_meses_medicos = models.BooleanField(u'¿Ha estado sometico a tratamiento medico en los ultimos 2 meses?', default=False)
	imotivo_medicos = models.TextField(u'Motivo', null= True) 
	iultimos_meses_hospi = models.BooleanField(u'¿Ha sido hospitalizado en los ultimos 2 meses?', default=False)
	imotivo_hospi = models.TextField(u'Motivo', null= True) 
	itomando_medicamento = models.BooleanField(u'¿Está tomando actualmente algun medicamento?', default=False)
	imedi_cuales = models.TextField(u'¿Cual(es)?', null= True) 
	imedi_motivo = models.TextField(u'Motivo', null= True) 
	'''Antecedentes Hemorragicos'''
	itrans_sangre = models.BooleanField(u'¿Le han transfundido sangre o algun derivado de la misma?', default=False)
	itras_sangre_motivo = models.TextField(u'Motivo', null= True)
	itrans_sangre_fecha = models.DateField(u'Fecha')
	'''Antecedentes Gineco-Hemorragicos (Si es Mujer)'''
	inum_embarazos = models.IntegerField(u'No. de Embarazos', null=True)
	inum_partos = models.IntegerField(u'No. de Partos', null=True)
	icesareas = models.IntegerField(u'Cesareas', null=True)
	iabortos = models.IntegerField(u'Abortos', null=True)
	icomplicaciones = models.TextField(u'Complicaciones', null= True) 
	'''Interrogatorio por aparatos y sistemas'''
	iinter_digestivo = models.TextField(u'Digestivo', null= False, default='No registrado', editable=True)
	iinter_respiratorio = models.TextField(u'Respiratorio', null= False, default='No registrado', editable=True)
	iinter_cardio = models.TextField(u'Cardiovascular', null= False, default='No registrado', editable=True)
	iinter_geni = models.TextField(u'Genitourinario', null= False, default='No registrado', editable=True)
	iinter_endo = models.TextField(u'Endocrino', null= False, default='No registrado', editable=True)
	iinter_tegu = models.TextField(u'Tegumentario', null= False, default='No registrado', editable=True)
	iinter_mus_esque = models.TextField(u'Musculo-Esqueletico', null= False, default='No registrado', editable=True)
	iinter_nervioso = models.TextField(u'Nervioso', null= False, default='No registrado', editable=True)
	'''Exploracion Fisica'''
	ipeso = models.DecimalField(u'Peso', default=50.5, max_digits=2, decimal_places =2)
	ipulso = models.IntegerField(u'Pulso', default= 100)
	#P.A
	ifrec_cardiaca =models.IntegerField(u'F.C', default= 100)
	ifrec_resp =models.IntegerField(u'F.R', default= 15)
	itemperatura = models.IntegerField(u'Temperatura(Grados Celsius)', default=0)
	italla = models.DecimalField(u'Talla',max_digits=5, decimal_places =2, default=1.80 )
	'''EXAMEN DE CABEZA'''
	itipo_craneo = models.ForeignKey(TipoCraneo, default='')
	icabeza_perfil = models.ForeignKey(Perfil, default='')
	icara = models.TextField(u'Cara',null = False, default= 'No registrado')
	'''ARTICULACION CRANEOMANDIBULAR'''
	idolor_masticar = models.BooleanField(u'Dolor al masticar o al hablar', default= False)
	idm_tipo = models.TextField(u'Tipo', null =False, default= 'No registrado')
	idm_duracion= models.IntegerField(u'Duración', default=0)
	idificultad_hablar = models.BooleanField(u'Dificultad al masticar o al hablar', default= False)
	idh_motivo = models.TextField(u'Motivo', null =True)
	iruido_abertura = models.BooleanField(u'Ruido Articular a la Abertura', default=False)
	iruido_cierre = models.BooleanField(u'Ruido Articular al Cierre', default=False)
	ipatron_recto = models.IntegerField(u'Recto', default=0) #Especificar
	iotras_observaciones = models.TextField(u'Otras Observaciones', null= True)
	ilabios = models.TextField(u'Labios', null=False, default= 'No registrado')
	'''CUELLO'''
	iganglios= models.TextField(u'Ganglios', null=False, default='')
	icervicales= models.TextField(u'Cervicales', null=False, default='')
	isubmaxilares= models.TextField(u'Submaxilares', null=False, default='')
	isubmentonianos= models.TextField(u'Submentonianos', null=False, default='')
	iparotideos= models.TextField(u'Parotideos', null=False, default='')
	ipreauriculares= models.TextField(u'Preauriculares', null=False, default='')
	iauriculares_post= models.TextField(u'Auriculares Post', null=False, default='')
	'''VII EXAMEN INTRABUCAL'''
	imucosas= models.TextField(u'Mucosas', null=False, default='')
	imejillas= models.TextField(u'Mejillas', null=False, default='')	
	ilengua= models.TextField(u'Lengua', null=False, default='')
	ipiso_boca= models.TextField(u'Piso de Boca', null=False, default='')
	iregion_retromolar= models.TextField(u'Retromolar', null=False, default='')
	ipaladar= models.TextField(u'Paladar', null=False, default='')
	iorofaringe= models.TextField(u'Orofaringe', null=False, default='')
	iencias= models.TextField(u'Encias', null=False, default='')
	iitsmo_fauces= models.TextField(u'Ismo de las Fauces', null=False, default='')
	'''VIII GLANDULAS SALIVALES'''
	ig_parotidas = models.TextField(u'Parotidas', null=False, default='')
	ig_submaximales = models.TextField(u'Maximales', null=False, default='')
	ig_sublinguales = models.TextField(u'Parotidas', null=False, default='')
	usuario = models.ForeignKey(Usuario, related_name='user_integral')

	def calcular_i_m_c(self):
		return self.italla*self.italla/ self.ipeso
	
	

	def __unicode__(self):
		return self.nommbre_paciente

		

	




	