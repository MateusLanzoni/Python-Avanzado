import csv
import json
import os

# Constantes de archivos
MASCOTAS_CSV = 'mascotas_duenos.csv'
CONSULTAS_JSON = 'consultas.json'


def crear_archivos_si_no_existen():
    """Crea los archivos CSV y JSON si no existen."""
    if not os.path.exists(MASCOTAS_CSV):
        with open(MASCOTAS_CSV, mode='w', newline='') as archivo:
            escritor = csv.writer(archivo)
            escritor.writerow(['nombre_mascota', 'especie', 'raza', 'edad', 'nombre_dueno', 'telefono_dueno'])

    if not os.path.exists(CONSULTAS_JSON):
        with open(CONSULTAS_JSON, mode='w') as archivo:
            json.dump([], archivo)


def leer_mascotas_csv():
    """Lee los datos de mascotas y dueños desde un archivo CSV."""
    with open(MASCOTAS_CSV, mode='r', newline='') as archivo:
        lector = csv.DictReader(archivo)
        return list(lector)


def agregar_mascota():
    """Agrega una nueva mascota al archivo CSV."""
    nombre = input("Nombre de la mascota: ")
    especie = input("Especie: ")
    raza = input("Raza: ")
    edad = input("Edad: ")
    dueno = input("Nombre del dueño: ")
    telefono = input("Teléfono del dueño: ")

    with open(MASCOTAS_CSV, mode='a', newline='') as archivo:
        escritor = csv.writer(archivo)
        escritor.writerow([nombre, especie, raza, edad, dueno, telefono])
    print("✅ Mascota agregada exitosamente.")


def buscar_mascota(nombre):
    """Busca una mascota por su nombre y devuelve sus datos."""
    mascotas = leer_mascotas_csv()
    for mascota in mascotas:
        if mascota['nombre_mascota'].lower() == nombre.lower():
            return mascota
    return None


def listar_mascotas():
    """Muestra todas las mascotas y sus dueños."""
    mascotas = leer_mascotas_csv()
    if mascotas:
        for mascota in mascotas:
            print(f"{mascota['nombre_mascota']} ({mascota['especie']}, {mascota['raza']}), "
                  f"{mascota['edad']} años - Dueño: {mascota['nombre_dueno']} ({mascota['telefono_dueno']})")
    else:
        print("No hay mascotas registradas.")


def leer_consultas_json():
    """Lee las consultas desde un archivo JSON."""
    with open(CONSULTAS_JSON, mode='r') as archivo:
        return json.load(archivo)


def agregar_consulta():
    """Agrega una nueva consulta al archivo JSON."""
    nombre_mascota = input("Nombre de la mascota: ")
    fecha = input("Fecha (YYYY-MM-DD): ")
    motivo = input("Motivo de la consulta: ")
    diagnostico = input("Diagnóstico: ")

    nueva_consulta = {
        "nombre_mascota": nombre_mascota,
        "fecha": fecha,
        "motivo": motivo,
        "diagnostico": diagnostico
    }

    consultas = leer_consultas_json()
    consultas.append(nueva_consulta)

    with open(CONSULTAS_JSON, mode='w') as archivo:
        json.dump(consultas, archivo, indent=4)
    print("✅ Consulta registrada exitosamente.")


def listar_consultas():
    """Muestra todas las consultas registradas."""
    consultas = leer_consultas_json()
    if consultas:
        for c in consultas:
            print(f"{c['fecha']} - {c['nombre_mascota']}: {c['motivo']} (Diagnóstico: {c['diagnostico']})")
    else:
        print("No hay consultas registradas.")


def menu():
    """Menú interactivo del sistema."""
    crear_archivos_si_no_existen()
    while True:
        print("\n--- Amigos Peludos ---")
        print("1. Agregar mascota")
        print("2. Listar mascotas")
        print("3. Buscar mascota")
        print("4. Agregar consulta")
        print("5. Listar consultas")
        print("6. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            agregar_mascota()
        elif opcion == "2":
            listar_mascotas()
        elif opcion == "3":
            nombre = input("Nombre de la mascota a buscar: ")
            resultado = buscar_mascota(nombre)
            if resultado:
                print(f"✅ Mascota encontrada: {resultado}")
            else:
                print("❌ Mascota no encontrada.")
        elif opcion == "4":
            agregar_consulta()
        elif opcion == "5":
            listar_consultas()
        elif opcion == "6":
            print("Hasta luego 🐶🐱")
            break
        else:
            print("Opción no válida. Intente nuevamente.")


# Ejecutar el menú si se corre el archivo directamente
if __name__ == "__main__":
    menu()
