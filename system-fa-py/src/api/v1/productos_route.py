from fastapi import APIRouter, Depends, HTTPException, status, Form, UploadFile
from sqlalchemy.orm import Session
from src.core.database import get_db
from src.models.productos import Productos, Categorias
from src.core.deps.auth_deps import get_current_user
from src.api.schema import ListDataResponse
from src.api.schema.productos_schema import ProductoDBSchema
import os
import uuid


UPLOAD_DIR = "static/files"

router = APIRouter(
    prefix="/v1/productos",
    tags=["PRODUCTOS"],
    responses={404: {"description": "Not found"}},
    dependencies=[Depends(get_current_user)]
)

# paginacion de productos
@router.get("/", response_model=ListDataResponse[ProductoDBSchema])
def productos(pagina: int = 1, limit: int = 10, db: Session = Depends(get_db)):
    productos = db.query(Productos).offset((pagina - 1) * limit).limit(limit).all()
    total_registros = db.query(Productos).count()
    return ListDataResponse(
        status = "success",
        total_paginas = total_registros,
        pagina_actual= pagina,
        data = productos
    )

# en formData se reciben los parametros de creacion de producto por la imagen
@router.post("/")
async def producto(
    nombre: str = Form(...),
    descripcion: str = Form(...),
    codigo: str = Form(...),
    categoria_id: int = Form(...),
    costo: float = Form(...),
    precio_venta: float = Form(...),
    imagen: UploadFile = Form(...),
    current_user: dict = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    allowed_extensions = ["png", "jpg", "jpeg", "gif"]
    
    extension = imagen.filename.split(".")[-1].lower()
    print(extension)
    if extension not in allowed_extensions:
        raise HTTPException(status_code=400, detail="Formato de imagen inválido")

    # Crear carpeta si no existe
    os.makedirs(UPLOAD_DIR, exist_ok=True)

    # Generar nombre único
    filename = f"{uuid.uuid4()}.{extension}"
    filepath = f"{UPLOAD_DIR}/{filename}"

    # Guardar archivo
    with open(filepath, "wb") as buffer:
        content = await imagen.read()
        buffer.write(content)

    url_imagen = filepath
    
    producto = Productos(
        nombre=nombre,
        descripcion=descripcion,
        codigo=codigo,
        categoria_id=categoria_id,
        costo=costo,
        precio_venta=precio_venta,
        url_imagen=url_imagen,
        usuario_id=current_user
    )
    
    db.add(producto)
    db.commit()
    return {
        "status": "success",
        "data": "Producto creado"
    }

@router.get("/listaSelect", response_model=ListDataResponse[ProductoDBSchema])
def listaSelect(pagina: int = 1, limit: int = 10, db: Session = Depends(get_db)):
    productos = db.query(Productos).offset((pagina - 1) * limit).limit(limit).all()
    total_registros = db.query(Productos).count()
    return ListDataResponse(
        status = "success",
        total_paginas = total_registros,
        pagina_actual= pagina,
        data = productos
    )
    return

@router.get("/categorias")
def categorias(db: Session = Depends(get_db)):
    categorias = db.query(Categorias).all()
    return {
        "status": "success",
        "data": categorias
    }