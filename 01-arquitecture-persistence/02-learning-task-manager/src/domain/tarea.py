from enum import Enum
from datetime import datetime


class Estado(Enum):
    PENDIENTE = "pendiente"
    COMPLETADA = "completada"


class Tarea:

    def __init__(self, id: int, titulo: str, descripcion: str, fecha: datetime, estado: Estado = Estado.PENDIENTE):
        self.id = id
        self.titulo = titulo
        self.descripcion = descripcion
        self.fecha = fecha
        self.estado = estado
