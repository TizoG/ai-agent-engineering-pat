from abc import ABC, abstractmethod
from typing import Optional

from ...domain.tarea import Tarea


class TaskRepository(ABC):

    @abstractmethod
    def crear_tarea(self, tarea: Tarea) -> None:
        pass

    @abstractmethod
    # Le pongo que me devuelva una lista porque listaremos todas las tareas
    def get_all(self) -> list[Tarea]:
        pass

    @abstractmethod
    def get_by_id(self, id: int) -> Optional[Tarea]:
        pass

    @abstractmethod
    def actualizar_tarea(self, tarea: Tarea) -> None:
        pass

    @abstractmethod
    def eliminar_tarea(self, id: int) -> None:
        pass


class MemoriaTareaRepositorio(TaskRepository):
    def __init__(self):
        self.tareas = {}

    def crear_tarea(self, tarea):
        self.tareas[tarea.id] = tarea

    def get_all(self):
        return list(self.tareas.values())

    def get_by_id(self, id) -> Optional[Tarea]:
        return self.tareas.get(id)

    def actualizar_tarea(self, tarea):
        self.tareas[tarea.id] = tarea

    def eliminar_tarea(self, id):
        del self.tareas[id]
