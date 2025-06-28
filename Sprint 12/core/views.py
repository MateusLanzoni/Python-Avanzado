# core/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from .models import Propietario, Mascota, Cita
from .forms import PropietarioForm, MascotaForm, CitaForm
import csv
import logging

logger = logging.getLogger(__name__)

# ---------- AUTENTICACIÓN ---------------
def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, f'Bienvenido {user.username}!')
            logger.info(f"Usuario {user.username} ha iniciado sesión")
            return redirect('home')
        else:
            messages.error(request, 'Usuario o contraseña incorrectos.')
            logger.warning(f"Intento de login fallido para usuario: {username}")
    return render(request, 'registration/login.html')

def user_logout(request):
    if request.user.is_authenticated:
        logger.info(f"Usuario {request.user.username} ha cerrado sesión")
        logout(request)
        messages.success(request, 'Has cerrado sesión exitosamente.')
    return redirect('home')

def user_register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Cuenta creada para {username}!')
            logger.info(f"Nuevo usuario registrado: {username}")
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

# ---------- HOME & SERVICIOS -----------
def home(request):
    return render(request, "home.html")

def servicios(request):
    return render(request, "servicios.html")

# ---------- PROPIETARIOS ---------------
@login_required
def propietarios_lista(request):
    return render(request, "propietarios_lista.html",
                  {"propietarios": Propietario.objects.all()})

@login_required
def propietario_crear(request):
    form = PropietarioForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save(); return redirect("propietarios_lista")
    return render(request, "propietario_form.html", {"form": form})

# ---------- MASCOTAS -------------------
@login_required
def mascotas_lista(request):
    data = Mascota.objects.select_related("propietario")
    return render(request, "mascotas_lista.html", {"mascotas": data})

@login_required
def mascota_crear(request):
    form = MascotaForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save(); return redirect("mascotas_lista")
    return render(request, "mascota_form.html", {"form": form})

# ---------- CITAS ----------------------
@login_required
def citas_lista(request):
    data = Cita.objects.select_related("mascota__propietario")
    return render(request, "citas_lista.html", {"citas": data})

@login_required
def cita_crear(request):
    form = CitaForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save(); return redirect("citas_lista")
    return render(request, "cita_form.html", {"form": form})