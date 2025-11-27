from pydantic import BaseModel
from typing import Optional
from datetime import date

class TrabajoBase(BaseModel):
    descripcion: str
    sub_costo: float
    lado: str
    fecha_finalizacion: Optional[date] = None

class TrabajoCreate(TrabajoBase):
    pass

class TrabajoUpdate(BaseModel):
    descripcion: Optional[str] = None
    sub_costo: Optional[float] = None
    lado: Optional[str] = None
    fecha_finalizacion: Optional[date] = None

class TrabajoOut(TrabajoBase):
    id: int

    class Config:
        orm_mode = True
