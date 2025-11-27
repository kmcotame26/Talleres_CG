from pydantic import BaseModel

class ClienteBase(BaseModel):
    nombre: str
    telefono: str | None = None
    direccion: str | None = None

class ClienteCreate(ClienteBase):
    pass

class ClienteOut(ClienteBase):
    id: int

    class Config:
        from_attributes = True
