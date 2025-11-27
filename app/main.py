from fastapi import FastAPI
from app.database import engine, Base
import asyncio

from app.routers import (
    rout_usuario,
    rout_cliente,
    rout_administrador,
    rout_taller,
    rout_trabajo,
    rout_vehiculo,
    rout_factura,
)

app = FastAPI(title="Taller de Latonería y Pintura", version="1.0")

async def create_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    print("✅ Tablas creadas o verificadas correctamente.")

@app.on_event("startup")
async def startup_event():
    await create_tables()

# 🔹 Registrar routers
app.include_router(rout_usuario.router, prefix="/usuarios", tags=["Usuarios"])
app.include_router(rout_cliente.router, prefix="/clientes", tags=["Clientes"])
app.include_router(rout_administrador.router, prefix="/administradores", tags=["Administradores"])
app.include_router(rout_taller.router, prefix="/talleres", tags=["Talleres"])
app.include_router(rout_trabajo.router, prefix="/trabajos", tags=["Trabajos"])
app.include_router(rout_vehiculo.router, prefix="/vehiculos", tags=["Vehículos"])
app.include_router(rout_factura.router, prefix="/facturas", tags=["Facturas"])

@app.get("/")
async def root():
    return {"mensaje": "🚗 Bienvenido al sistema del Taller de Latonería y Pintura"}

# 🔹 Solo si lo corres directamente (opcional en PyCharm)
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="127.0.0.1", port=8000, reload=True)
