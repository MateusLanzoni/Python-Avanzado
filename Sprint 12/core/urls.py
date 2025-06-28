# core/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("servicios/", views.servicios, name="servicios"),

    # Autenticación
    path("login/", views.user_login, name="login"),
    path("logout/", views.user_logout, name="logout"),
    path("register/", views.user_register, name="register"),

    path("propietarios/", views.propietarios_lista, name="propietarios_lista"),
    path("propietarios/nuevo/", views.propietario_crear, name="propietario_crear"),

    path("mascotas/", views.mascotas_lista, name="mascotas_lista"),
    path("mascotas/nuevo/", views.mascota_crear, name="mascota_crear"),

    path("citas/", views.citas_lista, name="citas_lista"),
    path("citas/nuevo/", views.cita_crear, name="cita_crear"),
]