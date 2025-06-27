# core/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("servicios/", views.servicios, name="servicios"),

    # Propietarios
    path("propietarios/", views.propietarios_lista, name="propietarios_lista"),
    path("propietarios/nuevo/", views.propietario_crear, name="propietario_crear"),
    path("propietarios/<int:pk>/editar/", views.propietario_editar, name="propietario_editar"),
    path("propietarios/<int:pk>/eliminar/", views.propietario_eliminar, name="propietario_eliminar"),

    # Mascotas
    path("mascotas/", views.mascotas_lista, name="mascotas_lista"),
    path("mascotas/nuevo/", views.mascota_crear, name="mascota_crear"),
    path("mascotas/<int:pk>/editar/", views.mascota_editar, name="mascota_editar"),
    path("mascotas/<int:pk>/eliminar/", views.mascota_eliminar, name="mascota_eliminar"),
    path("mascotas/<int:mascota_id>/historia/", views.historia_clinica, name="historia_clinica"),

    # Citas
    path("citas/", views.citas_lista, name="citas_lista"),
    path("citas/nuevo/", views.cita_crear, name="cita_crear"),
    path("citas/<int:pk>/editar/", views.cita_editar, name="cita_editar"),
    path("citas/<int:pk>/eliminar/", views.cita_eliminar, name="cita_eliminar"),

    # Medicamentos
    path("medicamentos/", views.medicamentos_lista, name="medicamentos_lista"),
    path("medicamentos/nuevo/", views.medicamento_crear, name="medicamento_crear"),
    path("medicamentos/<int:pk>/editar/", views.medicamento_editar, name="medicamento_editar"),
    path("medicamentos/<int:pk>/eliminar/", views.medicamento_eliminar, name="medicamento_eliminar"),

    # Veterinarios
    path("veterinarios/", views.veterinarios_lista, name="veterinarios_lista"),
    path("veterinarios/nuevo/", views.veterinario_crear, name="veterinario_crear"),
    path("veterinarios/<int:pk>/editar/", views.veterinario_editar, name="veterinario_editar"),
    path("veterinarios/<int:pk>/eliminar/", views.veterinario_eliminar, name="veterinario_eliminar"),

    # Cirugías
    path("cirugias/", views.cirugias_lista, name="cirugias_lista"),
    path("cirugias/nuevo/", views.cirugia_crear, name="cirugia_crear"),
    path("cirugias/<int:pk>/editar/", views.cirugia_editar, name="cirugia_editar"),
    path("cirugias/<int:pk>/eliminar/", views.cirugia_eliminar, name="cirugia_eliminar"),

    # Bitácoras de consulta
    path("bitacoras/", views.bitacoras_lista, name="bitacoras_lista"),
    path("bitacoras/nuevo/", views.bitacora_crear, name="bitacora_crear"),
    path("bitacoras/<int:pk>/editar/", views.bitacora_editar, name="bitacora_editar"),
    path("bitacoras/<int:pk>/eliminar/", views.bitacora_eliminar, name="bitacora_eliminar"),

    # Exportación CSV
    path("exportar/propietarios/", views.exportar_propietarios_csv, name="exportar_propietarios"),
    path("exportar/mascotas/", views.exportar_mascotas_csv, name="exportar_mascotas"),
]
