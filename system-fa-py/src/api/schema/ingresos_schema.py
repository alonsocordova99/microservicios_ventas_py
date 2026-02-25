from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime

class IngresoProductoSchema(BaseModel):
    producto_id: int
    cantidad: int
    costo_unitario: float
    subtotal: float

class IngresoSchema(BaseModel):
    proveedor: str
    tipo_documento: str
    numero_documento: str
    codigo_documento: str
    fecha: str
    notas_adicionales: str
    subtotal: float
    igv: float
    total: float
    
    ingresos_productos: List[IngresoProductoSchema]

class IngresoDBSchema(BaseModel):
    id: int
    usuario_id: int
    
    class Config:
        from_attributes = True
        
        
        
        
        

    
