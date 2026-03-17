from pydantic import BaseModel


class PrestamoCreate(BaseModel):
    socio_id: int
    libro_isbn: str
