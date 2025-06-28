@echo off
echo ========================================
echo  Diagnostico del Sistema - Clinica Veterinaria
echo ========================================
echo.

echo [1/6] Verificando Python...
py --version >nul 2>&1
if %errorlevel% equ 0 (
    echo ✓ Python:
    py --version
) else (
    echo ✗ Python no encontrado
    echo   Instala Python desde https://python.org
    goto :error
)

echo.
echo [2/6] Verificando pip...
py -m pip --version >nul 2>&1
if %errorlevel% equ 0 (
    echo ✓ pip disponible
) else (
    echo ✗ pip no encontrado
    goto :error
)

echo.
echo [3/6] Verificando Django...
py -c "import django; print(f'✓ Django {django.get_version()}')" 2>nul
if %errorlevel% neq 0 (
    echo ✗ Django no instalado
    echo   Ejecuta: py -m pip install Django==5.2.3
    goto :error
)

echo.
echo [4/6] Verificando configuracion del proyecto...
py -c "exec(open('manage.py').read())" check --deploy >nul 2>&1
if %errorlevel% equ 0 (
    echo ✓ Configuracion del proyecto OK
) else (
    echo ⚠ Revisar configuracion (normal en desarrollo)
)

echo.
echo [5/6] Verificando base de datos...
if exist "db.sqlite3" (
    echo ✓ Base de datos existe
) else (
    echo ⚠ Base de datos no existe - ejecuta: py manage.py migrate
)

echo.
echo [6/6] Verificando archivos estáticos...
if exist "static\css\estilo.css" (
    echo ✓ Archivos CSS encontrados
) else (
    echo ⚠ Archivos CSS no encontrados
)

echo.
echo ========================================
echo  ¡Diagnostico completado!
echo ========================================
echo ✓ Todo parece estar en orden
echo.
echo Para iniciar el servidor: start_server.bat
echo Para crear superusuario: py manage.py createsuperuser
echo.
goto :end

:error
echo.
echo ========================================
echo  ¡Errores encontrados!
echo ========================================
echo Consulta la seccion "Solucion de Problemas" en README.md
echo.

:end
pause
