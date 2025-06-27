# core/admin.py
from django.contrib import admin
from .models import (Propietario, Mascota, Cita, Medicamento, 
                    Veterinario, Cirugia, BitacoraConsulta)

@admin.register(Propietario)
class PropietarioAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'telefono', 'email']
    search_fields = ['nombre', 'email']

@admin.register(Mascota)
class MascotaAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'especie', 'edad', 'propietario']
    list_filter = ['especie']
    search_fields = ['nombre', 'propietario__nombre']

@admin.register(Cita)
class CitaAdmin(admin.ModelAdmin):
    list_display = ['fecha', 'hora', 'mascota', 'motivo']
    list_filter = ['fecha']
    search_fields = ['mascota__nombre', 'motivo']

@admin.register(Medicamento)
class MedicamentoAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'cantidad_disponible', 'fecha_vencimiento']
    list_filter = ['fecha_vencimiento']
    search_fields = ['nombre']

@admin.register(Veterinario)
class VeterinarioAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'especialidad', 'telefono']
    search_fields = ['nombre', 'especialidad']

@admin.register(Cirugia)
class CirugiaAdmin(admin.ModelAdmin):
    list_display = ['fecha', 'tipo_cirugia', 'mascota', 'veterinario', 'estado']
    list_filter = ['estado', 'fecha']
    search_fields = ['tipo_cirugia', 'mascota__nombre']

@admin.register(BitacoraConsulta)
class BitacoraConsultaAdmin(admin.ModelAdmin):
    list_display = ['fecha', 'mascota', 'veterinario', 'diagnostico']
    list_filter = ['fecha']
    search_fields = ['mascota__nombre', 'diagnostico']
    filter_horizontal = ['medicamentos_recetados']
