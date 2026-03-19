from datetime import datetime

from ...infrastructure.repository.task_repository import TaskRepository
from ...domain.tarea import Estado, Tarea


class CrearTarea:

    def __init__(self, tarea_repo: TaskRepository):

        self.tarea_repo = tarea_repo

    def ejecutar(self, id: int, titulo: str, descripcion: str, fecha: datetime, estado: Estado):
        list_tareas = self.tarea_repo.get_all()
        for title in list_tareas:
            if title.titulo == titulo:
                raise ValueError(
                    "Lo siento, pero el titulo de la tarea debe de ser unico.")

        total_pendientes = sum(
            t.estado == Estado.PENDIENTE for t in list_tareas)

        if total_pendientes >= 10:
            raise ValueError("No puedes tener más de 10 tareas.")
        new_tarea = Tarea(
            id=id,
            titulo=titulo,
            descripcion=descripcion,
            fecha=fecha,
            estado=estado
        )
        self.tarea_repo.crear_tarea(new_tarea)
        return f"La tarea {new_tarea.titulo} se ha añadido."


class CompletarTarea:

    def __init__(self, tarea_repo: TaskRepository):
        self.tarea_repo = tarea_repo

    def ejecutar(self, id: int):
        tarea_buscada = self.tarea_repo.get_by_id(id)
        if not tarea_buscada:
            raise ValueError("Lo siento, pero no encontramos esta tarea.")
        tarea_buscada.estado = Estado.COMPLETADA
        self.tarea_repo.actualizar_tarea(tarea_buscada)


class ListarTareas:

    def __init__(self, tarea_repo: TaskRepository):
        self.tarea_repo = tarea_repo

    def ejecutar(self):
        all_task = self.tarea_repo.get_all()
        return all_task
