# veterinaria.py
import logging
import datetime
import json # Para simular una base de datos guardando y cargando en formato JSON

# --------------------------------------------------------------------------- #
# CONFIGURACIÓN DEL LOGGING
# --------------------------------------------------------------------------- #
# Crear un logger específico para la aplicación de la clínica veterinaria.
# Esto es útil si tu aplicación es parte de un sistema más grande y quieres
# configurar el logging de forma independiente.
logger = logging.getLogger('ClinicaVeterinariaApp')
logger.setLevel(logging.DEBUG)  # Establecer el nivel mínimo de severidad para los logs (DEBUG, INFO, WARNING, ERROR, CRITICAL)

# Crear un manejador (handler) para escribir los logs a un archivo.
# 'FileHandler' enviará los mensajes de log a un archivo en disco.
file_handler = logging.FileHandler('clinica_veterinaria.log', mode='w') # 'w' para sobrescribir el log en cada ejecución, 'a' para añadir.
file_handler.setLevel(logging.DEBUG) # Establecer el nivel para este handler específico.

# Crear un formateador para definir el formato de los mensajes de log.
# %(asctime)s: Fecha y hora del log.
# %(name)s: Nombre del logger.
# %(levelname)s: Nivel del log (e.g., INFO, ERROR).
# %(message)s: El mensaje de log.
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)

# Añadir el manejador al logger.
# El logger ahora usará este file_handler para procesar los mensajes.
logger.addHandler(file_handler)

# Opcional: Añadir un handler para mostrar logs en la consola también (útil para desarrollo)
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO) # Mostrar INFO y niveles superiores en consola
console_handler.setFormatter(formatter)
# Descomentar la siguiente línea para activar logs en consola:
# logger.addHandler(console_handler)

logger.info("Logging configurado. La aplicación de la clínica veterinaria ha iniciado.")

# --------------------------------------------------------------------------- #
# CLASES Y FUNCIONES DEL SISTEMA DE LA CLÍNICA
# --------------------------------------------------------------------------- #

class Mascota:
    def __init__(self, id_mascota, nombre, especie, raza, edad, propietario):
        if not nombre or not isinstance(nombre, str):
            logger.error(f"Intento de crear mascota con nombre inválido: {nombre}")
            raise ValueError("El nombre de la mascota no puede estar vacío y debe ser texto.")
        if not especie or not isinstance(especie, str):
            logger.error(f"Intento de crear mascota con especie inválida: {especie}")
            raise ValueError("La especie de la mascota no puede estar vacía y debe ser texto.")
        if not isinstance(edad, int) or edad <= 0:
            logger.error(f"Intento de crear mascota con edad inválida: {edad}")
            raise ValueError("La edad debe ser un número entero positivo.")

        self.id_mascota = id_mascota
        self.nombre = nombre
        self.especie = especie
        self.raza = raza
        self.edad = edad
        self.propietario = propietario
        logger.info(f"Mascota creada: ID {self.id_mascota}, Nombre: {self.nombre}")

    def __str__(self):
        return f"ID: {self.id_mascota}, Nombre: {self.nombre}, Especie: {self.especie}, Raza: {self.raza}, Edad: {self.edad}, Propietario: {self.propietario}"

    def to_dict(self):
        return self.__dict__

    @staticmethod
    def from_dict(data):
        return Mascota(data['id_mascota'], data['nombre'], data['especie'], data['raza'], data['edad'], data['propietario'])

