import csv
import json
import logging
from datetime import datetime

# Configurar logging
logging.basicConfig(
    filename='veterinaria.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# Excepciones personalizadas
class DatosInvalidosError(Exception):
    pass

# Clases principales
class Mascota:
    def __init__(self, nombre, especie, edad):
        if not nombre or not especie or not isinstance(edad, int) or edad < 0:
            raise DatosInvalidosError("Datos inválidos para la mascota")
        self.nombre = nombre
        self.especie = especie
        self.edad = edad

    def to_dict(self):
        return {"nombre": self.nombre, "especie": self.especie, "edad": self.edad}

class Dueno:
    def __init__(self, nombre, direccion, telefono):
        if not nombre or not direccion or not telefono.isdigit():
            raise DatosInvalidosError("Datos inválidos para el dueño")
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono

    def to_dict(self):
        return {"nombre": self.nombre, "direccion": self.direccion, "telefono": self.telefono}

class Consulta:
    def __init__(self, mascota, dueno, fecha, motivo):
        if not isinstance(mascota, Mascota) or not isinstance(dueno, Dueno):
            raise DatosInvalidosError("Consulta debe tener una mascota y un dueño válidos")
        try:
            datetime.strptime(fecha, "%Y-%m-%d")
        except ValueError:
            raise DatosInvalidosError("Formato de fecha inválido, debe ser AAAA-MM-DD")
        if not motivo:
            raise DatosInvalidosError("Motivo de consulta no puede estar vacío")

        self.mascota = mascota
        self.dueno = dueno
        self.fecha = fecha
        self.motivo = motivo

    def to_dict(self):
        return {
            "mascota": self.mascota.to_dict(),
            "dueno": self.dueno.to_dict(),
            "fecha": self.fecha,
            "motivo": self.motivo
        }

# Funciones de manejo de archivos
def guardar_csv(nombre_archivo, datos, campos):
    with open(nombre_archivo, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=campos)
        writer.writeheader()
        writer.writerows(datos)
    logging.info(f'Datos guardados en CSV: {nombre_archivo}')

def guardar_json(nombre_archivo, datos):
    with open(nombre_archivo, 'w') as file:
        json.dump(datos, file, indent=4)
    logging.info(f'Datos guardados en JSON: {nombre_archivo}')

def cargar_json(nombre_archivo):
    with open(nombre_archivo, 'r') as file:
        datos = json.load(file)
    logging.info(f'Datos cargados desde JSON: {nombre_archivo}')
    return datos

# Funciones para agregar datos
def agregar_mascota(nombre, especie, edad):
    mascota = Mascota(nombre, especie, edad)
    logging.info(f'Mascota agregada: {nombre}')
    return mascota

def agregar_dueno(nombre, direccion, telefono):
    dueno = Dueno(nombre, direccion, telefono)
    logging.info(f'Dueño agregado: {nombre}')
    return dueno

def registrar_consulta(mascota, dueno, fecha, motivo):
    consulta = Consulta(mascota, dueno, fecha, motivo)
    logging.info(f'Consulta registrada para {mascota.nombre} el {fecha}')
    return consulta
