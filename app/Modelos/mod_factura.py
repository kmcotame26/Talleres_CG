from sqlalchemy import Column, Integer, Float, Date, ForeignKey
from app.database import Base
from datetime import date
from sqlalchemy.orm import relationship

class Factura(Base):
    __tablename__ = "facturas"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    fecha = Column(Date, default=date.today)
    total = Column(Float, nullable=False)
    cliente_id = Column(Integer, ForeignKey("clientes.id"))


    trabajos = relationship("Trabajo", back_populates="factura")
