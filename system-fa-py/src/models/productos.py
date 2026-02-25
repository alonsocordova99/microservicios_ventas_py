from src.core.database  import Base
from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from datetime import datetime
from sqlalchemy.orm import relationship


class Categorias(Base):
    __tablename__ = 'categorias'
    id = Column(Integer, primary_key=True)
    nombre = Column(String(50), nullable=False)
    url_imagen = Column(String(255), nullable=True)
    descripcion = Column(String(255), nullable=True)
    fecha_registro = Column(DateTime, default=datetime.now())
    
    
    
class Productos(Base):
    __tablename__ = 'productos'
    id = Column(Integer, primary_key=True)
    nombre = Column(String(50), nullable=False)
    descripcion = Column(String(255), nullable=False)
    codigo = Column(String(15), nullable=False)
    costo = Column(Float(10,2), nullable=False)
    precio_venta = Column(Float(10,2), nullable=False)
    url_imagen = Column(String(255), nullable=True)
    fecha_registro = Column(DateTime, default=datetime.now())
    
    categoria_id = Column(Integer, ForeignKey('categorias.id'))
    usuario_id = Column(Integer, ForeignKey('usuarios.id'))
    
    categoria = relationship("Categorias", backref="productos")
    usuario = relationship("Usuarios", backref="productos")
    
    


class Stocks(Base):
    __tablename__ = 'stocks'
    id = Column(Integer, primary_key=True)
    producto_id = Column(Integer, ForeignKey('productos.id'), primary_key=True)
    cantidad = Column(Integer, nullable=False, default=0)
    cantidad_anterior = Column(Integer, nullable=False, default=0)
    fecha = Column(DateTime, default=datetime.now())
    
    producto = relationship("Productos", backref="stocks")
    

class Movimientos(Base):
    __tablename__ = 'movimientos'
    id = Column(Integer, primary_key=True)
    usuario_id = Column(Integer, ForeignKey('usuarios.id'))
    cantidad = Column(Integer, nullable=False, default=0)
    producto_id = Column(Integer, ForeignKey('productos.id'))
    tipo_movimiento = Column(String(10), nullable=False)
    fecha_movimiento = Column(DateTime, default=datetime.now())
    
    usuario = relationship("Usuarios", backref="movimientos")
    producto = relationship("Productos", backref="movimientos")