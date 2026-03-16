from Infrastructure.repository import LibroRepository, SocioRepository


class RealizarPrestamo:
    def __init__(self, libro_repo: LibroRepository, socio_repo: SocioRepository):
        # Inyectamos las dependencias
        self.libro_repo = libro_repo
        self.socio_repo = socio_repo

    def ejecutar(self, id: int, isbn: str):
        # Recuperamos datos
        socio = self.socio_repo.obtener_por_id(id)
        libro = self.libro_repo.obtener_por_isbn(isbn)

        if not socio or not libro:
            raise ValueError("Socio o Libro no encontrado.")

        # Validar reglas de negocio.
        if libro.stock <= 0:
            raise ValueError("No hay unidades disponibles.")

        if len(socio.prestamos) >= 3:
            raise ValueError("El socio ya tiene 3 prestamos activos.")

        # Modificamos

        self.libro_repo.actualizar(libro)
        self.socio_repo.actualizar(socio)

        return "Prestamo realizado con exito"


class RealizarDevolucion:
    def __init__(self, libro_repo: LibroRepository, socio_repo: SocioRepository):
        self.libro_repo = libro_repo
        self.socio_repo = socio_repo

    def devolver(self, id: int, isbn: str):
        socio = self.socio_repo.obtener_por_id(id)
        libro = self.libro_repo.obtener_por_isbn(isbn)

        if not socio or not libro:
            raise ValueError("Socio o Libro no encontrado.")

        if libro.isbn not in socio.prestamos:
            return f"Lo siento, pero {libro.titulo}, no se lo hemos prestado a {socio.nombre}."

        libro.stock += 1
        socio.prestamos.remove(libro.isbn)

        self.libro_repo.actualizar(libro)
        self.socio_repo.actualizar(socio)

        return f"El libro {libro.titulo}, ya lo ha devuelto {socio.nombre}."


class MemoriaLibroRepository(LibroRepository):
    def __init__(self):
        self.libros = {}

    def obtener_por_isbn(self, isbn):
        return self.libros.get(isbn)

    def actualizar(self, libro):
        self.libros[libro.isbn] = libro
