from pydantic import BaseModel, Field
from typing import Optional

class TallerBase(BaseModel):
    id_trabajo: int
    lado_arreglar: str
    estado: str = Field(..., pattern="^(en arreglo|finalizado)$", description="Debe ser 'en arreglo' o 'finalizado'")

class TallerCreate(TallerBase):
    pass

class TallerUpdate(BaseModel):
    lado_arreglar: Optional[str] = None
    estado: Optional[str] = Field(None, pattern="^(en arreglo|finalizado)$")

class TallerOut(TallerBase):
    id: int

    class Config:
        orm_mode = True
