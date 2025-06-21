# core/views.py
from django.shortcuts import render, redirect
from .models import Propietario, Mascota, Cita
from .forms  import PropietarioForm, MascotaForm, CitaForm

# ---------- HOME & SERVICIOS -----------
def home(request):
    return render(request, "home.html")

def servicios(request):
    return render(request, "servicios.html")

# ---------- PROPIETARIOS ---------------
def propietarios_lista(request):
    return render(request, "propietarios_lista.html",
                  {"propietarios": Propietario.objects.all()})

def propietario_crear(request):
    form = PropietarioForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save(); return redirect("propietarios_lista")
    return render(request, "propietario_form.html", {"form": form})

# ---------- MASCOTAS -------------------
def mascotas_lista(request):
    data = Mascota.objects.select_related("propietario")
    return render(request, "mascotas_lista.html", {"mascotas": data})

def mascota_crear(request):
    form = MascotaForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save(); return redirect("mascotas_lista")
    return render(request, "mascota_form.html", {"form": form})

# ---------- CITAS ----------------------
def citas_lista(request):
    data = Cita.objects.select_related("mascota__propietario")
    return render(request, "citas_lista.html", {"citas": data})

def cita_crear(request):
    form = CitaForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save(); return redirect("citas_lista")
    return render(request, "cita_form.html", {"form": form})
