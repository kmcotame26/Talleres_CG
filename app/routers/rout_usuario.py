from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.database import get_db
from app.Modelos.mod_usuario import Usuario
from app.schemas.sch_usuario import UsuarioCreate, UsuarioOut
from typing import List

router = APIRouter(prefix="/usuarios", tags=["Usuarios"])

@router.post("/", response_model=UsuarioOut)
async def create_usuario(u: UsuarioCreate, db: AsyncSession = Depends(get_db)):
    nuevo = Usuario(**u.dict())
    db.add(nuevo)
    await db.commit()
    await db.refresh(nuevo)
    return nuevo

@router.get("/", response_model=List[UsuarioOut])
async def list_usuarios(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Usuario))
    return result.scalars().all()

@router.get("/{usuario_id}", response_model=UsuarioOut)
async def get_usuario(usuario_id: int, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Usuario).where(Usuario.id == usuario_id))
    usuario = result.scalar_one_or_none()
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return usuario

@router.put("/{usuario_id}", response_model=UsuarioOut)
async def update_usuario(usuario_id: int, data: UsuarioCreate, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Usuario).where(Usuario.id == usuario_id))
    usuario = result.scalar_one_or_none()
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    for key, value in data.dict().items():
        setattr(usuario, key, value)
    await db.commit()
    await db.refresh(usuario)
    return usuario

@router.delete("/{usuario_id}")
async def delete_usuario(usuario_id: int, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Usuario).where(Usuario.id == usuario_id))
    usuario = result.scalar_one_or_none()
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    await db.delete(usuario)
    await db.commit()
    return {"ok": True}

from sqlalchemy import func

@router.get("/buscar/{nombre}", response_model=UsuarioOut)
async def buscar_usuario_por_nombre(nombre: str, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Usuario).where(Usuario.nombre == nombre))
    usuario = result.scalar_one_or_none()
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return usuario