from django.shortcuts import render
from . import db_api  # Este archivo contiene tus funciones de SQLite

def home(request):
    return render(request, 'home.html')

def servicios(request):
    return render(request, 'servicios.html')

def dinamico(request):
    duenos = db_api.mostrar_duenos()
    mascotas = db_api.mostrar_mascotas()
    consultas = db_api.mostrar_consultas()
    return render(request, 'dinamico.html', {
        'duenos': duenos,
        'mascotas': mascotas,
        'consultas': consultas
    })