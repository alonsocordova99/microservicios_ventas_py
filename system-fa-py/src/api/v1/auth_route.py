from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from src.core.database import get_db
from src.models.usuarios import Usuarios
from src.core.security import create_access_token
from src.api.schema.auth_schema import LoginSchema, RegisterSchema

router = APIRouter(
    prefix="/v1/auth",
    tags=["AUTH"]
)


@router.post("/login")
def login(form_data: LoginSchema,db: Session = Depends(get_db)) -> dict:
    usuario = db.query(Usuarios).filter(Usuarios.email == form_data.username).first()
    if usuario and usuario.check_password(form_data.password):
        token = create_access_token(data={"usuario_id": str(usuario.id)})
        return {
            "access_token": token,
            "token_type": "bearer",
            "status": "success",
            "token": token,
            "data": {
                "usuario": usuario.email,
                "id": usuario.id,
                "rol": usuario.rol,
                "sucursal": usuario.sucursal
            }
        }
    else:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Incorrect email or password")


@router.post("/register")
def register(form_data: RegisterSchema,db: Session = Depends(get_db)):
    usuario = db.query(Usuarios).filter(Usuarios.email == form_data.email).first()
    if usuario:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Email already exists")
    
    usuario = Usuarios(
        nombre=form_data.nombre,
        email=form_data.email,
        password=form_data.password,
        rol="CAJERO",
        sucursal="CENTRO"
    )