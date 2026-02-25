from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from src.core.database import get_db
from src.models.empresa import Empresa, Configuracion
from src.core.security import create_access_token
from src.api.schema.empresa_schema import EmpresaSchema, EmpresaDBSchema

router = APIRouter(
    prefix="/v1/empresa",
    tags=["EMPRESA"]
)

@router.get("/info", response_model=EmpresaDBSchema)
def info(db: Session = Depends(get_db)) -> dict:
    empresa = db.query(Empresa).first()
    if empresa:
        return empresa
    else:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Empresa no encontrada")
    
@router.put("/update")
def update(form_data: EmpresaSchema,db: Session = Depends(get_db)):
    empresa = db.query(Empresa).first()
    if empresa:
        empresa.nombre = form_data.nombre
        empresa.ident_fiscal = form_data.ident_fiscal
        empresa.direccion = form_data.direccion
        empresa.moneda_base = form_data.moneda_base
        empresa.zona_horaria = form_data.zona_horaria
        empresa.is_alert_inventar_bajo = form_data.is_alert_inventar_bajo
        empresa.is_modo_offline = form_data.is_modo_offline
        db.commit()
        return {
            "status": "success",
            "data": "Empresa actualizada"
        }
    else:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Empresa no encontrada")
    
    
@router.get("/configuraciones")
def configure(codigos: str,db: Session = Depends(get_db)):
    codigos = codigos.split(",")
    # where in (codigos)
    configuraciones = db.query(Configuracion).filter(Configuracion.cod_prim.in_(codigos)).all()
    return {
        "status": "success",
        "codigos": codigos,
        "data": configuraciones
    }

    