from src.core.database  import Base
from sqlalchemy import Column, Integer, String, Float, Boolean, DateTime
from datetime import datetime

class Configuracion(Base):
    __tablename__ = 'configuracion'
    id = Column(Integer, primary_key=True)
    cod_prim = Column(Integer)
    cod_sec = Column(String(10), nullable=True)
    nombre = Column(String(50), nullable=True)
    descripcion = Column(String(255), nullable=True)
    valor_int = Column(Integer, nullable=True)
    valor_dec = Column(Float(10,2), nullable=True)
    valor_str = Column(String(255), nullable=True)
    estado = Column(Boolean, default=True)
    fecha_registro = Column(DateTime, default=datetime.now())
    
class Empresa(Base):
    __tablename__ = 'empresa'
    id = Column(Integer, primary_key=True)
    nombre = Column(String(50), nullable=False)
    ident_fiscal = Column(String(15), nullable=False)
    direccion = Column(String(100), nullable=False)
    moneda_base = Column(String(10), nullable=False)
    zona_horaria = Column(String(10), nullable=False)
    is_alert_inventar_bajo = Column(Boolean, default=False)
    is_modo_offline = Column(Boolean, default=False)
    fecha_registro = Column(DateTime, default=datetime.now())
    

