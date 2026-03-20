from fastapi import FastAPI, APIRouter, HTTPException, status
from uuid import UUID

from .schemas.create_tarea import CreateTarea
from ..app.use_case.crear_tarea import CrearTarea, ListarTareas, CompletarTarea, EliminarTarea
from .repository.task_repository import MemoriaTareaRepositorio

app = FastAPI()
router = APIRouter()

tarea_repo = MemoriaTareaRepositorio()


@router.post("/tasks")
def create_tarea(tarea: CreateTarea):
    task_create = CrearTarea(tarea_repo)

    try:
        task_create.ejecutar(tarea.titulo,
                             tarea.descripcion,  tarea.estado)
        return {"message": "Tarea creada con exito"}
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))


@router.get("/tasks")
def get_tasks():
    list_tasks = ListarTareas(tarea_repo)
    return list_tasks.ejecutar()


@router.put("/tasks/{id}/complete")
def put_complete(id: UUID):
    task_complete = CompletarTarea(tarea_repo)
    try:
        task_complete.ejecutar(id)
        return {"message": "Tarea completa con exito"}
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))


@router.delete("/tasks/{id}")
def delete_task(id: UUID):
    dele_task = EliminarTarea(tarea_repo)
    try:
        dele_task.ejecutar(id)
        return {"message": "Tarea eliminada correctamente."}
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=str(e))
