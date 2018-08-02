# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from ConsultaExterna.models import valoracionInicial, evolucionConsultaExterna, avanceRapido

admin.site.register(valoracionInicial)
admin.site.register(evolucionConsultaExterna)
admin.site.register(avanceRapido)


