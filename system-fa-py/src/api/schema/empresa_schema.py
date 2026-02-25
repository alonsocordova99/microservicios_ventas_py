from pydantic import BaseModel
from typing import Optional


class EmpresaSchema(BaseModel):
    nombre: str
    ident_fiscal: str
    direccion: str
    moneda_base: str
    zona_horaria: str
    is_alert_inventar_bajo: Optional[bool]
    is_modo_offline: Optional[bool]
    
class EmpresaDBSchema(EmpresaSchema):
    id: int
    
    class Config:
        from_attributes = True