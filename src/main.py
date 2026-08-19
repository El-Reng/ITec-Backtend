from fastapi import FastAPI
from database import Base, engine
from fastapi.middleware.cors import CORSMiddleware
from routers.tareas_router import tareas_router
import models

Base.metadata.create_all(bind= engine)

app = FastAPI()

app.title = "API - Rojo Leonel"
app.summary = "TP Evaluativo: FastAPI"

origins = [
    "http://localhost:5173",
    "http://127.0.0.1:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins = origins,
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers = ["*"],
)

app.include_router(router=tareas_router, prefix="/tareas")