from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from src.core.database import get_db
from src.models.clientes import Clientes
from src.api.schema.clientes_schema import ClienteDBSchema, ClienteSchema
from src.api.schema import ListDataResponse, ApiResponse
from src.core.deps.auth_deps import get_current_user

router = APIRouter(
    prefix="/v1/clientes",
    tags=["CLIENTES"],
    responses={404: {"description": "Not found"}},
    dependencies=[Depends(get_current_user)]
)

# paginacion de clientes
@router.get("/", response_model=ListDataResponse[ClienteDBSchema])
def clientes(pagina: int = 1, limit: int = 10, db: Session = Depends(get_db)):
    clientes = db.query(Clientes).offset((pagina - 1) * limit).limit(limit).all()
    total_registros = db.query(Clientes).count()
    return ListDataResponse(
        status = "success",
        total_paginas = total_registros,
        pagina_actual= pagina,
        data = clientes
    )
    
@router.post("/", response_model=ApiResponse)
def cliente(form_data: ClienteSchema,db: Session = Depends(get_db)):
    
    cliente = db.query(Clientes).filter(Clientes.email == form_data.email).first()
    if cliente:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Email already exists")
    
    cliente = Clientes(
        nombre=form_data.nombre,
        apellido=form_data.apellido,
        email=form_data.email,
        telefono=form_data.telefono,
        fecha_nacimiento=form_data.fecha_nacimiento,
        direccion=form_data.direccion
    )
    
    db.add(cliente)
    db.commit()
    return ApiResponse(
        status = "success",
        data = "Cliente creado"
    )
    
@router.delete("/{id}", response_model=ApiResponse)
def delete(id: int,db: Session = Depends(get_db)):
    cliente = db.query(Clientes).filter(Clientes.id == id).first()
    if cliente:
        db.delete(cliente)
        db.commit()
        return ApiResponse(
            status = "success",
            data = "Cliente eliminado"
        )
    else:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Cliente no encontrado")
    
@router.get("/{id}")
def cliente(id: int,db: Session = Depends(get_db)):
    cliente = db.query(Clientes).filter(Clientes.id == id).first()
    if cliente:
        return {
            "status": "success",
            "data": cliente
        }
    else:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Cliente no encontrado")