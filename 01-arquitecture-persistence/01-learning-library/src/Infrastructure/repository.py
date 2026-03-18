from abc import ABC, abstractmethod
from typing import Optional
import json
import os

from ..domain.libro import Libro
from ..domain.socio import Socio


class LibroRepository(ABC):
    @abstractmethod
    def obtener_por_isbn(self, isbn: str) -> Optional[Libro]:
        pass

    @abstractmethod
    def actualizar(self, libro: Libro) -> None:
        pass


class SocioRepository(ABC):
    @abstractmethod
    def obtener_por_id(self, id: int) -> Optional[Socio]:
        pass

    @abstractmethod
    def actualizar(self, socio: Socio) -> None:
        pass


class MemoriaSocioRepositorio(SocioRepository):
    def __init__(self):
        self.socios = {}

    def obtener_por_id(self, id) -> Optional[Socio]:
        return self.socios.get(id)

    def actualizar(self, socio):
        self.socios[socio.id] = socio

    def obtener_todos(self):
        return list(self.socios.values())


class MemoriaLibroRepository(LibroRepository):
    def __init__(self):
        self.libros = {}

    def obtener_por_isbn(self, isbn) -> Optional[Libro]:
        return self.libros.get(isbn)

    def actualizar(self, libro):
        self.libros[libro.isbn] = libro

    def obtener_todos(self):
        return list(self.libros.values())


class JsonSocioRepository(SocioRepository):
    def __init__(self, archivo="socios.json"):
        self.archivo = archivo
        self.socios = self._cargar_datos()

    def _cargar_datos(self):
        if not os.path.exists(self.archivo):
            return {}

        with open(self.archivo, "r") as f:
            datos = json.load(f)

            return {int(id): Socio(d["id"], d["nombre"], d["email"], d["prestamos"])
                    for id, d in datos.items()}

    def _guardar_datos(self):
        with open(self.archivo, "w") as f:
            datos_a_guardar = {id: s.__dict__ for id,
                               s in self.socios.items()}
            json.dump(datos_a_guardar, f, indent=4)

    def obtener_por_id(self, id: int):
        return self.socios.get(id)

    def actualizar(self, socio: Socio):
        self.socios[socio.id] = socio
        self._guardar_datos()

    def obtener_todos(self):
        return list(self.socios.values())


class JsonLibroRepository(LibroRepository):
    def __init__(self, archivo="libros.json"):
        self.archivo = archivo
        self.libros = self._cargar_datos()

    def _cargar_datos(self):
        if not os.path.exists(self.archivo):
            return {}

        with open(self.archivo, "r") as f:
            datos = json.load(f)

            return {str(isbn): Libro(d["isbn"], d["titulo"], d["autor"], d["stock"])
                    for isbn, d in datos.items()}

    def _guardar_datos(self):
        with open(self.archivo, "w") as f:
            datos_a_guardar = {isbn: l.__dict__ for isbn,
                               l in self.libros.items()}
            json.dump(datos_a_guardar, f, indent=4)

    def obtener_por_isbn(self, id: str):
        return self.libros.get(id)

    def actualizar(self, libro: Libro):
        self.libros[libro.isbn] = libro
        self._guardar_datos()

    def obtener_todos(self):
        return list(self.libros.values())
