from src.core.database  import Base
from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from datetime import datetime
from sqlalchemy.orm import relationship

class Ventas(Base):
    __tablename__ = 'ventas'
    id = Column(Integer, primary_key=True)
    cliente_id = Column(Integer, ForeignKey('clientes.id'))
    nombre_cliente = Column(String(50), nullable=True)
    tipo_documento = Column(String(10), nullable=False)
    codigo_documento = Column(String(20), nullable=False)
    subtotal = Column(Float(10,2), nullable=False)
    IGV = Column(Float(10,2), nullable=False)
    total = Column(Float(10,2), nullable=False)
    notas_adicionales = Column(String(255), nullable=True)
    fecha_registro = Column(DateTime, default=datetime.now())
    
    cliente = relationship("Clientes", back_populates="ventas")
    
class Ventas_productos(Base):
    __tablename__ = 'ventas_productos'
    venta_id = Column(Integer, ForeignKey('ventas.id'), primary_key=True)
    producto_id = Column(Integer, ForeignKey('productos.id'), primary_key=True)
    cantidad = Column(Integer, nullable=False, default=0)
    precio_unitario = Column(Float(10,2), nullable=False)
    subtotal = Column(Float(10,2), nullable=False)
    fecha_registro = Column(DateTime, default=datetime.now())
    
    venta = relationship("Ventas", back_populates="ventas_productos")
    producto = relationship("Productos", back_populates="ventas_productos")