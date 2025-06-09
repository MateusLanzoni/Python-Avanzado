import sqlite3
import logging
from datetime import datetime

# Configurar logging
logging.basicConfig(
    filename='veterinaria.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# Inicializar base de datos y tablas
def inicializar_base_datos():
    conn = sqlite3.connect('clinica_veterinaria.db')
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
    conn = sqlite3.connect('clinica_veterinaria.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO duenos (nombre, direccion, telefono) VALUES (?, ?, ?)',
                   (nombre, direccion, telefono))
    conn.commit()
    conn.close()

def insertar_mascota(nombre, especie, edad, id_dueno):
    conn = sqlite3.connect('clinica_veterinaria.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO mascotas (nombre, especie, edad, id_dueno) VALUES (?, ?, ?, ?)',
                   (nombre, especie, edad, id_dueno))
    conn.commit()
    conn.close()

def insertar_consulta(fecha, motivo, diagnostico, id_mascota):
    conn = sqlite3.connect('clinica_veterinaria.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO consultas (fecha, motivo, diagnostico, id_mascota) VALUES (?, ?, ?, ?)',
                   (fecha, motivo, diagnostico, id_mascota))
    conn.commit()
    conn.close()

# CRUD - Mostrar
def mostrar_duenos():
    conn = sqlite3.connect('clinica_veterinaria.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM duenos")
    duenos = cursor.fetchall()
    conn.close()
    return duenos

def mostrar_mascotas():
    conn = sqlite3.connect('clinica_veterinaria.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM mascotas")
    mascotas = cursor.fetchall()
    conn.close()
    return mascotas

def mostrar_consultas():
    conn = sqlite3.connect('clinica_veterinaria.db')
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
    conn = sqlite3.connect('clinica_veterinaria.db')
    cursor = conn.cursor()
    cursor.execute('''
        UPDATE duenos
        SET nombre = ?, direccion = ?, telefono = ?
        WHERE id = ?
    ''', (nombre, direccion, telefono, id_dueno))
    conn.commit()
    conn.close()

def actualizar_mascota(id_mascota, nombre, especie, edad):
    conn = sqlite3.connect('clinica_veterinaria.db')
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
    conn = sqlite3.connect('clinica_veterinaria.db')
    cursor = conn.cursor()
    cursor.execute("DELETE FROM duenos WHERE id = ?", (id_dueno,))
    conn.commit()
    conn.close()

def eliminar_mascota(id_mascota):
    conn = sqlite3.connect('clinica_veterinaria.db')
    cursor = conn.cursor()
    cursor.execute("DELETE FROM mascotas WHERE id = ?", (id_mascota,))
    conn.commit()
    conn.close()

def eliminar_consulta(id_consulta):
    conn = sqlite3.connect('clinica_veterinaria.db')
    cursor = conn.cursor()
    cursor.execute("DELETE FROM consultas WHERE id = ?", (id_consulta,))
    conn.commit()
    conn.close()

# Menú interactivo
def menu():
    inicializar_base_datos()
    while True:
        print("\n--- Menú Principal - Clínica Veterinaria ---")
        print("1. Agregar dueño")
        print("2. Agregar mascota")
        print("3. Registrar consulta")
        print("4. Ver dueños")
        print("5. Ver mascotas")
        print("6. Ver consultas")
        print("7. Actualizar dueño")
        print("8. Actualizar mascota")
        print("9. Eliminar dueño")
        print("10. Eliminar mascota")
        print("11. Eliminar consulta")
        print("0. Salir")

        opcion = input("Seleccione una opción: ")

        try:
            if opcion == "1":
                nombre = input("Nombre del dueño: ")
                direccion = input("Dirección: ")
                telefono = input("Teléfono: ")
                insertar_dueno(nombre, direccion, telefono)
                print("✅ Dueño agregado.")
            elif opcion == "2":
                nombre = input("Nombre de la mascota: ")
                especie = input("Especie: ")
                edad = int(input("Edad: "))
                id_dueno = int(input("ID del dueño: "))
                insertar_mascota(nombre, especie, edad, id_dueno)
                print("✅ Mascota agregada.")
            elif opcion == "3":
                id_mascota = int(input("ID de la mascota: "))
                fecha = input("Fecha (AAAA-MM-DD): ")
                motivo = input("Motivo: ")
                diagnostico = input("Diagnóstico: ")
                insertar_consulta(fecha, motivo, diagnostico, id_mascota)
                print("✅ Consulta registrada.")
            elif opcion == "4":
                for d in mostrar_duenos():
                    print(d)
            elif opcion == "5":
                for m in mostrar_mascotas():
                    print(m)
            elif opcion == "6":
                for c in mostrar_consultas():
                    print(c)
            elif opcion == "7":
                id_dueno = int(input("ID del dueño: "))
                nombre = input("Nuevo nombre: ")
                direccion = input("Nueva dirección: ")
                telefono = input("Nuevo teléfono: ")
                actualizar_dueno(id_dueno, nombre, direccion, telefono)
                print("✅ Dueño actualizado.")
            elif opcion == "8":
                id_mascota = int(input("ID de la mascota: "))
                nombre = input("Nuevo nombre: ")
                especie = input("Nueva especie: ")
                edad = int(input("Nueva edad: "))
                actualizar_mascota(id_mascota, nombre, especie, edad)
                print("✅ Mascota actualizada.")
            elif opcion == "9":
                id_dueno = int(input("ID del dueño: "))
                eliminar_dueno(id_dueno)
                print("🗑️ Dueño eliminado.")
            elif opcion == "10":
                id_mascota = int(input("ID de la mascota: "))
                eliminar_mascota(id_mascota)
                print("🗑️ Mascota eliminada.")
            elif opcion == "11":
                id_consulta = int(input("ID de la consulta: "))
                eliminar_consulta(id_consulta)
                print("🗑️ Consulta eliminada.")
            elif opcion == "0":
                print("👋 Saliendo del sistema...")
                break
            else:
                print("❌ Opción no válida.")
        except Exception as e:
            print(f"⚠️ Error: {e}")

# Ejecutar menú
menu()
