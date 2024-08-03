from sqlalchemy import Column, String, Integer
from .database import Base

class Customer(Base):
    __tablename__ = "customer"

    telefono = Column(String(10), primary_key=True, index=True)
    nombre = Column(String(50))
    apellido = Column(String(50))
    edad = Column(Integer)
