from src.core.database import Base
from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime

class Clientes(Base):
    __tablename__ = 'clientes'
    id = Column(Integer, primary_key=True)
    nombre = Column(String(50), nullable=False)
    apellido = Column(String(50), nullable=False)
    email = Column(String(100), nullable=False)
    telefono = Column(String(15), nullable=True)
    fecha_nacimiento = Column(DateTime, nullable=True)
    direccion = Column(String(100), nullable=True)
    ultimo_visita = Column(DateTime, nullable=True)
    fecha_registro = Column(DateTime, default=datetime.now())
    
