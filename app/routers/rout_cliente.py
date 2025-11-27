from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.database import get_db
from app.Modelos.mod_cliente import Cliente
from app.schemas.sch_cliente import ClienteCreate, ClienteOut
from typing import List

router = APIRouter(prefix="/clientes", tags=["Clientes"])

@router.post("/", response_model=ClienteOut)
async def create_cliente(c: ClienteCreate, db: AsyncSession = Depends(get_db)):
    nuevo = Cliente(**c.dict())
    db.add(nuevo)
    await db.commit()
    await db.refresh(nuevo)
    return nuevo

@router.get("/", response_model=List[ClienteOut])
async def list_clientes(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Cliente))
    return result.scalars().all()

@router.get("/{cliente_id}", response_model=ClienteOut)
async def get_cliente(cliente_id: int, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Cliente).where(Cliente.id == cliente_id))
    cliente = result.scalar_one_or_none()
    if not cliente:
        raise HTTPException(status_code=404, detail="Cliente no encontrado")
    return cliente

@router.put("/{cliente_id}", response_model=ClienteOut)
async def update_cliente(cliente_id: int, data: ClienteCreate, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Cliente).where(Cliente.id == cliente_id))
    cliente = result.scalar_one_or_none()
    if not cliente:
        raise HTTPException(status_code=404, detail="Cliente no encontrado")
    for key, value in data.dict().items():
        setattr(cliente, key, value)
    await db.commit()
    await db.refresh(cliente)
    return cliente

@router.delete("/{cliente_id}")
async def delete_cliente(cliente_id: int, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Cliente).where(Cliente.id == cliente_id))
    cliente = result.scalar_one_or_none()
    if not cliente:
        raise HTTPException(status_code=404, detail="Cliente no encontrado")
    await db.delete(cliente)
    await db.commit()
    return {"ok": True}
