from pydantic import BaseModel, Field, validator
import re

def validate_phone(v: str) -> str:
    if not re.match(r'^\d{10}$', v):
        raise ValueError('El teléfono debe tener exactamente 10 dígitos')
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
            raise ValueError('El cliente debe ser mayor de 18 años')
        return v

class ClienteCreate(ClienteBase):
    pass

class Cliente(ClienteBase):
    class Config:
        orm_mode = True