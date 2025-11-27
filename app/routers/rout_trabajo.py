from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.database import get_db
from app.Modelos.mod_trabajo import Trabajo
from app.schemas.sch_trabajo import TrabajoCreate, TrabajoOut, TrabajoUpdate
from typing import List

router = APIRouter(prefix="/trabajos", tags=["Trabajos"])

@router.post("/", response_model=TrabajoOut)
async def create_trabajo(t: TrabajoCreate, db: AsyncSession = Depends(get_db)):
    nuevo = Trabajo(**t.dict())
    db.add(nuevo)
    await db.commit()
    await db.refresh(nuevo)
    return nuevo


@router.get("/", response_model=List[TrabajoOut])
async def get_trabajos(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Trabajo))
    return result.scalars().all()


@router.get("/{trabajo_id}", response_model=TrabajoOut)
async def get_trabajo(trabajo_id: int, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Trabajo).where(Trabajo.id == trabajo_id))
    trabajo = result.scalars().first()
    if not trabajo:
        raise HTTPException(status_code=404, detail="Trabajo no encontrado")
    return trabajo


@router.put("/{trabajo_id}", response_model=TrabajoOut)
async def update_trabajo(trabajo_id: int, t: TrabajoUpdate, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Trabajo).where(Trabajo.id == trabajo_id))
    trabajo = result.scalars().first()
    if not trabajo:
        raise HTTPException(status_code=404, detail="Trabajo no encontrado")

    for key, value in t.dict(exclude_unset=True).items():
        setattr(trabajo, key, value)

    await db.commit()
    await db.refresh(trabajo)
    return trabajo


@router.delete("/{trabajo_id}")
async def delete_trabajo(trabajo_id: int, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Trabajo).where(Trabajo.id == trabajo_id))
    trabajo = result.scalars().first()
    if not trabajo:
        raise HTTPException(status_code=404, detail="Trabajo no encontrado")

    await db.delete(trabajo)
    await db.commit()
    return {"mensaje": "Trabajo eliminado correctamente"}
