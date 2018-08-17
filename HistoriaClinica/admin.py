# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from HistoriaClinica.models import Civil, HistoriaClinica, Sexo, TipoInterrogatorio, TipoCraneo,Perfil, HistoriaClinicaControlado,PlanTratamiento, PlanEjecucion, HistoriaClinicaIntegral, Estado

admin.site.register(HistoriaClinica)
admin.site.register(Estado)
admin.site.register(Civil)
admin.site.register(Sexo)
admin.site.register(TipoInterrogatorio)
admin.site.register(TipoCraneo)
admin.site.register(Perfil)
admin.site.register(HistoriaClinicaControlado)
admin.site.register(PlanTratamiento)
admin.site.register(PlanEjecucion)
admin.site.register(HistoriaClinicaIntegral)

