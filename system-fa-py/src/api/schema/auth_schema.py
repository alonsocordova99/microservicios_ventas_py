from pydantic import BaseModel
from typing import Optional


class LoginSchema(BaseModel):
    username: str
    password: str
    
class RegisterSchema(BaseModel):
    nombre: str
    email: str
    password: str
    password_confirm: str
