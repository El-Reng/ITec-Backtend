from fastapi import HTTPException, Path, APIRouter
from typing import Annotated
from schemas.tareas_schemas import Tarea, TareaUpdate

tareas_router = APIRouter()

#"BASE DE DATOS"
tareas: list[Tarea] = [
    Tarea(id=1, titulo="TP de Backend", fecha="23/06", prioridad="Alta"),
    Tarea(id=2, titulo="TP de Frontend", fecha="23/06", prioridad="Alta"),
    Tarea(id=3, titulo="Ver ultima clase de Diseño", fecha="24/06", prioridad="Alta"),
]

#TAREAS
@tareas_router.get("/", tags= ["Tareas"], response_model= list[Tarea])
def ver_tareas() -> list[Tarea]:
    return tareas

#TAREA
@tareas_router.get("/{id}", tags= ["Tareas"], response_model= Tarea,
        responses={
            404: {
                "description": "Tarea no encontrada",
                "content": {
                    "application/json": {"example": {"detail": "Tarea no encontrada"}}
                }
            }
        })
def ver_tarea(id: Annotated[int, Path(gt=0)]) -> Tarea:
    for t in tareas:
        if t.id == id:
           return t
    raise HTTPException(status_code=404, detail="Tarea no encontrada")

#AGREGAR TAREA
@tareas_router.post("/", tags = ["Tareas"], response_model= list[Tarea])
def agregar_tarea(tarea: Tarea) -> list[Tarea]:
    tareas.append(tarea)
    return tareas

#REESCRIBIR TAREA
@tareas_router.put("/{id}", tags = ["Tareas"], response_model= Tarea,
        responses={
            404: {
                "description": "Tarea no encontrada",
                "content": {
                    "application/json": {"example": {"detail": "Tarea no encontrada"}}
                }
            }
        })
def reescribir_tarea(id: Annotated[int, Path(gt=0)], tarea: TareaUpdate) -> Tarea:
    for t in tareas:
        if t.id == id:
            t.titulo = tarea.titulo
            t.fecha = tarea.fecha
            t.prioridad = tarea.prioridad
            return t
    raise HTTPException(status_code=404, detail="Tarea no encontrada")

#BORRAR TAREA
@tareas_router.delete("/{id}", tags = ["Tareas"], response_model= list[Tarea],
        responses={
            404: {
                "description": "Tarea no encontrada",
                "content": {
                    "application/json": {"example": {"detail": "Tarea no encontrada"}}
                }
            }
        })
def borrar_tarea(id: Annotated[int, Path(gt=0)]) -> list[Tarea]:
    for t in tareas:
        if t.id == id:
            tareas.remove(t)
            return tareas
    raise HTTPException(status_code=404, detail="Tarea no encontrada")