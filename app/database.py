from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = "sqlite+aiosqlite:///C:/Users/karol/Proyecto_Taller/identifier.sqlite"



engine = create_async_engine(DATABASE_URL, echo=False, future=True)


async_session = sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False
)

# 🔹 Base para todos los modelos
Base = declarative_base()

# 🔹 Dependencia para obtener la sesión en cada petición
async def get_db():
    async with async_session() as session:
        yield session
