import json
import os
from uuid import UUID

from .task_repository import TaskRepository
from ...domain.tarea import Tarea


class JsonRepository(TaskRepository):

    def __init__(self, archivo="task.json"):
        self.archivo = archivo
        self.tareas = self._cargar_datos()

    def _cargar_datos(self):
        if not os.path.exists(self.archivo):
            return {}
        try:

            with open(self.archivo, "r") as f:
                datos = json.load(f)
                resultado = {}
                for id, d in datos.items():
                    tarea = Tarea(d["titulo"], d["descripcion"], d["estado"])
                    tarea.id = UUID(id)
                    tarea.fecha = d["fecha"]
                    resultado[tarea.id] = tarea

                return resultado

        except IOError as e:
            raise IOError(str(e))

    def _guardar_datos(self):
        try:
            with open(self.archivo, "w") as f:
                datos_a_guardar = {str(id): t.__dict__ for id,
                                   t in self.tareas.items()}
                json.dump(datos_a_guardar, f, indent=4)
        except:
            raise IOError("Error al guardar datos.")

    def get_by_id(self, id: UUID):
        if not self.tareas.get(id):
            raise KeyError("La tarea no existe.")
        return self.tareas.get(id)

    def actualizar_tarea(self, tarea: Tarea):
        self.tareas[tarea.id] = tarea
        self._guardar_datos()

    def get_all(self):
        return list(self.tareas.values())

    def crear_tarea(self, tarea):
        self.tareas[tarea.id] = tarea
        self._guardar_datos()

    def eliminar_tarea(self, id: UUID):
        exists = self.tareas.get(id)
        if not exists:
            raise ValueError("Lo siento pero esta tarea no existe.")
        del self.tareas[id]
