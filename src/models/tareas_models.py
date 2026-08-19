from database import Base
from sqlalchemy import Column, Integer, String

class Tarea(Base):
    __tablename__ = "tarea"

    id = Column(Integer, primary_key= True, index= True)
    titulo = Column(String)
    fecha = Column(String)
    prioridad = Column(String)