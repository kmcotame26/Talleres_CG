from sqlalchemy import Column, Integer, String, Float, Date, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class Trabajo(Base):
    __tablename__ = "trabajos"

    id = Column(Integer, primary_key=True, index=True)
    descripcion = Column(String)
    sub_costo = Column(Float)
    lado = Column(String)
    fecha_finalizacion = Column(Date)


    vehiculo_id = Column(Integer, ForeignKey("vehiculos.id"))
    vehiculo = relationship("Vehiculo", back_populates="trabajos")

    # Relación: un trabajo pertenece a una factura
    factura_id = Column(Integer, ForeignKey("facturas.id"))
    factura = relationship("Factura", back_populates="trabajos")