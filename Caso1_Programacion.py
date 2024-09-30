from datetime import datetime

# Clase para representar a un cliente
class Cliente:
    contador_clientes = 0

    def __init__(self, nombre_completo, fecha_nacimiento, municipio):
        Cliente.contador_clientes += 1
        self.id_cliente = Cliente.contador_clientes
        self.nombre_completo = nombre_completo
        self.fecha_nacimiento = fecha_nacimiento
        self.municipio = municipio
        self.servicios = []

    def agregar_servicio(self, servicio):
        self.servicios.append(servicio)

    def mostrar_informacion(self):
        print(f"Cliente ID: {self.id_cliente}")
        print(f"Nombre: {self.nombre_completo}")
        print(f"Fecha de nacimiento: {self.fecha_nacimiento}")
        print(f"Municipio: {self.municipio}")
        print("Servicios adquiridos:")
        for servicio in self.servicios:
            servicio.mostrar_informacion()
        print("\n")

# Clase base para representar un servicio bancario
class ServicioBancario:
    def __init__(self, fecha_adquisicion):
        self.fecha_adquisicion = fecha_adquisicion

    def mostrar_informacion(self):
        pass

# Clase para Cuentas de Ahorro
class CuentaAhorro(ServicioBancario):
    contador_cuentas = 0

    def __init__(self, fecha_adquisicion, interes_anual):
        super().__init__(fecha_adquisicion)
        CuentaAhorro.contador_cuentas += 1
        self.numero_cuenta = CuentaAhorro.contador_cuentas
        self.interes_anual = interes_anual

    def mostrar_informacion(self):
        print(f"Cuenta de Ahorro - Número: {self.numero_cuenta}")
        print(f"Fecha de adquisición: {self.fecha_adquisicion}")
        print(f"Interés anual: {self.interes_anual}%")

# Clase para Tarjetas de Crédito
class TarjetaCredito(ServicioBancario):
    contador_tarjetas_credito = 0

    def __init__(self, fecha_adquisicion, fecha_vencimiento, tipo, limite_credito):
        super().__init__(fecha_adquisicion)
        TarjetaCredito.contador_tarjetas_credito += 1
        self.numero_tarjeta = TarjetaCredito.contador_tarjetas_credito
        self.fecha_vencimiento = fecha_vencimiento
        self.tipo = tipo
        self.limite_credito = limite_credito

    def mostrar_informacion(self):
        print(f"Tarjeta de Crédito - Número: {self.numero_tarjeta}")
        print(f"Fecha de adquisición: {self.fecha_adquisicion}")
        print(f"Fecha de vencimiento: {self.fecha_vencimiento}")
        print(f"Tipo: {self.tipo}")
        print(f"Límite de crédito: {self.limite_credito}")

# Clase para Tarjetas de Débito
class TarjetaDebito(ServicioBancario):
    contador_tarjetas_debito = 0

    def __init__(self, fecha_adquisicion, fecha_vencimiento, numero_cuenta_asociada):
        super().__init__(fecha_adquisicion)
        TarjetaDebito.contador_tarjetas_debito += 1
        self.numero_tarjeta = TarjetaDebito.contador_tarjetas_debito
        self.fecha_vencimiento = fecha_vencimiento
        self.numero_cuenta_asociada = numero_cuenta_asociada

    def mostrar_informacion(self):
        print(f"Tarjeta de Débito - Número: {self.numero_tarjeta}")
        print(f"Fecha de adquisición: {self.fecha_adquisicion}")
        print(f"Fecha de vencimiento: {self.fecha_vencimiento}")
        print(f"Número de cuenta asociada: {self.numero_cuenta_asociada}")

# Clase para Chequeras
class Chequera(ServicioBancario):
    contador_chequeras = 0

    def __init__(self, fecha_adquisicion, fecha_vencimiento, cantidad_cheques):
        super().__init__(fecha_adquisicion)
        Chequera.contador_chequeras += 1
        self.numero_chequera = Chequera.contador_chequeras
        self.fecha_vencimiento = fecha_vencimiento
        self.cantidad_cheques = cantidad_cheques
        self.cheques_entregados = list(range(1, cantidad_cheques+1))  # Números de cheques

    def mostrar_informacion(self):
        print(f"Chequera - Número: {self.numero_chequera}")
        print(f"Fecha de adquisición: {self.fecha_adquisicion}")
        print(f"Fecha de vencimiento: {self.fecha_vencimiento}")
        print(f"Cantidad de cheques: {self.cantidad_cheques}")
        print(f"Cheques entregados: {self.cheques_entregados}")

# Lista para almacenar todos los clientes
clientes = []

# Función para agregar un nuevo cliente
def agregar_cliente():
    nombre = input("Nombre completo: ")
    fecha_nacimiento = input("Fecha de nacimiento (YYYY-MM-DD): ")
    municipio = input("Municipio de residencia: ")
    cliente = Cliente(nombre, fecha_nacimiento, municipio)
    clientes.append(cliente)
    print(f"Cliente {nombre} agregado exitosamente.\n")

# Función para mostrar todos los clientes
def listar_clientes():
    if not clientes:
        print("No hay clientes registrados.\n")
    else:
        print("Clientes registrados:")
        for cliente in clientes:
            print(f"ID: {cliente.id_cliente} - Nombre: {cliente.nombre_completo}")

# Función para buscar un cliente por su ID
def mostrar_cliente():
    id_cliente = int(input("Ingrese el ID del cliente: "))
    for cliente in clientes:
        if cliente.id_cliente == id_cliente:
            cliente.mostrar_informacion()
            return
    print("Cliente no encontrado.\n")

# Menú principal
def menu_principal():
    while True:
        print("\n--- Menú Principal ---")
        print("1. Agregar Cliente")
        print("2. Listar Clientes")
        print("3. Mostrar Información de un Cliente")
        print("4. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            agregar_cliente()
        elif opcion == "2":
            listar_clientes()
        elif opcion == "3":
            mostrar_cliente()
        elif opcion == "4":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción inválida. Intente nuevamente.")

# Ejecutar el menú
menu_principal()
