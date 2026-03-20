from enum import Enum
from datetime import datetime
from uuid import uuid4


class Estado(Enum):
    PENDIENTE = "pendiente"
    COMPLETADA = "completada"


class Tarea:

    def __init__(self, titulo: str, descripcion: str, estado: Estado = Estado.PENDIENTE):
        self.id = uuid4()
        self.titulo = titulo
        self.descripcion = descripcion
        self.fecha = datetime.now()
        self.estado = estado
