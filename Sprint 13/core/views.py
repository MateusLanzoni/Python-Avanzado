# core/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib import messages
from .models import Propietario, Mascota, Cita, Medicamento, Veterinario, Cirugia, BitacoraConsulta
from .forms import (PropietarioForm, MascotaForm, CitaForm, MedicamentoForm, 
                   VeterinarioForm, CirugiaForm, BitacoraConsultaForm)
import csv
import logging

logger = logging.getLogger(__name__)

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
        form.save()
        messages.success(request, "Propietario creado exitosamente.")
        logger.info(f"Propietario creado: {form.instance.nombre}")
        return redirect("propietarios_lista")
    return render(request, "propietario_form.html", {"form": form})

def propietario_editar(request, pk):
    propietario = get_object_or_404(Propietario, pk=pk)
    form = PropietarioForm(request.POST or None, instance=propietario)
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Propietario actualizado exitosamente.")
        return redirect("propietarios_lista")
    return render(request, "propietario_form.html", {"form": form, "propietario": propietario})

def propietario_eliminar(request, pk):
    propietario = get_object_or_404(Propietario, pk=pk)
    if request.method == "POST":
        nombre = propietario.nombre
        propietario.delete()
        messages.success(request, f"Propietario {nombre} eliminado exitosamente.")
        logger.info(f"Propietario eliminado: {nombre}")
        return redirect("propietarios_lista")
    return render(request, "confirmar_eliminacion.html", {"objeto": propietario, "tipo": "propietario"})

# ---------- MASCOTAS -------------------
def mascotas_lista(request):
    data = Mascota.objects.select_related("propietario")
    return render(request, "mascotas_lista.html", {"mascotas": data})

def mascota_crear(request):
    form = MascotaForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Mascota creada exitosamente.")
        logger.info(f"Mascota creada: {form.instance.nombre}")
        return redirect("mascotas_lista")
    return render(request, "mascota_form.html", {"form": form})

def mascota_editar(request, pk):
    mascota = get_object_or_404(Mascota, pk=pk)
    form = MascotaForm(request.POST or None, instance=mascota)
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Mascota actualizada exitosamente.")
        return redirect("mascotas_lista")
    return render(request, "mascota_form.html", {"form": form, "mascota": mascota})

def mascota_eliminar(request, pk):
    mascota = get_object_or_404(Mascota, pk=pk)
    if request.method == "POST":
        nombre = mascota.nombre
        mascota.delete()
        messages.success(request, f"Mascota {nombre} eliminada exitosamente.")
        logger.info(f"Mascota eliminada: {nombre}")
        return redirect("mascotas_lista")
    return render(request, "confirmar_eliminacion.html", {"objeto": mascota, "tipo": "mascota"})

def historia_clinica(request, mascota_id):
    mascota = get_object_or_404(Mascota, id=mascota_id)
    bitacoras = BitacoraConsulta.objects.filter(mascota=mascota).order_by('-fecha')
    cirugias = Cirugia.objects.filter(mascota=mascota).order_by('-fecha')
    
    context = {
        'mascota': mascota,
        'bitacoras': bitacoras,
        'cirugias': cirugias,
    }
    logger.info(f"Historia clínica generada para mascota: {mascota.nombre}")
    return render(request, "historia_clinica.html", context)

# ---------- CITAS ----------------------
def citas_lista(request):
    data = Cita.objects.select_related("mascota__propietario")
    return render(request, "citas_lista.html", {"citas": data})

def cita_crear(request):
    form = CitaForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Cita creada exitosamente.")
        logger.info(f"Cita creada para mascota: {form.instance.mascota.nombre}")
        return redirect("citas_lista")
    return render(request, "cita_form.html", {"form": form})

def cita_editar(request, pk):
    cita = get_object_or_404(Cita, pk=pk)
    form = CitaForm(request.POST or None, instance=cita)
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Cita actualizada exitosamente.")
        return redirect("citas_lista")
    return render(request, "cita_form.html", {"form": form, "cita": cita})

def cita_eliminar(request, pk):
    cita = get_object_or_404(Cita, pk=pk)
    if request.method == "POST":
        cita.delete()
        messages.success(request, "Cita eliminada exitosamente.")
        logger.info(f"Cita eliminada para mascota: {cita.mascota.nombre}")
        return redirect("citas_lista")
    return render(request, "confirmar_eliminacion.html", {"objeto": cita, "tipo": "cita"})

# ---------- MEDICAMENTOS ---------------
def medicamentos_lista(request):
    medicamentos = Medicamento.objects.all().order_by('nombre')
    return render(request, "medicamentos_lista.html", {"medicamentos": medicamentos})

def medicamento_crear(request):
    form = MedicamentoForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Medicamento registrado exitosamente.")
        return redirect("medicamentos_lista")
    return render(request, "medicamento_form.html", {"form": form})

def medicamento_editar(request, pk):
    medicamento = get_object_or_404(Medicamento, pk=pk)
    form = MedicamentoForm(request.POST or None, instance=medicamento)
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Medicamento actualizado exitosamente.")
        return redirect("medicamentos_lista")
    return render(request, "medicamento_form.html", {"form": form, "medicamento": medicamento})

