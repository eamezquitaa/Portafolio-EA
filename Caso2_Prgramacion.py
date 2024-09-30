# Clase para representar al cónyuge
class Conyuge:
    def __init__(self, nombre, fecha_cumpleanos):
        self.nombre = nombre
        self.fecha_cumpleanos = fecha_cumpleanos

    def mostrar_informacion(self):
        print(f"Cónyuge: {self.nombre}, Cumpleaños: {self.fecha_cumpleanos}")

# Clase para representar a un colaborador
class Colaborador:
    contador_colaboradores = 0

    def __init__(self, nombre_completo, fecha_nacimiento, municipio, division, salario):
        Colaborador.contador_colaboradores += 1
        self.id_colaborador = Colaborador.contador_colaboradores
        self.nombre_completo = nombre_completo
        self.fecha_nacimiento = fecha_nacimiento
        self.municipio = municipio
        self.division = division
        self.salario = salario
        self.conyuge = None

    def agregar_conyuge(self, conyuge):
        self.conyuge = conyuge

    def mostrar_informacion(self):
        print(f"Colaborador ID: {self.id_colaborador}")
        print(f"Nombre: {self.nombre_completo}")
        print(f"Fecha de nacimiento: {self.fecha_nacimiento}")
        print(f"Municipio: {self.municipio}")
        print(f"División: {self.division}")
        print(f"Salario mensual: Q{self.salario}")
        if self.conyuge:
            self.conyuge.mostrar_informacion()
        else:
            print("No tiene cónyuge registrado.")
        print("\n")

# Lista para almacenar todos los colaboradores
colaboradores = []

# Función para agregar un nuevo colaborador
def agregar_colaborador():
    nombre = input("Nombre completo del colaborador: ")
    fecha_nacimiento = input("Fecha de nacimiento (YYYY-MM-DD): ")
    municipio = input("Municipio de residencia: ")
    division = input("División a la que pertenece: ")
    salario = float(input("Salario mensual: Q"))
    colaborador = Colaborador(nombre, fecha_nacimiento, municipio, division, salario)
    colaboradores.append(colaborador)
    print(f"Colaborador {nombre} agregado exitosamente.\n")

# Función para agregar un cónyuge a un colaborador
def agregar_conyuge_a_colaborador():
    id_colaborador = int(input("Ingrese el ID del colaborador: "))
    for colaborador in colaboradores:
        if colaborador.id_colaborador == id_colaborador:
            nombre_conyuge = input("Nombre del cónyuge: ")
            fecha_cumpleanos_conyuge = input("Cumpleaños del cónyuge (YYYY-MM-DD): ")
            conyuge = Conyuge(nombre_conyuge, fecha_cumpleanos_conyuge)
            colaborador.agregar_conyuge(conyuge)
            print(f"Cónyuge agregado a {colaborador.nombre_completo}.\n")
            return
    print("Colaborador no encontrado.\n")

# Función para listar todos los colaboradores
def listar_colaboradores():
    if not colaboradores:
        print("No hay colaboradores registrados.\n")
    else:
        print("Colaboradores registrados:")
        for colaborador in colaboradores:
            print(f"ID: {colaborador.id_colaborador} - Nombre: {colaborador.nombre_completo}")

# Función para mostrar información completa de un colaborador
def mostrar_colaborador():
    id_colaborador = int(input("Ingrese el ID del colaborador: "))
    for colaborador in colaboradores:
        if colaborador.id_colaborador == id_colaborador:
            colaborador.mostrar_informacion()
            return
    print("Colaborador no encontrado.\n")

# Menú principal para colaboradores
def menu_colaboradores():
    while True:
        print("\n--- Menú Colaboradores ---")
        print("1. Agregar Colaborador")
        print("2. Agregar Cónyuge a Colaborador")
        print("3. Listar Colaboradores")
        print("4. Mostrar Información de un Colaborador")
        print("5. Regresar al Menú Principal")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            agregar_colaborador()
        elif opcion == "2":
            agregar_conyuge_a_colaborador()
        elif opcion == "3":
            listar_colaboradores()
        elif opcion == "4":
            mostrar_colaborador()
        elif opcion == "5":
            break
        else:
            print("Opción inválida. Intente nuevamente.")
