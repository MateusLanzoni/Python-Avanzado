@echo off
echo ========================================
echo  Verificador de Python
echo ========================================
echo.

echo Verificando Python...
py --version >nul 2>&1
if %errorlevel% equ 0 (
    echo ✓ Python encontrado:
    py --version
    echo.
    echo Verificando pip...
    py -m pip --version >nul 2>&1
    if %errorlevel% equ 0 (
        echo ✓ pip disponible
        echo.
        echo ¡Todo listo! Puedes ejecutar setup.bat
    ) else (
        echo ✗ pip no encontrado
        echo Instala pip o actualiza Python
    )
) else (
    echo ✗ Python no encontrado
    echo.
    echo Por favor instala Python desde: https://python.org
    echo Asegurate de marcar "Add Python to PATH" durante la instalacion
)

echo.
pause
