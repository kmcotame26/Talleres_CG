from pydantic import BaseModel

class UsuarioBase(BaseModel):
    nombre: str
    correo: str
    contraseña: str

class UsuarioCreate(UsuarioBase):
    pass

class UsuarioOut(UsuarioBase):
    id: int

    class Config:
        from_attributes = True
