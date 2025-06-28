# Sistema de Gestión de Clínica Veterinaria - Sprint 12.5

## Descripción
Sistema completo de gestión para una clínica veterinaria desarrollado con Django, que incluye gestión de propietarios, mascotas, citas, medicamentos, veterinarios, cirugías y consultas médicas. **Esta versión incluye sistema de autenticación completo con login, logout y registro de usuarios**.

## Características Principales

### Sistema de Autenticación ⭐ NUEVO
- **Registro de usuarios**: Los nuevos usuarios pueden crear cuentas
- **Inicio y cierre de sesión**: Sistema completo de autenticación
- **Control de acceso**: Las funciones de gestión requieren autenticación
- **Interfaz intuitiva**: Enlaces de login/logout en la navegación
- **Logging de eventos**: Registro de todas las actividades de autenticación

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
- **Sistema de autenticación integrado con @login_required** ⭐ NUEVO
- Sistema de logging para auditoría y eventos de autenticación ⭐ ACTUALIZADO
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

## Uso del Sistema

### Acceso Inicial ⭐ NUEVO
1. Visite `http://127.0.0.1:8000/` para acceder a la página principal
2. **Usuarios no autenticados** pueden ver la página principal pero no acceder a funciones de gestión
3. Haga clic en **"Registrarse"** para crear una nueva cuenta de usuario
4. O use **"Iniciar Sesión"** si ya tiene una cuenta
5. Una vez autenticado, tendrá acceso completo a todas las funcionalidades

### Navegación
- **Inicio**: Página principal con información del estado de autenticación ⭐ ACTUALIZADO
- **Propietarios**: Gestión de dueños de mascotas (**requiere login** ⭐)
- **Mascotas**: Gestión de mascotas (**requiere login** ⭐)
- **Citas**: Programación de citas veterinarias (**requiere login** ⭐)
- **Medicamentos**: Control de inventario (**requiere login** ⭐)
- **Veterinarios**: Gestión del equipo médico (**requiere login** ⭐)
- **Cirugías**: Programación quirúrgica (**requiere login** ⭐)
- **Bitácoras**: Registro de consultas (**requiere login** ⭐)
- **Admin**: Panel de administración Django (`/admin/`)

### Panel de Administración
- Acceso directo: `http://127.0.0.1:8000/admin/`
- Usuario de prueba: `admin` / `admin123`
- Permite gestión completa de todos los datos

### Funcionalidades de Autenticación ⭐ NUEVO
- Los usuarios no autenticados pueden ver la página principal
- Todas las funciones de gestión requieren autenticación
- Los usuarios autenticados ven sus datos y opciones de cierre de sesión
- Mensajes informativos guían al usuario en todo momento
- Sistema de logging registra todos los eventos de autenticación

## Validación de Funcionalidades

### 0. Sistema de Autenticación ⭐ NUEVO
1. **Registro**: Ir a `/register/` y crear nueva cuenta
2. **Login**: Acceder a `/login/` con credenciales
3. **Protección**: Intentar acceder a `/propietarios/` sin login (debe redirigir)
4. **Logout**: Cerrar sesión y verificar redirección
5. **Verificar logging**: Revisar `veterinaria.log` para eventos de autenticación

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

- `/` - Página principal (acceso público)
- `/login/` - Iniciar sesión ⭐ NUEVO
- `/logout/` - Cerrar sesión ⭐ NUEVO  
- `/register/` - Registro de usuarios ⭐ NUEVO
- `/propietarios/` - Gestión de propietarios (**requiere login** ⭐)
- `/mascotas/` - Gestión de mascotas (**requiere login** ⭐)
- `/mascotas/{id}/historia/` - Historia clínica (**requiere login** ⭐)
- `/citas/` - Gestión de citas (**requiere login** ⭐)
- `/medicamentos/` - Gestión de medicamentos (**requiere login** ⭐)
- `/veterinarios/` - Gestión de veterinarios (**requiere login** ⭐)
- `/cirugias/` - Programación de cirugías (**requiere login** ⭐)
- `/bitacoras/` - Bitácoras de consulta (**requiere login** ⭐)
- `/exportar/propietarios/` - Exportar propietarios CSV (**requiere login** ⭐)
- `/exportar/mascotas/` - Exportar mascotas CSV (**requiere login** ⭐)
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

- **Sistema de autenticación Django integrado** ⭐ NUEVO
- **Decoradores @login_required en todas las vistas de gestión** ⭐ NUEVO
- **Control de acceso granular** ⭐ NUEVO
- Validación de formularios con Django Forms
- Protección CSRF en formularios
- Confirmación antes de eliminar registros
- **Logging de operaciones críticas y eventos de autenticación** ⭐ ACTUALIZADO

## Estructura del Proyecto

```
Sprint 12.5/
├── core/                   # Aplicación principal
│   ├── models.py          # Modelos de datos
│   ├── views.py           # Lógica de vistas + autenticación ⭐ ACTUALIZADO
│   ├── forms.py           # Formularios Django
│   ├── urls.py            # URLs de la aplicación + auth ⭐ ACTUALIZADO
│   └── admin.py           # Configuración del admin
├── templates/             # Plantillas HTML
│   ├── base.html         # Plantilla base + navegación auth ⭐ ACTUALIZADO
│   ├── home.html         # Página principal + status auth ⭐ ACTUALIZADO
│   ├── registration/     # Templates de autenticación ⭐ NUEVO
│   │   ├── login.html    # Formulario de login ⭐ NUEVO
│   │   └── register.html # Formulario de registro ⭐ NUEVO
│   ├── historia_clinica.html
│   ├── medicamentos_lista.html
│   └── ...
├── static/               # Archivos estáticos
├── veterinaria_web/      # Configuración Django
│   └── settings.py       # + configuraciones LOGIN_* ⭐ ACTUALIZADO
├── manage.py             # Script de gestión Django
├── requirements.txt      # Dependencias
└── README.md            # Este archivo ⭐ ACTUALIZADO
```

## Contribución

1. Seguir el patrón MVT de Django
2. Mantener coherencia en nomenclatura
3. Documentar cambios importantes
4. Probar funcionalidades antes de commit
5. Actualizar README.md según sea necesario
