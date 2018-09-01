# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.db.models import Sum


class ProductoClinica(models.Model):
	nombre = models.CharField(u'Nombre', max_length=40)
	tipo = models.CharField(u'Tipo', max_length=150)
	precio = models.IntegerField(u'Precio', default=0)

	def __unicode__(self):
		return self.nombre

class Venta(models.Model):
	folio = models.BigAutoField(u'Folio', primary_key=True)
	fecha =models.DateTimeField(u'Fecha', auto_now_add=True)
	productos = models.ForeignKey(ProductoClinica)
	cantidad = models.IntegerField('Cantidad', default=1)


	


	


	


