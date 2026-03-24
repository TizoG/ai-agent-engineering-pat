from abc import ABC, abstractmethod
from typing import Optional

from ..domain.model_producto import Producto


class ProductRepository(ABC):

    @abstractmethod
    def guardar(self, producto: Producto) -> None:
        pass

    @abstractmethod
    def get_by_id(self, id: int) -> Optional[Producto]:
        pass

    @abstractmethod
    def get_all(self) -> list[Producto]:
        pass
