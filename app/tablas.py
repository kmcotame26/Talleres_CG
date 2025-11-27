# app/tablas.py
import asyncio
from app.database import Base, engine
from app.Modelos.mod_administrador import Administrador
from app.Modelos.mod_vehiculo import Vehiculo
from app.Modelos.mod_taller import Taller
from app.Modelos.mod_trabajo import Trabajo
from app.Modelos.mod_factura import Factura

async def create_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    print("✅ Tablas creadas exitosamente en la base de datos.")

if __name__ == "__main__":
    asyncio.run(create_tables())
