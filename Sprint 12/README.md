# Sistema de Gestión de## Puesta en marcha

### 🚀 Inicio Rápido (Recomendado)
```batch
# 1. Verificar que Python esté instalado
check_python.bat

# 2. Configuración automática completa (solo primera vez)
setup.bat

# 3. Crear superusuario (opcional)
django_run.bat createsuperuser

# 4. Iniciar servidor
start_server.bat

# 5. Abrir navegador en: http://127.0.0.1:8000/
```

### 🛠️ Configuración Manual
```bash
# 1. Verificar Python
py --version

# 2. Instalar dependencias
py -m pip install -r requirements.txt

# 3. Ejecutar migraciones
django_run.bat migrate

# 4. Crear superusuario
django_run.bat createsuperuser

# 5. Iniciar servidor
start_server.bat
```

### 📁 Archivos de Ayuda Incluidos
- `check_python.bat`: Verifica que Python esté correctamente instalado
- `setup.bat`: Configuración automática completa del proyecto
- `start_server.bat`: Inicia el servidor de desarrollo rápidamente
- `django_run.bat`: Ejecuta comandos Django (uso: `django_run.bat [comando]`)
- `diagnostico.bat`: Diagnóstico completo del sistemaa

Este proyecto Django implementa un sistema completo de gestión para una clínica veterinaria con funcionalidades CRUD para propietarios, mascotas y citas, además de autenticación de usuarios.

## Características Principales

### Sistema de Autenticación
- **Registro de usuarios**: Los nuevos usuarios pueden crear cuentas
- **Inicio y cierre de sesión**: Sistema completo de autenticación
- **Control de acceso**: Las funciones de gestión requieren autenticación
- **Interfaz intuitiva**: Enlaces de login/logout en la navegación

### Gestión de Datos
- **Propietarios**: Registro y gestión de información de los dueños de mascotas
- **Mascotas**: Gestión completa con vinculación a propietarios  
- **Citas**: Sistema de programación de citas vinculadas a mascotas
- **Panel de Administración**: Acceso completo vía Django Admin

### Características Técnicas
- **Logging**: Sistema de registro de eventos y errores
- **Interfaz moderna**: CSS responsivo con diseño moderno
- **Validación de datos**: Validación completa en formularios
- **Mensajes de usuario**: Feedback visual para todas las acciones

## Puesta en marcha

```bash
# 1. Instalar dependencias (ya descrito más arriba)
pip install -r requirements.txt

# 2. Crear las tablas (solo la primera vez o cuando cambien los modelos)
python manage.py migrate

# 3. (Opcional) Generar migraciones si hay cambios en modelos
# python manage.py makemigrations core
# python manage.py migrate

# 4. Crear superusuario para acceso administrativo
python manage.py createsuperuser

# 5. Lanzar servidor de desarrollo
python manage.py runserver
```

## Uso del Sistema

### Acceso Inicial
1. Visite `http://127.0.0.1:8000/` para acceder a la página principal
2. Haga clic en "Registrarse" para crear una nueva cuenta de usuario
3. O use "Iniciar Sesión" si ya tiene una cuenta

### Navegación
- **Inicio**: Página principal con información del estado de autenticación
- **Propietarios**: Gestión de dueños de mascotas (requiere login)
- **Mascotas**: Gestión de mascotas (requiere login)
- **Citas**: Programación de citas veterinarias (requiere login)
- **Admin**: Panel de administración Django (`/admin/`)

### Panel de Administración
- Acceso directo: `http://127.0.0.1:8000/admin/`
- Usuario de prueba: `admin` / `admin123`
- Permite gestión completa de todos los datos

### Funcionalidades de Autenticación
- Los usuarios no autenticados pueden ver la página principal
- Todas las funciones de gestión requieren autenticación
- Los usuarios autenticados ven sus datos y opciones de cierre de sesión
- Mensajes informativos guían al usuario en todo momento

## Estructura del Proyecto

```
Sprint 12/
├── core/                 # Aplicación principal
│   ├── models.py         # Modelos de datos
│   ├── views.py          # Vistas y lógica de negocio
│   ├── forms.py          # Formularios Django
│   ├── urls.py           # Rutas de la aplicación
│   └── admin.py          # Configuración del admin
├── templates/            # Plantillas HTML
│   ├── base.html         # Plantilla base
│   ├── home.html         # Página principal
│   ├── registration/     # Templates de autenticación
│   │   ├── login.html    # Formulario de login
│   │   └── register.html # Formulario de registro
│   └── [otros templates]
├── static/css/           # Archivos CSS
└── veterinaria_web/      # Configuración del proyecto
```

## Validación y Pruebas

Para verificar que todo funciona correctamente:

```bash
# Verificar configuración del proyecto
django_run.bat manage.py check

# Ejecutar servidor de desarrollo
start_server.bat

# Probar funcionalidades:
# 1. Registro de nuevo usuario en: http://127.0.0.1:8000/register/
# 2. Login/logout en: http://127.0.0.1:8000/login/
# 3. Acceso a secciones protegidas
# 4. Gestión de propietarios, mascotas y citas
# 5. Panel de administración: http://127.0.0.1:8000/admin/
```

### Solución de Problemas

#### Error: "Python no encontrado"
1. **Instalar Python**: Descargar desde [python.org](https://python.org)
2. **Marcar "Add Python to PATH"** durante la instalación
3. **Reiniciar** PowerShell/VS Code después de instalar
4. **Verificar**: Ejecutar `check_python.bat`

#### Error: "pip no encontrado"
```bash
# Instalar pip si no está disponible
py -m ensurepip --upgrade
```

#### Error: "No module named 'django'"
```bash
# Instalar Django manualmente
py -m pip install Django==5.2.3
```

#### Error de base de datos
```bash
# Ejecutar migraciones
py manage.py migrate
```

#### Error de permisos
- **Ejecutar PowerShell como administrador** si es necesario
- **Verificar** que no haya antivirus bloqueando Python

#### Para verificar que todo funciona:
```bash
# Verificar Python y dependencias
check_python.bat

# Verificar configuración de Django
py manage.py check

# Ver versión de Django instalada
py -c "import django; print(django.get_version())"
```

## Tecnologías Utilizadas
- **Django 5.2.3**: Framework web principal
- **SQLite**: Base de datos para desarrollo
- **CSS3**: Estilos responsivos y modernos
- **HTML5**: Estructura semántica
- **Python 3.12**: Lenguaje de programación

## Logging
El sistema registra eventos importantes en `veterinaria.log`, incluyendo:
- Inicios y cierres de sesión de usuarios
- Registro de nuevos usuarios
- Intentos de acceso no autorizados
- Errores del sistema