class Clinica:
    def __init__(self, db_file='datos_clinica.json'):
        self.mascotas = {}  # Usar un diccionario para fácil acceso por ID
        self.citas = []
        self.next_mascota_id = 1
        self.next_cita_id = 1
        self.db_file = db_file
        self.cargar_datos()
        logger.info("Sistema de Clínica inicializado.")

    def _generar_id_mascota(self):
        id_actual = self.next_mascota_id
        self.next_mascota_id += 1
        return id_actual

    def _generar_id_cita(self):
        id_actual = self.next_cita_id
        self.next_cita_id += 1
        return id_actual

    def agregar_mascota(self, nombre, especie, raza, edad, propietario):
        try:
            logger.debug(f"Intentando agregar mascota: {nombre}, {especie}, {edad}")
            mascota_id = self._generar_id_mascota()
            nueva_mascota = Mascota(mascota_id, nombre, especie, raza, edad, propietario)
            self.mascotas[mascota_id] = nueva_mascota
            logger.info(f"Mascota '{nombre}' con ID {mascota_id} agregada exitosamente.")
            self.guardar_datos()
            return mascota_id
        except ValueError as ve:
            logger.error(f"Error al agregar mascota (ValueError): {ve}")
            print(f"Error de validación: {ve}")
            return None
        except Exception as e:
            logger.critical(f"Error inesperado al agregar mascota: {e}", exc_info=True)
            print(f"Ocurrió un error inesperado: {e}")
            return None

    def buscar_mascota_por_id(self, id_mascota):
        logger.debug(f"Buscando mascota con ID: {id_mascota}")
        mascota = self.mascotas.get(id_mascota)
        if mascota:
            logger.info(f"Mascota encontrada: {mascota.nombre}")
        else:
            logger.warning(f"No se encontró mascota con ID: {id_mascota}")
        return mascota

    def listar_mascotas(self):
        logger.info("Listando todas las mascotas.")
        if not self.mascotas:
            print("No hay mascotas registradas.")
            logger.info("No hay mascotas para listar.")
            return
        for mascota_id, mascota in self.mascotas.items():
            print(mascota)

    def agendar_cita(self, id_mascota, fecha_hora_str, motivo):
        try:
            logger.debug(f"Intentando agendar cita para mascota ID {id_mascota} en {fecha_hora_str}")
            mascota = self.buscar_mascota_por_id(id_mascota)
            if not mascota:
                print(f"Error: No se encontró la mascota con ID {id_mascota}.")
                logger.warning(f"Intento de agendar cita para mascota no existente ID: {id_mascota}")
                return False

            try:
                fecha_hora = datetime.datetime.strptime(fecha_hora_str, "%Y-%m-%d %H:%M")
                if fecha_hora < datetime.datetime.now():
                    logger.warning(f"Intento de agendar cita en el pasado: {fecha_hora_str}")
                    print("Error: La fecha y hora de la cita deben ser en el futuro.")
                    return False
            except ValueError:
                logger.error(f"Formato de fecha y hora inválido: {fecha_hora_str}")
                print("Error: Formato de fecha y hora inválido. Use YYYY-MM-DD HH:MM.")
                return False

            cita_id = self._generar_id_cita()
            cita = {
                "id_cita": cita_id,
                "id_mascota": id_mascota,
                "nombre_mascota": mascota.nombre,
                "fecha_hora": fecha_hora_str,
                "motivo": motivo,
                "estado": "programada"
            }
            self.citas.append(cita)
            logger.info(f"Cita agendada exitosamente: ID {cita_id} para mascota ID {id_mascota} el {fecha_hora_str}")
            self.guardar_datos()
            return True
        except Exception as e:
            logger.critical(f"Error inesperado al agendar cita: {e}", exc_info=True)
            print(f"Ocurrió un error inesperado al agendar la cita: {e}")
            return False

    def listar_citas(self):
        logger.info("Listando todas las citas.")
        if not self.citas:
            print("No hay citas programadas.")
            logger.info("No hay citas para listar.")
            return
        for cita in self.citas:
            print(f"ID Cita: {cita['id_cita']}, Mascota: {cita['nombre_mascota']} (ID: {cita['id_mascota']}), Fecha: {cita['fecha_hora']}, Motivo: {cita['motivo']}, Estado: {cita['estado']}")

    def guardar_datos(self):
        logger.debug(f"Intentando guardar datos en {self.db_file}")
        try:
            datos = {
                "mascotas": {mid: m.to_dict() for mid, m in self.mascotas.items()},
                "citas": self.citas,
                "next_mascota_id": self.next_mascota_id,
                "next_cita_id": self.next_cita_id
            }
            with open(self.db_file, 'w') as f:
                json.dump(datos, f, indent=4)
            logger.info(f"Datos guardados exitosamente en {self.db_file}")
        except IOError as e:
            logger.error(f"Error de E/S al guardar datos en {self.db_file}: {e}", exc_info=True)
            print(f"Error: No se pudieron guardar los datos en el archivo: {e}")
        except Exception as e:
            logger.critical(f"Error inesperado al guardar datos: {e}", exc_info=True)
            print(f"Error inesperado al guardar datos: {e}")

    def cargar_datos(self):
        logger.debug(f"Intentando cargar datos desde {self.db_file}")
        try:
            with open(self.db_file, 'r') as f:
                datos = json.load(f)
                self.mascotas = {int(mid): Mascota.from_dict(m_data) for mid, m_data in datos.get("mascotas", {}).items()}
                self.citas = datos.get("citas", [])
                self.next_mascota_id = datos.get("next_mascota_id", 1)
                self.next_cita_id = datos.get("next_cita_id", 1)
            logger.info(f"Datos cargados exitosamente desde {self.db_file}")
        except FileNotFoundError:
            logger.warning(f"Archivo de datos {self.db_file} no encontrado. Se iniciará con datos vacíos.")
            print(f"Advertencia: Archivo de datos '{self.db_file}' no encontrado. Se iniciará con una base de datos vacía.")
        except json.JSONDecodeError as e:
            logger.error(f"Error al decodificar JSON desde {self.db_file}: {e}", exc_info=True)
            print(f"Error: El archivo de datos '{self.db_file}' está corrupto o no es un JSON válido.")
        except Exception as e:
            logger.critical(f"Error inesperado al cargar datos: {e}", exc_info=True)
            print(f"Error inesperado al cargar datos: {e}")


