# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class TipoProducto(models.Model):
	tipos= models.CharField(u'Tipo', max_length=25)
	def __unicode__(self):
		return self.tipos


class ProductoClinica(models.Model):
	nombre = models.CharField(u'Nombre', max_length=40)
	tipo = models.ForeignKey(TipoProducto)
	precio = models.IntegerField(u'Precio', default=0)
	def __unicode__(self):
		return self.nombre

class Venta(models.Model):
	folio = models.BigAutoField(u'Folio', primary_key=True)
	fecha =models.DateTimeField(u'Fecha', auto_now_add=True)
	productos = models.ForeignKey(ProductoClinica)


class Caja(models.Model):
	ventas =  models.ForeignKey(Venta)
	



	'''
	CONSULTA_DENTAL = models.IntegerField(u'Consulta Dental')
	CONSULTA_MEDICA = models.IntegerField(u'ConsultaMediaEjemplo')
	RX_PERIAPICAL = models.IntegerField(u'RX PERIPICAL(Adulto, Infantil)')
	RX_OCLUSAL = models.IntegerField(u'RX OCLUSAL')
	ORTO_CD_IMPRESA = models.IntegerField(u'Ortopantomografia + CD e Impresa')
	RX_LATERAL_CRANEO = models.IntegerField(u'RX Lateral de Cráneo + CD')
	PRUEBA_GLUCOSA = models.IntegerField(u'Pruba de Glucosa')
	MODELOS_ESTUDIO = models.IntegerField(u'Modelos de Estudio')
	PAQUETE_BARRERAS = models.IntegerField(u'Paquete de Barreras de Protección')
	
	CEMENTACION= models.IntegerField(u'Cementación y/o reconstrucción c/ionomero de Vidrio por pilar')
	CURACION_ALVEOLITIS = models.IntegerField(u'Curación de Alveolitis')
	DRENADO_ABCESO = models.IntegerField('Drenadp de Abceso')
	VACIAMIENTO_PULPAR = models.IntegerField(u'Vaciamiento Pulpar')
	FERULIZACION_RESINA = models.IntegerField(u'Ferulización con Resina por Diente') 
	'''
	'''Tratamientos de Prevención
	AP_FLUORURO = models.IntegerField(u'Aplicación de Fluoruro(cada ocasión)')
	DETRA_CAVITRON = models.IntegerField(u'Detrartraje por Cavitrón(por arcada)')
	DETRA_CURETA = models.IntegerField(u'Detrartraje y Cureta Manual(por arcada)')
	DESGASTE = models.IntegerField(u'Desgaste selectivo por Unidad')
	PRO_SUP = models.IntegerField(u'Profilaxis Superficial')
	SELLADOR = models.IntegerField(u'Selladores de Fosetas y Fisuras(por diente)')
	'''
	'''Tratamiento de Exodoncia
	EX_SIMPLE = models.IntegerField(u'Extracción Simple')
	EX_3_MOLAR = models.IntegerField(u'Extracción de 3RA Molar Erupcionada')
	EX_MUL_4 = models.IntegerField(u'Extracciones Multiples Más de 4 (por cuadrante)')
	EX_COM = models.IntegerField(u'Extracción Complicada')
	'''
	'''Cirugía
	DIENTES_RET = models.IntegerField(u'Dientes Retenidos')
	ALV_ARCADA = models.IntegerField(u'Alveoloplastia por Arcada(con o sin extracción)+Paquete')
	API_PAQUETE = models.IntegerField(u'Apicectomia + Paquete')
	FRENILEVTOMIA = models.IntegerField(u'Frenilectomia (NO Incluye Paquete)')
	ALI_RADI = models.IntegerField(u'Alisado Radicular (NO Incluye Paquete)')
	ALACORONA = models.IntegerField(u'Alargamiento de Corona (NO Incluye Paquete)')
	GINGI_GINGI = models.IntegerField(u'Gingivectomia y/o Gingivoplastía(por cuadrante, NO Incluye Paquete')
	EXO_ARCADA = models.IntegerField(u'Exostosis por Arcada (NO Incluye Paquete)')
	BIOPSIA = models.IntegerField(u'Biopsia')
	BIO_EST_PAQ = models.IntegerField(u'Biopsia + Estudio + Paquete') 
	'''
	


