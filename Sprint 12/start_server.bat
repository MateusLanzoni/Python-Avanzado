@echo off
echo ========================================
echo  Iniciando Servidor de Clinica Veterinaria
echo ========================================
echo.
echo Presiona Ctrl+C para detener el servidor
echo Servidor disponible en: http://127.0.0.1:8000/
echo.
py -c "exec(open('manage.py').read())" runserver
