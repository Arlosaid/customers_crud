from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from fastapi import status

from app.api import schemas, repository
from app.db.database import get_db

router = APIRouter()

@router.post("/customers", response_model=schemas.Cliente, status_code=status.HTTP_201_CREATED)
def create_cliente(customer: schemas.CustomerCreate, db: Session = Depends(get_db)):
    db_cliente = repository.get_cliente(db, telefono=customer.telefono)
    if db_cliente:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Phone already registered")
    db_cliente = repository.create_cliente(db=db, customer=customer)
    return schemas.Cliente(
        nombreCliente=schemas.CustomerName(nombre=db_cliente.nombre, apellido=db_cliente.apellido),
        telefono=db_cliente.telefono,
        edad=db_cliente.edad
    )

@router.get("/customers/{phone}", response_model=schemas.Cliente)
def read_cliente(telefono: str, db: Session = Depends(get_db)):
    db_cliente = repository.get_cliente(db, telefono=telefono)
    if db_cliente is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Customer not found")
    return schemas.Cliente(
        nombreCliente=schemas.CustomerName(nombre=db_cliente.nombre, apellido=db_cliente.apellido),
        telefono=db_cliente.telefono,
        edad=db_cliente.edad
    )

@router.put("/customers/{phone}", response_model=schemas.Cliente)
def update_cliente(telefono: str, customer: schemas.CustomerCreate, db: Session = Depends(get_db)):
    db_cliente = repository.update_cliente(db, telefono=telefono, customer=customer)
    if db_cliente is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Customer not found")
    return schemas.Cliente(
        nombreCliente=schemas.CustomerName(nombre=db_cliente.nombre, apellido=db_cliente.apellido),
        telefono=db_cliente.telefono,
        edad=db_cliente.edad
    )

@router.delete("/customers/{phone}", response_model=None,status_code=status.HTTP_204_NO_CONTENT)
def delete_cliente(telefono: str, db: Session = Depends(get_db)):
    db_cliente = repository.delete_cliente(db, telefono=telefono)
    if db_cliente is None:
        raise HTTPException(status_code=404, detail="Customer not found")
    return None
