class Libreria:
    def __init__(self, secciones, direccion):
        self.secciones = secciones
        self.direccion = direccion
        self.catalogo = []

    def agregar_libro(self, libro):
        self.catalogo.append(libro)
        print(f'Libro "{libro.titulo}" agregado al catálogo.')

    def eliminar_libro(self, titulo):
        self.catalogo = [libro for libro in self.catalogo if libro.titulo != titulo]
        print(f'Libro "{titulo}" eliminado del catálogo.')

    def __str__(self):
        return f'Librería en {self.direccion} con secciones: {", ".join(self.secciones)}'

class Libro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
        self.prestado = False
        self.fecha_de_devolucion = None
        self.historial_prestamos = []

    def prestar(self, fecha_de_devolucion):
        self.prestado = True
        self.fecha_de_devolucion = fecha_de_devolucion
        self.historial_prestamos.append(fecha_de_devolucion)
        print(f'Libro "{self.titulo}" prestado hasta {fecha_de_devolucion}.')

    def devolver(self):
        self.prestado = False
        self.fecha_de_devolucion = None
        print(f'Libro "{self.titulo}" devuelto.')

    def __str__(self):
        estado = "prestado" if self.prestado else "disponible"
        return f'Libro: {self.titulo} por {self.autor}, actualmente {estado}.'

class Lector:
    def __init__(self, carnet, nombre, apellido, fecha_nacimiento):
        self.carnet = carnet
        self.nombre = nombre
        self.apellido = apellido
        self.fecha_nacimiento = fecha_nacimiento
        self.libros_prestados = []

    def prestar_libro(self, libro, fecha_de_devolucion):
        if not libro.prestado:
            libro.prestar(fecha_de_devolucion)
            self.libros_prestados.append(libro)
        else:
            print(f'El libro "{libro.titulo}" ya está prestado.')

    def devolver_libro(self, libro):
        if libro in self.libros_prestados:
            libro.devolver()
            self.libros_prestados.remove(libro)
        else:
            print(f'El libro "{libro.titulo}" no está prestado por este lector.')

    def consultar_libros(self):
        if self.libros_prestados:
            print(f'Libros prestados por {self.nombre} {self.apellido}:')
            for libro in self.libros_prestados:
                print(f'- {libro.titulo}')
        else:
            print(f'{self.nombre} {self.apellido} no tiene libros prestados.')

    def __str__(self):
        return f'Lector: {self.nombre} {self.apellido}, Carnet: {self.carnet}'

# Ejemplo 
libreria = Libreria(["Ficción", "No Ficción", "Ciencia"], "Calle Principal 123")
libro1 = Libro("El Quijote", "Miguel de Cervantes")
libro2 = Libro("Cien Años de Soledad", "Gabriel García Márquez")
lector = Lector("12345", "Juan", "Pérez", "01/01/1990")

libreria.agregar_libro(libro1)
libreria.agregar_libro(libro2)
print(libreria)

lector.prestar_libro(libro1, "10/09/2024")
lector.consultar_libros()
lector.devolver_libro(libro1)
lector.consultar_libros()