# --------------------------------------------------------------------------- #
# FUNCIONES DE UTILIDAD PARA ENTRADAS ROBUSTAS
# --------------------------------------------------------------------------- #

def obtener_input_texto(prompt):
    """Obtiene un input de texto no vacío del usuario."""
    while True:
        try:
            valor = input(prompt).strip()
            if not valor:
                logger.warning("Entrada de texto vacía proporcionada.")
                raise ValueError("La entrada no puede estar vacía.")
            return valor
        except ValueError as e:
            print(f"Error: {e}. Por favor, intente de nuevo.")
        except Exception as e: # Manejo de otras posibles excepciones como EOFError si se interrumpe la entrada
            logger.error(f"Error inesperado al obtener input de texto: {e}", exc_info=True)
            print(f"Ocurrió un error inesperado durante la entrada: {e}. Intente de nuevo.")


def obtener_input_entero_positivo(prompt):
    """Obtiene un input de entero positivo del usuario."""
    while True:
        try:
            valor_str = input(prompt).strip()
            if not valor_str: # Manejar entrada vacía antes de la conversión
                logger.warning("Entrada de entero vacía proporcionada.")
                raise ValueError("La entrada no puede estar vacía.")

            valor = int(valor_str)
            if valor <= 0:
                logger.warning(f"Entrada de entero no positiva: {valor}")
                raise ValueError("El número debe ser positivo.")
            return valor
        except ValueError as e: # Captura errores de int() y los generados manualmente
            logger.error(f"Error al convertir a entero o valor no positivo: {valor_str} -> {e}")
            print(f"Error: {e}. Por favor, ingrese un número entero positivo.")
        except Exception as e:
            logger.error(f"Error inesperado al obtener input de entero: {e}", exc_info=True)
            print(f"Ocurrió un error inesperado durante la entrada: {e}. Intente de nuevo.")

# --------------------------------------------------------------------------- #
# INTERFAZ DE USUARIO (MENÚ PRINCIPAL)
# --------------------------------------------------------------------------- #

def mostrar_menu():
    print("\n--- Clínica Veterinaria ---")
    print("1. Agregar Mascota")
    print("2. Buscar Mascota por ID")
    print("3. Listar todas las Mascotas")
    print("4. Agendar Cita")
    print("5. Listar todas las Citas")
    print("6. Salir")

