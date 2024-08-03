from pydantic import BaseModel, Field, validator
import re

def validate_phone(v: str) -> str:
    if not re.match(r'^\d{10}$', v):
        raise ValueError('String should have at least 10 characters')
    return v

class NombreCliente(BaseModel):
    nombre: str
    apellido: str

class ClienteBase(BaseModel):
    nombreCliente: NombreCliente
    telefono: str = Field(..., min_length=10, max_length=10)
    edad: int = Field(..., gt=17)

    @validator('telefono')
    def validate_telefono(cls, v):
        return validate_phone(v)

    @validator('edad')
    def validar_edad(cls, v):
        if v < 18:
            raise ValueError('Input should be greater than 17')
        return v

class ClienteCreate(ClienteBase):
    pass

class Cliente(ClienteBase):
    class Config:
        orm_mode = True