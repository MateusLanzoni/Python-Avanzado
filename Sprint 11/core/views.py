from django.shortcuts import render, redirect
from .models import Propietario, Mascota
from .forms  import PropietarioForm, MascotaForm

# ---------- Propietarios ----------
def propietarios_lista(request):
    data = Propietario.objects.all()
    return render(request, "propietarios_lista.html", {"propietarios": data})

def propietario_crear(request):
    form = PropietarioForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("propietarios_lista")
    return render(request, "propietario_form.html", {"form": form})

# ---------- Mascotas ----------
def mascotas_lista(request):
    data = Mascota.objects.select_related("propietario")
    return render(request, "mascotas_lista.html", {"mascotas": data})

def mascota_crear(request):
    form = MascotaForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("mascotas_lista")
    return render(request, "mascota_form.html", {"form": form})
