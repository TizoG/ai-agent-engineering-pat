from datetime import datetime
from pydantic import BaseModel

from ...domain.tarea import Estado


class CreateTarea(BaseModel):
    titulo: str
    descripcion: str
    estado: Estado
