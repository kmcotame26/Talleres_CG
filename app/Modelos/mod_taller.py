from sqlalchemy import Column, Integer, String, ForeignKey
from app.database import Base

class Taller(Base):
    __tablename__ = "talleres"

    id = Column(Integer, primary_key=True, index=True)
    id_trabajo = Column(Integer, ForeignKey("trabajos.id"))
    lado_arreglar = Column(String)
    estado = Column(String)  # "en arreglo" o "finalizado"
