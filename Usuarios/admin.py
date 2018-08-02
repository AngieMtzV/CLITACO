# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from Usuarios.models import Usuario

admin.site.register(Usuario, UserAdmin)
