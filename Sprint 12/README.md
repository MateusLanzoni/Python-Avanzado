# Sprint 10 - Proyecto Django: Clínica Veterinaria

Este sprint contiene un proyecto básico en Django siguiendo el patrón MVT, orientado a una clínica veterinaria.

## Estructura

- `veterinaria_web/`: Proyecto Django
- `core/`: Aplicación principal (vistas, urls, plantillas)
- `templates/`: Plantillas HTML para las vistas
- `.venv/`: Entorno virtual (no subir al repositorio)
- `requirements.txt`: Lista de dependencias

## Cómo ejecutar

1. Crear y activar el entorno virtual:

```bash
python -m venv .venv
.\.venv\Scripts\Activate.ps1

2. Instalar dependencias:

```bash
pip install -r requirements.txt


3. Ejecutar el servidor:

```bash
python manage.py runserver

4. acceder a la APP:

Inicio: http://127.0.0.1:8000/
Servicios: http://127.0.0.1:8000/servicios/
Menú Dinámico: http://127.0.0.1:8000/dinamico/