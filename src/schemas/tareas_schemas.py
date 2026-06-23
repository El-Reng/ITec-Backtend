from pydantic import BaseModel, Field
from typing import Annotated

#ESQUEMAS
class Tarea(BaseModel):
    id: Annotated[int, Field(gt=0)]
    titulo: Annotated[str, Field(min_length=1, max_length=50)]
    fecha: Annotated[str, Field(min_length=1, max_length=8, examples=["01/01/26"])]
    prioridad: Annotated[str, Field(min_length=1, max_length=10, examples=["baja", "media", "alta"])]

class TareaUpdate(BaseModel):
    titulo: Annotated[str, Field(min_length=1, max_length=50)]
    fecha: Annotated[str, Field(min_length=1, max_length=8, examples=["01/01/26"])]
    prioridad: Annotated[str, Field(min_length=1, max_length=10, examples=["baja", "media", "alta"])]