def medicamento_eliminar(request, pk):
    medicamento = get_object_or_404(Medicamento, pk=pk)
    if request.method == "POST":
        nombre = medicamento.nombre
        medicamento.delete()
        messages.success(request, f"Medicamento {nombre} eliminado exitosamente.")
        return redirect("medicamentos_lista")
    return render(request, "confirmar_eliminacion.html", {"objeto": medicamento, "tipo": "medicamento"})

# ---------- VETERINARIOS ---------------
def veterinarios_lista(request):
    veterinarios = Veterinario.objects.all().order_by('nombre')
    return render(request, "veterinarios_lista.html", {"veterinarios": veterinarios})

def veterinario_crear(request):
    form = VeterinarioForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Veterinario registrado exitosamente.")
        return redirect("veterinarios_lista")
    return render(request, "veterinario_form.html", {"form": form})

def veterinario_editar(request, pk):
    veterinario = get_object_or_404(Veterinario, pk=pk)
    form = VeterinarioForm(request.POST or None, instance=veterinario)
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Veterinario actualizado exitosamente.")
        return redirect("veterinarios_lista")
    return render(request, "veterinario_form.html", {"form": form, "veterinario": veterinario})

def veterinario_eliminar(request, pk):
    veterinario = get_object_or_404(Veterinario, pk=pk)
    if request.method == "POST":
        nombre = veterinario.nombre
        veterinario.delete()
        messages.success(request, f"Veterinario {nombre} eliminado exitosamente.")
        return redirect("veterinarios_lista")
    return render(request, "confirmar_eliminacion.html", {"objeto": veterinario, "tipo": "veterinario"})

# ---------- CIRUGÍAS -------------------
def cirugias_lista(request):
    cirugias = Cirugia.objects.select_related("mascota", "veterinario").order_by('-fecha')
    return render(request, "cirugias_lista.html", {"cirugias": cirugias})

def cirugia_crear(request):
    form = CirugiaForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Cirugía programada exitosamente.")
        return redirect("cirugias_lista")
    return render(request, "cirugia_form.html", {"form": form})

def cirugia_editar(request, pk):
    cirugia = get_object_or_404(Cirugia, pk=pk)
    form = CirugiaForm(request.POST or None, instance=cirugia)
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Cirugía actualizada exitosamente.")
        return redirect("cirugias_lista")
    return render(request, "cirugia_form.html", {"form": form, "cirugia": cirugia})

def cirugia_eliminar(request, pk):
    cirugia = get_object_or_404(Cirugia, pk=pk)
    if request.method == "POST":
        cirugia.delete()
        messages.success(request, "Cirugía eliminada exitosamente.")
        return redirect("cirugias_lista")
    return render(request, "confirmar_eliminacion.html", {"objeto": cirugia, "tipo": "cirugía"})

# ---------- BITÁCORAS DE CONSULTA ------
def bitacoras_lista(request):
    bitacoras = BitacoraConsulta.objects.select_related("mascota", "veterinario").order_by('-fecha')
    return render(request, "bitacoras_lista.html", {"bitacoras": bitacoras})

def bitacora_crear(request):
    form = BitacoraConsultaForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Bitácora de consulta registrada exitosamente.")
        return redirect("bitacoras_lista")
    return render(request, "bitacora_form.html", {"form": form})

def bitacora_editar(request, pk):
    bitacora = get_object_or_404(BitacoraConsulta, pk=pk)
    form = BitacoraConsultaForm(request.POST or None, instance=bitacora)
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Bitácora actualizada exitosamente.")
        return redirect("bitacoras_lista")
    return render(request, "bitacora_form.html", {"form": form, "bitacora": bitacora})

def bitacora_eliminar(request, pk):
    bitacora = get_object_or_404(BitacoraConsulta, pk=pk)
    if request.method == "POST":
        bitacora.delete()
        messages.success(request, "Bitácora eliminada exitosamente.")
        return redirect("bitacoras_lista")
    return render(request, "confirmar_eliminacion.html", {"objeto": bitacora, "tipo": "bitácora"})

# ---------- EXPORTACIÓN CSV ------------
def exportar_propietarios_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="propietarios.csv"'
    
    writer = csv.writer(response)
    writer.writerow(['ID', 'Nombre', 'Teléfono', 'Email'])
    
    for propietario in Propietario.objects.all():
        writer.writerow([propietario.id, propietario.nombre, propietario.telefono, propietario.email])
    
    logger.info("Exportación CSV de propietarios realizada")
    return response

def exportar_mascotas_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="mascotas.csv"'
    
    writer = csv.writer(response)
    writer.writerow(['ID', 'Nombre', 'Especie', 'Edad', 'Propietario'])
    
    for mascota in Mascota.objects.select_related('propietario'):
        writer.writerow([mascota.id, mascota.nombre, mascota.especie, 
                        mascota.edad, mascota.propietario.nombre])
    
    logger.info("Exportación CSV de mascotas realizada")
    return response
