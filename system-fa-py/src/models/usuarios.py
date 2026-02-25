
from src.core.database  import Base
from sqlalchemy import Column, Integer, String, Boolean, DateTime
from datetime import datetime

class Usuarios(Base):
    __tablename__ = 'usuarios'
    id = Column(Integer, primary_key=True)
    nombre = Column(String(50), nullable=False)
    email = Column(String(100), nullable=False)
    rol = Column(String(10), nullable=False)
    sucursal = Column(String(10), nullable=False)
    password = Column(String(255), nullable=False)
    fecha_registro = Column(DateTime, default=datetime.now())
    
    def check_password(self, password):
        return self.password == password

