# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from Caja.models import Caja, Venta, ProductoClinica, TipoProducto

admin.site.register(Caja)
admin.site.register(Venta)
admin.site.register(ProductoClinica)
admin.site.register(TipoProducto)
