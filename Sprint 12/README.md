## Puesta en marcha

```bash
# 1. Instalar dependencias (ya descrito más arriba)
pip install -r requirements.txt

# 2. Crear las tablas (solo la primera vez o cuando cambien los modelos)
python manage.py migrate

# 3. (Opcional, solo si tú mismo añades/eliminas campos)
# python manage.py makemigrations core
# python manage.py migrate

# 4. Crear superusuario (una sola vez)
python manage.py createsuperuser

# 5. Lanzar servidor de desarrollo
python manage.py runserver
