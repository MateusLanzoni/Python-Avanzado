import sqlite3
import logging
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DB_PATH  = BASE_DIR / "clinica_veterinaria.db"

def _connect():
    return sqlite3.connect(DB_PATH)

# Configurar logging
logging.basicConfig(
    filename='veterinaria.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# Inicializar base de datos y tablas
def inicializar_base_datos():
    conn = _connect()
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS duenos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            direccion TEXT NOT NULL,
            telefono TEXT NOT NULL
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS mascotas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            especie TEXT NOT NULL,
            edad INTEGER NOT NULL,
            id_dueno INTEGER NOT NULL,
            FOREIGN KEY (id_dueno) REFERENCES duenos(id)
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS consultas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            fecha TEXT NOT NULL,
            motivo TEXT NOT NULL,
            diagnostico TEXT,
            id_mascota INTEGER NOT NULL,
            FOREIGN KEY (id_mascota) REFERENCES mascotas(id)
        )
    ''')

    conn.commit()
    conn.close()
    logging.info("Base de datos y tablas creadas.")

# CRUD - Insertar
def insertar_dueno(nombre, direccion, telefono):
    conn = _connect()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO duenos (nombre, direccion, telefono) VALUES (?, ?, ?)',
                   (nombre, direccion, telefono))
    conn.commit()
    conn.close()

def insertar_mascota(nombre, especie, edad, id_dueno):
    conn = _connect()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO mascotas (nombre, especie, edad, id_dueno) VALUES (?, ?, ?, ?)',
                   (nombre, especie, edad, id_dueno))
    conn.commit()
    conn.close()

def insertar_consulta(fecha, motivo, diagnostico, id_mascota):
    conn = _connect()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO consultas (fecha, motivo, diagnostico, id_mascota) VALUES (?, ?, ?, ?)',
                   (fecha, motivo, diagnostico, id_mascota))
    conn.commit()
    conn.close()

# CRUD - Mostrar
def mostrar_duenos():
    conn = _connect()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM duenos")
    duenos = cursor.fetchall()
    conn.close()
    return duenos

def mostrar_mascotas():
    conn = _connect()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM mascotas")
    mascotas = cursor.fetchall()
    conn.close()
    return mascotas

def mostrar_consultas():
    conn = _connect()
    cursor = conn.cursor()
    cursor.execute('''
        SELECT c.id, c.fecha, c.motivo, c.diagnostico, m.nombre AS mascota
        FROM consultas c
        JOIN mascotas m ON c.id_mascota = m.id
    ''')
    consultas = cursor.fetchall()
    conn.close()
    return consultas

# CRUD - Actualizar
def actualizar_dueno(id_dueno, nombre, direccion, telefono):
    conn = _connect()
    cursor = conn.cursor()
    cursor.execute('''
        UPDATE duenos
        SET nombre = ?, direccion = ?, telefono = ?
        WHERE id = ?
    ''', (nombre, direccion, telefono, id_dueno))
    conn.commit()
    conn.close()

def actualizar_mascota(id_mascota, nombre, especie, edad):
    conn = _connect()
    cursor = conn.cursor()
    cursor.execute('''
        UPDATE mascotas
        SET nombre = ?, especie = ?, edad = ?
        WHERE id = ?
    ''', (nombre, especie, edad, id_mascota))
    conn.commit()
    conn.close()

# CRUD - Eliminar
def eliminar_dueno(id_dueno):
    conn = _connect()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM duenos WHERE id = ?", (id_dueno,))
    conn.commit()
    conn.close()

def eliminar_mascota(id_mascota):
    conn = _connect()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM mascotas WHERE id = ?", (id_mascota,))
    conn.commit()
    conn.close()

def eliminar_consulta(id_consulta):
    conn = _connect()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM consultas WHERE id = ?", (id_consulta,))
    conn.commit()
    conn.close()