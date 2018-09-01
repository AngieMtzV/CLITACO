# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from Caja.models import  Venta, ProductoClinica


admin.site.register(Venta)
admin.site.register(ProductoClinica)

