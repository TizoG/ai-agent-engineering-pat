from sqlalchemy.orm import Session
from uuid import UUID

from ...repository.task_repository import TaskRepository
from .models import TareaModel
from ....domain.tarea import Tarea


class SqlRepository(TaskRepository):

    def __init__(self, db: Session):
        self.db = db

    def get_all(self):
        results = self.db.query(TareaModel).all()
        return results

    def get_by_id(self, id: UUID):
        return self.db.query(TareaModel).filter(TareaModel.id == id).first()

    def crear_tarea(self, tarea: Tarea):
        new_tarea = TareaModel(
            id=tarea.id,
            titulo=tarea.titulo,
            descripcion=tarea.descripcion,
            estado=tarea.estado,
        )
        new_tarea.fecha = tarea.fecha
        self.db.add(new_tarea)
        self.db.commit()

    def actualizar_tarea(self, tarea: Tarea):
        new_tarea = TareaModel(
            id=tarea.id,
            titulo=tarea.titulo,
            descripcion=tarea.descripcion,
            estado=tarea.estado,
        )
        new_tarea.fecha = tarea.fecha
        self.db.merge(new_tarea)
        self.db.commit()

    def eliminar_tarea(self, id: UUID):
        tarea = self.db.query(TareaModel).filter(TareaModel.id == id).first()
        if not tarea:
            raise ValueError("Lo siento pero esta tarea no existe.")
        self.db.delete(tarea)
        self.db.commit()
