from .db import Base
from sqlalchemy import Column, String, DateTime, UUID


class TareaModel(Base):
    __tablename__ = "tareas"

    id = Column(UUID, primary_key=True)
    titulo = Column(String)
    descripcion = Column(String)
    estado = Column(String)
    fecha = Column(DateTime)