def main():
    logger.info("Función main iniciada.")
    mi_clinica = Clinica()

    while True:
        mostrar_menu()
        opcion_str = input("Seleccione una opción: ").strip()
        logger.debug(f"Usuario seleccionó la opción: {opcion_str}")

        if opcion_str == '1':
            print("\n--- Agregar Nueva Mascota ---")
            try:
                nombre = obtener_input_texto("Nombre de la mascota: ")
                especie = obtener_input_texto("Especie: ")
                raza = input("Raza (opcional): ").strip() # Raza puede ser opcional y vacía
                edad = obtener_input_entero_positivo("Edad (años): ")
                propietario = obtener_input_texto("Nombre del propietario: ")

                mascota_id = mi_clinica.agregar_mascota(nombre, especie, raza if raza else "N/A", edad, propietario)
                if mascota_id:
                    print(f"Mascota '{nombre}' agregada con ID: {mascota_id}")
            except Exception as e: # Captura general por si algo falla en el flujo de agregar mascota
                logger.error(f"Error en el flujo de agregar mascota: {e}", exc_info=True)
                print(f"Ocurrió un error al intentar agregar la mascota: {e}")

        elif opcion_str == '2':
            print("\n--- Buscar Mascota ---")
            try:
                id_mascota_buscar = obtener_input_entero_positivo("ID de la mascota a buscar: ")
                mascota = mi_clinica.buscar_mascota_por_id(id_mascota_buscar)
                if mascota:
                    print(f"Mascota encontrada: {mascota}")
                else:
                    print(f"No se encontró ninguna mascota con el ID {id_mascota_buscar}.")
            except Exception as e:
                logger.error(f"Error en el flujo de buscar mascota: {e}", exc_info=True)
                print(f"Ocurrió un error al buscar la mascota: {e}")

        elif opcion_str == '3':
            print("\n--- Listado de Mascotas ---")
            mi_clinica.listar_mascotas()

        elif opcion_str == '4':
            print("\n--- Agendar Nueva Cita ---")
            try:
                id_mascota_cita = obtener_input_entero_positivo("ID de la mascota para la cita: ")
                # Verificar si la mascota existe antes de pedir más datos
                if not mi_clinica.buscar_mascota_por_id(id_mascota_cita):
                    print(f"Error: No existe mascota con ID {id_mascota_cita}. No se puede agendar la cita.")
                    logger.warning(f"Intento de agendar cita para mascota ID {id_mascota_cita} que no existe (verificación temprana).")
                    continue # Volver al menú

                fecha_hora_str = obtener_input_texto("Fecha y hora de la cita (YYYY-MM-DD HH:MM): ")
                motivo = obtener_input_texto("Motivo de la cita: ")
                if mi_clinica.agendar_cita(id_mascota_cita, fecha_hora_str, motivo):
                    print("Cita agendada exitosamente.")
                else:
                    print("No se pudo agendar la cita. Revise los mensajes de error y el log.")
            except Exception as e:
                logger.error(f"Error en el flujo de agendar cita: {e}", exc_info=True)
                print(f"Ocurrió un error al intentar agendar la cita: {e}")


        elif opcion_str == '5':
            print("\n--- Listado de Citas ---")
            mi_clinica.listar_citas()

        elif opcion_str == '6':
            logger.info("Usuario seleccionó salir. La aplicación terminará.")
            print("Gracias por usar el sistema de la Clínica Veterinaria. ¡Hasta luego!")
            mi_clinica.guardar_datos() # Asegurarse de guardar antes de salir
            break

        else:
            logger.warning(f"Opción inválida seleccionada por el usuario: {opcion_str}")
            print("Opción no válida. Por favor, intente de nuevo.")

    logger.info("Aplicación de la clínica veterinaria ha finalizado.")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt: # Manejo de Ctrl+C
        logger.info("Aplicación interrumpida por el usuario (KeyboardInterrupt).")
        print("\nAplicación interrumpida. ¡Adiós!")
    except Exception as e: # Captura global de errores no esperados en main
        logger.critical(f"Ha ocurrido un error crítico no capturado en la ejecución principal: {e}", exc_info=True)
        print(f"ERROR CRÍTICO: {e}. Revise 'clinica_veterinaria.log' para más detalles.")