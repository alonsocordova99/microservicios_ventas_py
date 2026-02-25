from pydantic import BaseModel
from fastapi import UploadFile, Form
from typing import Optional
from datetime import datetime

class ProductoSchema(BaseModel):
    nombre: str
    descripcion: str
    codigo: str
    categoria_id: int
    costo: float
    precio_venta: float
    url_imagen: str
    usuario_id: int
    
    
class ProductoDBSchema(ProductoSchema):
    id: int
    fecha_registro: datetime
    
    class Config:
        from_attributes = True
        