from fastapi import FastAPI
from fastapi import Body

app = FastAPI()
app.title = "API - Rojo Leonel"
app.summary = "Práctico 1: Crud en memoria con FastAPI"

recordatorios = [
    {"id": 1, "titulo": "Tarea de Backend", "fecha": "22/04"},
    {"id": 2, "titulo": "Tarea de Frontend", "fecha": "22/04"},
    {"id": 3, "titulo": "Ver ultima clase de Diseño", "fecha": "23/04"},
]

@app.get("/recordatorios", tags = ["Recordatorios"])
async def ver_recordatorios():
    return recordatorios

@app.get("/recordatorio/{id}", tags = ["Recordatorios"])
def ver_recodatorio(id: int):
    for r in recordatorios:
        if r["id"] == id:
           return r
    return []

@app.post("/agregar-recordatorio", tags = ["Recordatorios"])
def agregar_recordatorio(id: int, titulo: str, fecha: str):
    recordatorio_nuevo = {"id": id, "titulo": titulo, "fecha": fecha} 
    recordatorios.append(recordatorio_nuevo)
    return recordatorios

@app.put("/reescribir-recordatorio", tags = ["Recordatorios"])
def reescribir_recordatorio(id: int = Body(), titulo: str = Body(), fecha: str = Body()):
    for r in recordatorios:
        if r["id"] == id:
            r["titulo"] = titulo
            r["fecha"] = fecha
            return {"msg": "El recordatorio fue editado correctamente"}
    return []

@app.patch("/editar-recordatorio", tags = ["Recordatorios"])
def editar_recordatorio(id: int, titulo: str | None = None, fecha: str | None = None):
    for r in recordatorios:
        if r["id"] == id:
            r["titulo"] = titulo if titulo else r["titulo"]
            r["genero"] = fecha if fecha else r["genero"]
            return r
    return {"msg": "No se encontró el recordatorio a editar"}

@app.delete("/borrar-recordatorio/{id}", tags = ["Recordatorios"])
def borrar_recordatorio(id: int):
    for r in recordatorios:
        if r["id"] == id:
            recordatorios.remove(r)
            return recordatorios
    return {"msg": "Recordatorio no encontrado"}