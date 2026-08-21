from fastapi import HTTPException, Path, APIRouter, Depends
from typing import Annotated
from schemas.tareas_schemas import Tarea, TareaUpdate
from database import get_db
from sqlalchemy.orm import Session
import models

tareas_router = APIRouter()

# #"BASE DE DATOS"
# tareas: list[Tarea] = [
#     Tarea(id=1, titulo="TP de Backend", fecha="23/06", prioridad="Alta"),
#     Tarea(id=2, titulo="TP de Frontend", fecha="23/06", prioridad="Alta"),
#     Tarea(id=3, titulo="Ver ultima clase de Diseño", fecha="24/06", prioridad="Media"),
# ]

#TAREAS
@tareas_router.get("/", tags= ["Tareas"], response_model= list[Tarea])
def ver_tareas(db: Session = Depends(get_db)) -> list[models.Tarea]:
    return db.query(models.Tarea).all()

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
def ver_tarea(id: Annotated[int, Path(gt=0)], db:Session = Depends(get_db)) -> Tarea:
    tarea_obtenida = db.query(models.Tarea).filter(models.Tarea.id == id).first()
    
    if not tarea_obtenida:
        raise HTTPException(status_code=404, detail="Tarea no encontrada")

    return tarea_obtenida

#AGREGAR TAREA
@tareas_router.post("/", tags = ["Tareas"], response_model= Tarea)
def agregar_tarea(tarea: TareaUpdate, db:Session = Depends(get_db)) -> Tarea:
    nueva_tarea = models.Tarea(
        titulo = tarea.titulo,
        fecha = tarea.fecha,
        prioridad = tarea.prioridad,
    )
    db.add(nueva_tarea)
    db.commit()
    db.refresh(nueva_tarea)

    return nueva_tarea

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
def reescribir_tarea(id: Annotated[int, Path(gt=0)], tarea: TareaUpdate, db: Session = Depends(get_db)) -> Tarea:
    tarea_obtenida = db.query(models.Tarea).filter(models.Tarea.id == id).first()

    if not tarea_obtenida:
        raise HTTPException(status_code=404, detail="Tarea no encontrada")

    setattr(tarea_obtenida, "titulo", tarea.titulo)
    setattr(tarea_obtenida, "fecha", tarea.fecha)
    setattr(tarea_obtenida, "prioridad", tarea.prioridad)

    db.commit()
    db.refresh(tarea_obtenida)

    return tarea_obtenida

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
def borrar_tarea(id: Annotated[int, Path(gt=0)], db: Session = Depends(get_db)) -> list[models.Tarea]:
    tarea_obtenida = db.query(models.Tarea).filter(models.Tarea.id == id).first()

    if not tarea_obtenida:
        raise HTTPException(status_code=404, detail="Tarea no encontrada")

    db.delete(tarea_obtenida)
    db.commit()

    return db.query(models.Tarea).all()