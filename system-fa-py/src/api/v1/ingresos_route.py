from fastapi import APIRouter, Depends, HTTPException, status, Form, UploadFile
from sqlalchemy.orm import Session
from src.core.database import get_db
from src.models.ingresos import Ingresos
from src.core.deps.auth_deps import get_current_user
from src.api.schema import ListDataResponse, ApiResponse
from src.api.schema.ingresos_schema import IngresoDBSchema, IngresoSchema
import os
import uuid


UPLOAD_DIR = "static/files"

router = APIRouter(
    prefix="/v1/ingresos",
    tags=["INGRESOS"],
    responses={404: {"description": "Not found"}},
    dependencies=[Depends(get_current_user)]
)


@router.get("/", response_model=ListDataResponse[IngresoDBSchema])
def ingresos(pagina: int = 1, limit: int = 10, db: Session = Depends(get_db)):
    ingresos = db.query(Ingresos).offset((pagina - 1) * limit).limit(limit).all()
    total_registros = db.query(Ingresos).count()
    return ListDataResponse(
        status = "success",
        total_paginas = total_registros,
        pagina_actual= pagina,
        data = ingresos
    )
    
    
@router.post("/", response_model=ApiResponse)
def ingreso(form_data: IngresoSchema,db: Session = Depends(get_db), current_user: dict = Depends(get_current_user)):
    
    ingreso = Ingresos(
        usuario_id=current_user,
        proveedor=form_data.proveedor,
        tipo_documento=form_data.tipo_documento,
        codigo_documento=form_data.codigo_documento,
        fecha=form_data.fecha,
        notas_adicionales=form_data.notas_adicionales,
        subtotal=form_data.subtotal,
        igv=form_data.igv,
        total=form_data.total,
        ingresos_productos=form_data.ingresos_productos
    )
    
    
    db.add(ingreso)
    db.commit()
    return ApiResponse(
        status = "success",
        data = "Ingreso creado"
    )
    