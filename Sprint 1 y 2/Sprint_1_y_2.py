import re
import os
import platform
from colorama import init, Fore, Style

# Inicializa colorama para que funcione bien en Windows y otros sistemas
init(autoreset=True)

# Para mejorar el estilo se limpia la pantalla y se usa colorama
def limpiar_pantalla():
    sistema = platform.system()
    if sistema == "Windows":
        os.system('cls')
    else:
        os.system('clear')

# Validacion formato correo
def validar_correo(correo):

    patron_basico = r'^[\w\.-]+@[\w\.-]+\.\w+$'

    if not re.match(patron_basico, correo):
        return False

    if correo.endswith("@estudiante.utv.edu.co") or correo.endswith("@utv.edu.co"):
        return True
    else:
        return False

# Clasificacion del correo segun el caso
def clasificar_correo(correo):

    if correo.endswith("@estudiante.utv.edu.co"):
        return "estudiante"
    elif correo.endswith("@utv.edu.co"):
        return "docente"
    else:
        return "desconocido"

# Registro de correos precedidos de la validacion
def registrar_correo(correos):

    print(Fore.CYAN + "\n--- Registro de correo ---" + Style.RESET_ALL)
    correo = input("Ingrese el correo electrónico a registrar: ").strip()

    if validar_correo(correo):
        tipo = clasificar_correo(correo)
        for c in correos:
            if c['correo'].lower() == correo.lower():
                print(Fore.RED + "\n¡Este correo ya está registrado!" + Style.RESET_ALL)
                return
        correos.append({'correo': correo, 'tipo': tipo})
        print(Fore.GREEN + f"\nCorreo registrado correctamente como {tipo}." + Style.RESET_ALL)
    else:
        print(Fore.RED + "\nCorreo inválido. Debe tener formato correcto y dominio permitido." + Style.RESET_ALL)
    print("-" * 40)

# Metodo mostrar
def mostrar_correos(correos):

    print(Fore.CYAN + "\n--- Correos registrados ---" + Style.RESET_ALL)
    if not correos:
        print(Fore.RED + "No hay correos registrados." + Style.RESET_ALL)
    else:
        for i, c in enumerate(correos, start=1):
            print(f"{i}. {c['correo']} ({c['tipo']})")
    print("-" * 40)

# Metodo Buscar
def buscar_correo(correos):

    print(Fore.CYAN + "\n--- Búsqueda de correos ---" + Style.RESET_ALL)
    busqueda = input("Ingrese parte o el correo completo a buscar: ").strip().lower()
    resultados = []

    for c in correos:
        if busqueda in c['correo'].lower():
            resultados.append(c)

    if resultados:
        print(Fore.GREEN + f"\nSe encontraron {len(resultados)} resultado(s):" + Style.RESET_ALL)
        for i, c in enumerate(resultados, start=1):
            print(f"{i}. {c['correo']} ({c['tipo']})")
    else:
        print(Fore.RED + "\nNo se encontraron correos que coincidan con la búsqueda." + Style.RESET_ALL)
    print("-" * 40)

# Funcional
def menu():

    correos = []

    while True:
        limpiar_pantalla()
        print(Fore.CYAN + "=== Biblioteca UTV - Gestor de Correos ===" + Style.RESET_ALL)
        print("1. Registrar un nuevo correo electrónico")
        print("2. Ver correos registrados")
        print("3. Buscar un correo específico")
        print("4. Salir de la aplicación")
        print("-" * 40)

        opcion = input("Seleccione una opción (1-4): ").strip()

        if opcion == '1':
            registrar_correo(correos)
            input("\nPresione Enter para continuar...")
        elif opcion == '2':
            mostrar_correos(correos)
            input("\nPresione Enter para continuar...")
        elif opcion == '3':
            buscar_correo(correos)
            input("\nPresione Enter para continuar...")
        elif opcion == '4':
            print(Fore.GREEN + "\nGracias por usar la aplicación. ¡Hasta luego!" + Style.RESET_ALL)
            break
        else:
            print(Fore.RED + "\nOpción inválida. Por favor ingrese un número entre 1 y 4." + Style.RESET_ALL)
            input("\nPresione Enter para continuar...")


if __name__ == "__main__":
    menu()