from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.database import get_db
from app.Modelos.mod_vehiculo import Vehiculo
from app.schemas.sch_vehiculo import VehiculoCreate, VehiculoOut
from typing import List

router = APIRouter(prefix="/vehiculos", tags=["Vehiculos"])

@router.post("/", response_model=VehiculoOut)
async def create_vehiculo(v: VehiculoCreate, db: AsyncSession = Depends(get_db)):
    nuevo = Vehiculo(**v.dict())
    db.add(nuevo)
    await db.commit()
    await db.refresh(nuevo)
    return nuevo

@router.get("/", response_model=List[VehiculoOut])
async def get_vehiculos(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Vehiculo))
    return result.scalars().all()

@router.get("/{vehiculo_id}", response_model=VehiculoOut)
async def get_vehiculo(vehiculo_id: int, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Vehiculo).where(Vehiculo.id == vehiculo_id))
    vehiculo = result.scalar_one_or_none()
    if not vehiculo:
        raise HTTPException(status_code=404, detail="Vehículo no encontrado")
    return vehiculo

@router.delete("/{vehiculo_id}")
async def delete_vehiculo(vehiculo_id: int, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Vehiculo).where(Vehiculo.id == vehiculo_id))
    vehiculo = result.scalar_one_or_none()
    if not vehiculo:
        raise HTTPException(status_code=404, detail="Vehículo no encontrado")
    await db.delete(vehiculo)
    await db.commit()
    return {"message": "Vehículo eliminado correctamente"}
