from pydantic import BaseModel
from typing import Generic, TypeVar, List

T = TypeVar("T")

class ListDataResponse(BaseModel, Generic[T]):
    status: str
    data: List[T]
    total_paginas: int
    pagina_actual: int
    

class ApiResponse(BaseModel):
    status: str
    data: str