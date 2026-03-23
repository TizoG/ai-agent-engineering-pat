from fastapi import FastAPI, APIRouter, HTTPException, status, Depends
from uuid import UUID
from sqlalchemy.orm import Session

from .schemas.create_tarea import CreateTarea
from ..app.use_case.crear_tarea import CrearTarea, ListarTareas, CompletarTarea, EliminarTarea
from .repository.task_repository import MemoriaTareaRepositorio
from .repository.memory_database.sql_repositoy import SqlRepository
from .repository.memory_database.db import get_db
from ..infrastructure.repository.memory_database.db import Base, engine

app = FastAPI()
router = APIRouter()

Base.metadata.create_all(engine)


def get_repo(db: Session = Depends(get_db)):
    return SqlRepository(db)


# Para la Data Base db : Session = Depends(get_db)

@router.post("/tasks")
def create_tarea(tarea: CreateTarea, repo=Depends(get_repo)):
    task_create = CrearTarea(repo)

    try:
        task_create.ejecutar(tarea.titulo,
                             tarea.descripcion,  tarea.estado)
        return {"message": "Tarea creada con exito"}
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))


@router.get("/tasks")
def get_tasks(repo=Depends(get_repo)):
    list_tasks = ListarTareas(repo)
    return list_tasks.ejecutar()


@router.put("/tasks/{id}/complete")
def put_complete(id: UUID, repo=Depends(get_repo)):
    task_complete = CompletarTarea(repo)
    try:
        task_complete.ejecutar(id)
        return {"message": "Tarea completa con exito"}
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))


@router.delete("/tasks/{id}")
def delete_task(id: UUID, repo=Depends(get_repo)):
    dele_task = EliminarTarea(repo)
    try:
        dele_task.ejecutar(id)
        return {"message": "Tarea eliminada correctamente."}
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=str(e))
