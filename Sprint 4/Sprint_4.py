from datetime import datetime
from colorama import init, Fore, Style

init(autoreset=True)

class Propietario:
    def __init__(self, nombre, telefono, direccion):
        self.nombre = nombre
        self.telefono = telefono
        self.direccion = direccion

    def __str__(self):
        return f"{self.nombre} | Tel: {self.telefono} | Dirección: {self.direccion}"

class Mascota:
    def __init__(self, nombre, especie, raza, edad, propietario):
        self.nombre = nombre
        self.especie = especie
        self.raza = raza
        self.edad = edad
        self.propietario = propietario

    def __str__(self):
        return f"{self.nombre} ({self.especie} - {self.raza}) | Edad: {self.edad} años | Dueño: {self.propietario.nombre}"

class Consulta:
    def __init__(self, fecha, motivo, diagnostico, mascota):
        self.fecha = fecha
        self.motivo = motivo
        self.diagnostico = diagnostico
        self.mascota = mascota

    def __str__(self):
        return f"Fecha: {self.fecha} | Motivo: {self.motivo} | Diagnóstico: {self.diagnostico}"

def pausar():
    input(Fore.YELLOW + "\nPresione Enter para continuar..." + Style.RESET_ALL)

def registrarPropietario(propietarios):
    print(Fore.CYAN + "--- Registrar Propietario ---" + Style.RESET_ALL)
    nombre = input("Nombre: ").strip()
    telefono = input("Teléfono: ").strip()
    direccion = input("Dirección: ").strip()

    for d in propietarios:
        if d.nombre.lower() == nombre.lower():
            print(Fore.RED + "\nPropietario ya registrado." + Style.RESET_ALL)
            pausar()
            return d

    propietario = Propietario(nombre, telefono, direccion)
    propietarios.append(propietario)
    print(Fore.GREEN + "\nPropietario registrado correctamente." + Style.RESET_ALL)
    pausar()
    return propietario

def registrar_mascota(mascotas, propietarios):
    print(Fore.CYAN + "--- Registrar Mascota ---" + Style.RESET_ALL)
    nombre = input("Nombre de la mascota: ").strip()
    especie = input("Especie: ").strip()
    raza = input("Raza: ").strip()
    while True:
        try:
            edad = int(input("Edad (años): ").strip())
            if edad < 0:
                print(Fore.RED + "Edad no puede ser negativa." + Style.RESET_ALL)
                continue
            break
        except ValueError:
            print(Fore.RED + "Por favor, ingrese un número válido para la edad." + Style.RESET_ALL)

    propietario = registrarPropietario(propietarios)

    mascota = Mascota(nombre, especie, raza, edad, propietario)
    mascotas.append(mascota)
    print(Fore.GREEN + f"\nMascota '{nombre}' registrada correctamente." + Style.RESET_ALL)
    pausar()

def listar_mascotas(mascotas):
    print(Fore.CYAN + "--- Listado de Mascotas ---" + Style.RESET_ALL)
    if not mascotas:
        print(Fore.RED + "No hay mascotas registradas." + Style.RESET_ALL)
    else:
        for i, m in enumerate(mascotas, start=1):
            print(f"{i}. {m}")
    pausar()

def buscar_mascota(mascotas, nombre):
    for m in mascotas:
        if m.nombre.lower() == nombre.lower():
            return m
    return None

def registrar_consulta(mascotas, consultas, propietarios):
    print(Fore.CYAN + "--- Registrar Consulta ---" + Style.RESET_ALL)
    nombre = input("Nombre de la mascota para la consulta: ").strip()
    mascota = buscar_mascota(mascotas, nombre)

    if mascota is None:
        print(Fore.YELLOW + "\nMascota no encontrada." + Style.RESET_ALL)
        decision = input("¿Desea registrar esta mascota? (s/n): ").strip().lower()
        if decision != 's':
            print(Fore.RED + "Consulta cancelada. Mascota no registrada." + Style.RESET_ALL)
            pausar()
            return

        print(Fore.CYAN + "--- Registro rápido de Mascota ---" + Style.RESET_ALL)
        especie = input("Especie: ").strip()
        raza = input("Raza: ").strip()
        while True:
            try:
                edad = int(input("Edad (años): ").strip())
                if edad < 0:
                    print(Fore.RED + "Edad no puede ser negativa." + Style.RESET_ALL)
                    continue
                break
            except ValueError:
                print(Fore.RED + "Por favor, ingrese un número válido para la edad." + Style.RESET_ALL)

        print(Fore.YELLOW + "A continuación, ingrese los datos del dueño..." + Style.RESET_ALL)
        propietario = registrarPropietario(propietarios)

        mascota = Mascota(nombre, especie, raza, edad, propietario)
        mascotas.append(mascota)
        print(Fore.GREEN + f"\nMascota '{nombre}' registrada correctamente." + Style.RESET_ALL)

    fecha_str = input("Fecha (DD-MM-AAAA), dejar vacío para hoy: ").strip()
    if fecha_str == "":
        fecha = datetime.today().strftime("%d-%m-%Y")
    else:
        try:
            fecha = datetime.strptime(fecha_str, "%d-%m-%Y").strftime("%d-%m-%Y")
        except ValueError:
            print(Fore.RED + "\nFormato de fecha inválido. Usando fecha actual." + Style.RESET_ALL)
            fecha = datetime.today().strftime("%d-%m-%Y")

    motivo = input("Motivo de la consulta: ").strip()
    diagnostico = input("Diagnóstico: ").strip()

    consulta = Consulta(fecha, motivo, diagnostico, mascota)
    consultas.append(consulta)
    print(Fore.GREEN + "\nConsulta registrada correctamente." + Style.RESET_ALL)
    pausar()


def mostrar_historial_consultas(consultas):
    print(Fore.CYAN + "--- Historial de Consultas ---" + Style.RESET_ALL)
    nombre = input("Nombre de la mascota: ").strip()
    historial = [c for c in consultas if c.mascota.nombre.lower() == nombre.lower()]
    if not historial:
        print(Fore.RED + "\nNo hay consultas registradas para esa mascota." + Style.RESET_ALL)
        pausar()
        return

    print(f"\nHistorial de consultas para {nombre}:")
    for c in historial:
        print(c)
    pausar()

def menu():
    propietarios = []
    mascotas = []
    consultas = []  # Lista para almacenar todas las consultas

    while True:
        print(Fore.MAGENTA + "=== Clínica Veterinaria Amigos Peludos ===" + Style.RESET_ALL)
        print("1. Registrar mascota")
        print("2. Registrar consulta")
        print("3. Listar mascotas")
        print("4. Ver historial de consultas de una mascota")
        print("5. Salir")
        opcion = input("Seleccione una opción (1-5): ").strip()

        if opcion == '1':
            registrar_mascota(mascotas, propietarios)
        elif opcion == '2':
            registrar_consulta(mascotas, consultas, propietarios)
        elif opcion == '3':
            listar_mascotas(mascotas)
        elif opcion == '4':
            mostrar_historial_consultas(consultas)
        elif opcion == '5':
            print(Fore.GREEN + "\nGracias por usar el sistema. ¡Hasta luego!" + Style.RESET_ALL)
            break
        else:
            print(Fore.RED + "\nOpción inválida, intente de nuevo." + Style.RESET_ALL)
            pausar()

if __name__ == "__main__":
    menu()
