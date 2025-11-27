from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.database import get_db
from app.Modelos.mod_taller import Taller
from app.schemas.sch_taller import TallerCreate, TallerOut, TallerUpdate
from typing import List

router = APIRouter(prefix="/talleres", tags=["Talleres"])

@router.post("/", response_model=TallerOut)
async def create_taller(t: TallerCreate, db: AsyncSession = Depends(get_db)):
    nuevo = Taller(**t.dict())
    db.add(nuevo)
    await db.commit()
    await db.refresh(nuevo)
    return nuevo


@router.get("/", response_model=List[TallerOut])
async def get_talleres(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Taller))
    return result.scalars().all()


@router.get("/{taller_id}", response_model=TallerOut)
async def get_taller(taller_id: int, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Taller).where(Taller.id == taller_id))
    taller = result.scalars().first()
    if not taller:
        raise HTTPException(status_code=404, detail="Taller no encontrado")
    return taller


@router.put("/{taller_id}", response_model=TallerOut)
async def update_taller(taller_id: int, t: TallerUpdate, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Taller).where(Taller.id == taller_id))
    taller = result.scalars().first()
    if not taller:
        raise HTTPException(status_code=404, detail="Taller no encontrado")

    for key, value in t.dict(exclude_unset=True).items():
        setattr(taller, key, value)

    await db.commit()
    await db.refresh(taller)
    return taller


@router.delete("/{taller_id}")
async def delete_taller(taller_id: int, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Taller).where(Taller.id == taller_id))
    taller = result.scalars().first()
    if not taller:
        raise HTTPException(status_code=404, detail="Taller no encontrado")

    await db.delete(taller)
    await db.commit()
    return {"mensaje": "Taller eliminado correctamente"}
