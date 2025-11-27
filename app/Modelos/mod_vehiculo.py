from sqlalchemy import Column, Integer, String, ForeignKey
from app.database import Base
from sqlalchemy.orm import relationship

class Vehiculo(Base):
    __tablename__ = "vehiculos"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    marca = Column(String(100), nullable=False)
    modelo = Column(String(100), nullable=False)
    placa = Column(String(20), unique=True, nullable=False)
    cliente_id = Column(Integer, ForeignKey("clientes.id"))

    cliente_id = Column(Integer, ForeignKey("clientes.id"))
    cliente = relationship("Cliente", back_populates="vehiculos")

    # Relación: un vehículo tiene muchos trabajos
    trabajos = relationship("Trabajo", back_populates="vehiculo")
