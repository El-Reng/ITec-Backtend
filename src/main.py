from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers.tareas_router import tareas_router

app = FastAPI()

app.title = "API - Rojo Leonel"
app.summary = "TP Evaluativo: FastAPI"

origins = [
    "http://127.0.0.1:3000",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins = origins,
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers = ["*"],
)

app.include_router(router=tareas_router, prefix="/tareas")