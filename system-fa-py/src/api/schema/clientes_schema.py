from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class ClienteSchema(BaseModel):
    nombre: str
    apellido: str
    email: str
    telefono: str
    fecha_nacimiento: Optional[datetime]
    direccion: Optional[str]
    
class ClienteDBSchema(ClienteSchema):
    id: int
    fecha_registro: Optional[datetime]
    ultimo_visita: Optional[datetime]
    
    class Config:
        from_attributes = True