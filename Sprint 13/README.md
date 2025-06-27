# Sistema de Gestión de Clínica Veterinaria

## Descripción
Sistema completo de gestión para una clínica veterinaria desarrollado con Django, que incluye gestión de propietarios, mascotas, citas, medicamentos, veterinarios, cirugías y consultas médicas.

## Características Principales

### Gestión Básica
- **Propietarios**: Registro, edición, listado y eliminación de propietarios
- **Mascotas**: Gestión completa de mascotas vinculadas a propietarios
- **Citas**: Programación y gestión de citas veterinarias

### Funcionalidades Avanzadas
- **Medicamentos**: Control de inventario con fechas de vencimiento y stock
- **Veterinarios**: Registro de profesionales con especialidades
- **Cirugías**: Programación y seguimiento de cirugías veterinarias
- **Bitácoras de Consulta**: Registro detallado de consultas médicas
- **Historia Clínica**: Generación automática del historial médico completo
- **Exportación CSV**: Exportación de datos básicos en formato CSV

### Características Técnicas
- Patrón MVT (Modelo-Vista-Plantilla) de Django
- Django ORM para gestión de base de datos
- Sistema de logging para auditoría
- Interfaz moderna con Bootstrap 5
- Manejo de excepciones y mensajes de usuario
- Relaciones complejas entre modelos

## Puesta en marcha

```powershell
# 1. Instalar dependencias
C:/Users/mateu/AppData/Local/Programs/Python/Python313/python.exe -m pip install -r requirements.txt

# 2. Crear las tablas (solo la primera vez o cuando cambien los modelos)
C:/Users/mateu/AppData/Local/Programs/Python/Python313/python.exe manage.py makemigrations
C:/Users/mateu/AppData/Local/Programs/Python/Python313/python.exe manage.py migrate

# 3. Crear superusuario (una sola vez)
C:/Users/mateu/AppData/Local/Programs/Python/Python313/python.exe manage.py createsuperuser

# 4. Lanzar servidor de desarrollo
C:/Users/mateu/AppData/Local/Programs/Python/Python313/python.exe manage.py runserver
```

## Validación de Funcionalidades

### 1. Gestión de Medicamentos
1. Acceder a `/medicamentos/`
2. Crear nuevo medicamento con fecha de vencimiento
3. Verificar alertas de stock bajo y medicamentos próximos a vencer
4. Editar cantidad disponible
5. Eliminar medicamento

### 2. Programación de Cirugías
1. Ir a `/cirugias/`
2. Programar nueva cirugía seleccionando mascota y veterinario
3. Cambiar estado de cirugía (programada → en proceso → completada)
4. Ver listado con filtros por estado

### 3. Registro de Bitácoras de Consulta
1. Acceder a `/bitacoras/`
2. Crear nueva consulta médica
3. Incluir observaciones, diagnóstico y tratamiento
4. Asignar medicamentos recetados
5. Registrar peso y temperatura

### 4. Historia Clínica
1. Desde la lista de mascotas, hacer clic en el ícono de historia clínica
2. Verificar que se muestren todas las consultas ordenadas por fecha
3. Ver cirugías programadas/realizadas
4. Comprobar información completa del historial

### 5. Exportación de Datos
1. Usar menú "Exportar" → "Propietarios CSV"
2. Descargar archivo CSV con datos de propietarios
3. Repetir para "Mascotas CSV"
4. Verificar formato y contenido de archivos

### 6. Sistema de Logging
1. Realizar cualquier operación CRUD
2. Verificar archivo `veterinaria.log` en directorio raíz
3. Comprobar registro de eventos importantes

## URLs Principales

- `/` - Página principal
- `/propietarios/` - Gestión de propietarios
- `/mascotas/` - Gestión de mascotas
- `/mascotas/{id}/historia/` - Historia clínica
- `/citas/` - Gestión de citas
- `/medicamentos/` - Gestión de medicamentos
- `/veterinarios/` - Gestión de veterinarios
- `/cirugias/` - Programación de cirugías
- `/bitacoras/` - Bitácoras de consulta
- `/exportar/propietarios/` - Exportar propietarios CSV
- `/exportar/mascotas/` - Exportar mascotas CSV
- `/admin/` - Panel de administración Django

## Modelos de Datos

### Principales
- **Propietario**: Información de contacto
- **Mascota**: Datos de la mascota vinculada a propietario
- **Veterinario**: Información profesional del veterinario

### Operacionales
- **Cita**: Programación de citas
- **Medicamento**: Inventario con control de vencimiento
- **Cirugia**: Programación quirúrgica
- **BitacoraConsulta**: Registro detallado de consultas

## Tecnologías Utilizadas

- Django 5.2.3
- SQLite (base de datos)
- Bootstrap 5 (frontend)
- Font Awesome (iconos)
- Python 3.13

## Características de Seguridad

- Validación de formularios con Django Forms
- Protección CSRF en formularios
- Confirmación antes de eliminar registros
- Logging de operaciones críticas

## Estructura del Proyecto

```
Sprint 12/
├── core/                   # Aplicación principal
│   ├── models.py          # Modelos de datos
│   ├── views.py           # Lógica de vistas
│   ├── forms.py           # Formularios Django
│   ├── urls.py            # URLs de la aplicación
│   └── admin.py           # Configuración del admin
├── templates/             # Plantillas HTML
│   ├── base.html         # Plantilla base
│   ├── historia_clinica.html
│   ├── medicamentos_lista.html
│   └── ...
├── static/               # Archivos estáticos
├── veterinaria_web/      # Configuración Django
├── manage.py             # Script de gestión Django
├── requirements.txt      # Dependencias
└── README.md            # Este archivo
```

## Contribución

1. Seguir el patrón MVT de Django
2. Mantener coherencia en nomenclatura
3. Documentar cambios importantes
4. Probar funcionalidades antes de commit
5. Actualizar README.md según sea necesario
