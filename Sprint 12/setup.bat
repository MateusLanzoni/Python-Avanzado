@echo off
echo ========================================
echo  Configuracion inicial de la Clinica Veterinaria
echo ========================================
echo.

echo [1/5] Verificando Python...
py --version >nul 2>&1
if %errorlevel% neq 0 (
    echo Error: Python no encontrado. Instala Python desde python.org
    pause
    exit /b 1
)

echo [2/5] Instalando dependencias...
py -m pip install -r requirements.txt
if %errorlevel% neq 0 (
    echo Error al instalar dependencias.
    pause
    exit /b 1
)

echo [3/5] Verificando configuracion Django...
py -c "exec(open('manage.py').read())" check
if %errorlevel% neq 0 (
    echo Error en la configuracion de Django.
    pause
    exit /b 1
)

echo [4/5] Ejecutando migraciones...
py -c "exec(open('manage.py').read())" migrate
if %errorlevel% neq 0 (
    echo Error al ejecutar migraciones.
    pause
    exit /b 1
)

echo [5/5] ¡Configuracion completada!
echo.
echo Para crear un superusuario, ejecuta:
echo django_run.bat createsuperuser
echo.
echo Para iniciar el servidor, ejecuta:
echo start_server.bat
echo.
echo Luego visita: http://127.0.0.1:8000/
echo.
pause
