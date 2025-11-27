from pydantic import BaseModel

class AdministradorBase(BaseModel):
    nombre: str
    correo: str
    rol: str | None = None

class AdministradorCreate(AdministradorBase):
    pass

class AdministradorOut(AdministradorBase):
    id: int

    class Config:
        from_attributes = True
