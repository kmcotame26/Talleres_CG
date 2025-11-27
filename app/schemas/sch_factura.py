from pydantic import BaseModel
from datetime import date

class FacturaBase(BaseModel):
    fecha: date | None = None
    total: float
    cliente_id: int | None = None

class FacturaCreate(FacturaBase):
    pass

class FacturaOut(FacturaBase):
    id: int

    class Config:
        from_attributes = True
