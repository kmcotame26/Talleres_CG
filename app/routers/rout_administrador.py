from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.database import get_db
from app.Modelos.mod_administrador import Administrador
from app.schemas.sch_administrador import AdministradorCreate, AdministradorOut
from typing import List

router = APIRouter(prefix="/administradores", tags=["Administradores"])

@router.post("/", response_model=AdministradorOut)
async def create_admin(a: AdministradorCreate, db: AsyncSession = Depends(get_db)):
    nuevo = Administrador(**a.dict())
    db.add(nuevo)
    await db.commit()
    await db.refresh(nuevo)
    return nuevo

@router.get("/", response_model=List[AdministradorOut])
async def list_admins(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Administrador))
    return result.scalars().all()

@router.get("/{admin_id}", response_model=AdministradorOut)
async def get_admin(admin_id: int, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Administrador).where(Administrador.id == admin_id))
    admin = result.scalar_one_or_none()
    if not admin:
        raise HTTPException(status_code=404, detail="Administrador no encontrado")
    return admin

@router.put("/{admin_id}", response_model=AdministradorOut)
async def update_admin(admin_id: int, data: AdministradorCreate, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Administrador).where(Administrador.id == admin_id))
    admin = result.scalar_one_or_none()
    if not admin:
        raise HTTPException(status_code=404, detail="Administrador no encontrado")
    for key, value in data.dict().items():
        setattr(admin, key, value)
    await db.commit()
    await db.refresh(admin)
    return admin

@router.delete("/{admin_id}")
async def delete_admin(admin_id: int, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Administrador).where(Administrador.id == admin_id))
    admin = result.scalar_one_or_none()
    if not admin:
        raise HTTPException(status_code=404, detail="Administrador no encontrado")
    await db.delete(admin)
    await db.commit()
    return {"ok": True}
