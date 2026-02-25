from src.core.database  import Base
from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from datetime import datetime
from sqlalchemy.orm import relationship

class Ingresos(Base):
    __tablename__ = 'ingresos'
    id = Column(Integer, primary_key=True)
    usuario_id = Column(Integer, ForeignKey('usuarios.id'))
    proveedor = Column(String(100), nullable=False)
    tipo_documento = Column(String(10), nullable=False)
    codigo_documento = Column(String(20), nullable=False)
    fecha = Column(DateTime, default=datetime.now())
    notas_adicionales = Column(String(255), nullable=True)
    subtotal = Column(Float(10,2), nullable=False)
    IGV = Column(Float(10,2), nullable=False)
    total = Column(Float(10,2), nullable=False)
    
    usuario = relationship("Usuarios", back_populates="ingresos")
    
class Ingresos_productos(Base):
    __tablename__ = 'ingresos_productos'
    ingreso_id = Column(Integer, ForeignKey('ingresos.id'), primary_key=True)
    producto_id = Column(Integer, ForeignKey('productos.id'), primary_key=True)
    cantidad = Column(Integer, nullable=False, default=0)
    costo_unitario = Column(Float(10,2), nullable=False)
    subtotal = Column(Float(10,2), nullable=False)
    fecha = Column(DateTime, default=datetime.now())
    
    ingreso = relationship("Ingresos", back_populates="ingresos_productos")
    producto = relationship("Productos", back_populates="ingresos_productos")
    
    