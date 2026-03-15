from abc import ABC, abstractmethod
from typing import Optional

from domain.libro import Libro
from domain.socio import Socio


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
