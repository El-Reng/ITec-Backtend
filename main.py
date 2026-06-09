from fastapi import FastAPI, HTTPException, Path
from pydantic import BaseModel, Field
from typing import Annotated

app = FastAPI()
app.title = "API - Rojo Leonel"
app.summary = "Práctico 2: Pydantic"

#ESQUEMAS
class Recordatorio(BaseModel):
    id: Annotated[int, Field(gt=0)]
    titulo: Annotated[str, Field(min_length=1, max_length=50)]
    fecha: Annotated[str, Field(min_length=1, max_length=8, examples=["01/01/26"])]

class RecordatorioUpdate(BaseModel):
    titulo: Annotated[str, Field(min_length=1, max_length=50)]
    fecha: Annotated[str, Field(min_length=1, max_length=8, examples=["01/01/26"])]

#"BASE DE DATOS"
recordatorios: list[Recordatorio] = [
    Recordatorio(id=1, titulo="Tarea de Backend", fecha="22/04"),
    Recordatorio(id=2, titulo="Tarea de Frontend", fecha="22/04"),
    Recordatorio(id=3, titulo="Ver ultima clase de Diseño", fecha="23/04"),
]

#RECORDATORIOS
@app.get("/recordatorios", tags= ["Recordatorios"], response_model= list[Recordatorio])
def ver_recordatorios() -> list[Recordatorio]:
    return recordatorios

#RECORDATORIO
@app.get("/recordatorio/{id}", tags= ["Recordatorios"], response_model= Recordatorio,
        responses={
            404: {
                "description": "Recordatorio no encontrado",
                "content": {
                    "aplication/json": {"example": {"detail": "Recordatorio no encontrado"}}
                }
            }
        })
def ver_recodatorio(id: Annotated[int, Path(gt=0)]) -> Recordatorio:
    for r in recordatorios:
        if r.id == id:
           return r
    raise HTTPException(status_code=404, detail="Recordatorio no encontrado")

#AGREGAR RECORDATORIO
@app.post("/agregar-recordatorio", tags = ["Recordatorios"], response_model= list[Recordatorio])
def agregar_recordatorio(recordatorio: Recordatorio) -> list[Recordatorio]:
    recordatorios.append(recordatorio)
    return recordatorios

#REESCRIBIR RECORDATORIO
@app.put("/reescribir-recordatorio/{id}", tags = ["Recordatorios"], response_model= Recordatorio,
        responses={
            404: {
                "description": "Recordatorio no encontrado",
                "content": {
                    "aplication/json": {"example": {"detail": "Recordatorio no encontrado"}}
                }
            }
        })
def reescribir_recordatorio(id: Annotated[int, Path(gt=0)], recordatorio: RecordatorioUpdate) -> Recordatorio:
    for r in recordatorios:
        if r.id == id:
            r.titulo = recordatorio.titulo
            r.fecha = recordatorio.fecha
            return r
    raise HTTPException(status_code=404, detail="Recordatorio no encontrado")

#BORRAR RECORDATORIO
@app.delete("/borrar-recordatorio/{id}", tags = ["Recordatorios"], response_model= list[Recordatorio],
        responses={
            404: {
                "description": "Recordatorio no encontrado",
                "content": {
                    "aplication/json": {"example": {"detail": "Recordatorio no encontrado"}}
                }
            }
        })
def borrar_recordatorio(id: Annotated[int, Path(gt=0)]) -> list[Recordatorio]:
    for r in recordatorios:
        if r.id == id:
            recordatorios.remove(r)
            return recordatorios
    raise HTTPException(status_code=404, detail="Recordatorio no encontrado")