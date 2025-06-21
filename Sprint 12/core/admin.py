# core/admin.py
from django.contrib import admin
from .models import Propietario, Mascota, Cita

admin.site.register([Propietario, Mascota, Cita])
