from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.database import get_db
from app.Modelos.mod_factura import Factura
from app.schemas.sch_factura import FacturaCreate, FacturaOut
from typing import List

router = APIRouter(prefix="/facturas", tags=["Facturas"])

@router.post("/", response_model=FacturaOut)
async def create_factura(f: FacturaCreate, db: AsyncSession = Depends(get_db)):
    nuevo = Factura(**f.dict())
    db.add(nuevo)
    await db.commit()
    await db.refresh(nuevo)
    return nuevo

@router.get("/", response_model=List[FacturaOut])
async def get_facturas(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Factura))
    return result.scalars().all()

@router.get("/{factura_id}", response_model=FacturaOut)
async def get_factura(factura_id: int, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Factura).where(Factura.id == factura_id))
    factura = result.scalar_one_or_none()
    if not factura:
        raise HTTPException(status_code=404, detail="Factura no encontrada")
    return factura

@router.delete("/{factura_id}")
async def delete_factura(factura_id: int, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Factura).where(Factura.id == factura_id))
    factura = result.scalar_one_or_none()
    if not factura:
        raise HTTPException(status_code=404, detail="Factura no encontrada")
    await db.delete(factura)
    await db.commit()
    return {"message": "Factura eliminada correctamente"}
