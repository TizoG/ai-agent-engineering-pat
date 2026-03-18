from fastapi import FastAPI, APIRouter, HTTPException

from .schemas.prestamo import PrestamoCreate
from src.app.use_case.consultar_estado import ConsultarEstado
from src.app.use_case.prestar_libro import RealizarPrestamo, RealizarDevolucion
from .repository import JsonLibroRepository, JsonSocioRepository
from ..domain.socio import Socio
from ..domain.libro import Libro


app = FastAPI()

libro_repo = JsonLibroRepository("libros.json")
socio_repo = JsonSocioRepository("socios.json")

libro = Libro("123", "Libro 1", "Autor 1", 10)
socio = Socio(1, "Socio 1", "email", [])
libro_repo.actualizar(libro)
socio_repo.actualizar(socio)

libro_2 = Libro("456", "Libro 2", "Autor 2", 5)
socio_2 = Socio(2, "Socio 2", "email", [])
libro_repo.actualizar(libro_2)
socio_repo.actualizar(socio_2)

libro_3 = Libro("789", "Libro 3", "Autor 3", 10)
socio_3 = Socio(3, "Socio 3", "email", [])
libro_repo.actualizar(libro_3)
socio_repo.actualizar(socio_3)

libro_4 = Libro("012", "Libro 4", "Autor 4", 10)
socio_4 = Socio(4, "Socio 4", "email", [])
libro_repo.actualizar(libro_4)
socio_repo.actualizar(socio_4)

router = APIRouter()


@router.post("/prestamos")
def prestar_libro(prestamo: PrestamoCreate):

    operacion = RealizarPrestamo(libro_repo, socio_repo)
    try:
        operacion.ejecutar(prestamo.socio_id, prestamo.libro_isbn)
        return {"message": "Prestamo realizado con exito"}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.put("/devoluciones")
def devolver_libro(prestamo: PrestamoCreate):

    operacion = RealizarDevolucion(libro_repo, socio_repo)
    try:
        operacion.devolver(prestamo.socio_id, prestamo.libro_isbn)
        return {"message": "Devolucion realizada con exito"}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get("/estado")
def get_biblioteca():
    consulta = ConsultarEstado(libro_repo, socio_repo)
    return consulta.ejecutar()


app.include_router(router)
