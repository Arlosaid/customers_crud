from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.api import schemas, repository
from app.db.database import get_db

router = APIRouter()

@router.post("/clientes/", response_model=schemas.Cliente)
def create_cliente(cliente: schemas.ClienteCreate, db: Session = Depends(get_db)):
    db_cliente = repository.get_cliente(db, telefono=cliente.telefono)
    if db_cliente:
        raise HTTPException(status_code=400, detail="Teléfono ya registrado")
    db_cliente = repository.create_cliente(db=db, cliente=cliente)
    # Convertir al modelo Pydantic
    return schemas.Cliente(
        nombreCliente=schemas.NombreCliente(nombre=db_cliente.nombre, apellido=db_cliente.apellido),
        telefono=db_cliente.telefono,
        edad=db_cliente.edad
    )

@router.get("/clientes/{telefono}", response_model=schemas.Cliente)
def read_cliente(telefono: str, db: Session = Depends(get_db)):
    db_cliente = repository.get_cliente(db, telefono=telefono)
    if db_cliente is None:
        raise HTTPException(status_code=404, detail="Cliente no encontrado")
    # Convertir al modelo Pydantic
    return schemas.Cliente(
        nombreCliente=schemas.NombreCliente(nombre=db_cliente.nombre, apellido=db_cliente.apellido),
        telefono=db_cliente.telefono,
        edad=db_cliente.edad
    )

@router.put("/clientes/{telefono}", response_model=schemas.Cliente)
def update_cliente(telefono: str, cliente: schemas.ClienteCreate, db: Session = Depends(get_db)):
    db_cliente = repository.update_cliente(db, telefono=telefono, cliente=cliente)
    if db_cliente is None:
        raise HTTPException(status_code=404, detail="Cliente no encontrado")
    # Convertir al modelo Pydantic
    return schemas.Cliente(
        nombreCliente=schemas.NombreCliente(nombre=db_cliente.nombre, apellido=db_cliente.apellido),
        telefono=db_cliente.telefono,
        edad=db_cliente.edad
    )

@router.delete("/clientes/{telefono}", response_model=schemas.Cliente)
def delete_cliente(telefono: str, db: Session = Depends(get_db)):
    db_cliente = repository.delete_cliente(db, telefono=telefono)
    if db_cliente is None:
        raise HTTPException(status_code=404, detail="Cliente no encontrado")
    # Convertir al modelo Pydantic
    return schemas.Cliente(
        nombreCliente=schemas.NombreCliente(nombre=db_cliente.nombre, apellido=db_cliente.apellido),
        telefono=db_cliente.telefono,
        edad=db_cliente.edad
    )
