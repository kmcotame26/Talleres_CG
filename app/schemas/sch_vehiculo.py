from pydantic import BaseModel

class VehiculoBase(BaseModel):
    marca: str
    modelo: str
    placa: str
    cliente_id: int | None = None

class VehiculoCreate(VehiculoBase):
    pass

class VehiculoOut(VehiculoBase):
    id: int

    class Config:
        from_attributes = True
