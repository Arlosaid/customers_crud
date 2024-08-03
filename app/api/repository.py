from sqlalchemy.orm import Session
from app.db import model
from app.api import schemas

def get_cliente(db: Session, telefono: str):
    return db.query(model.Customer).filter(model.Customer.telefono == telefono).first()

def create_cliente(db: Session, cliente: schemas.ClienteCreate):
    db_cliente = model.Customer(
        telefono=cliente.telefono,
        nombre=cliente.nombreCliente.nombre,
        apellido=cliente.nombreCliente.apellido,
        edad=cliente.edad
    )
    db.add(db_cliente)
    db.commit()
    db.refresh(db_cliente)
    return db_cliente

def update_cliente(db: Session, telefono: str, cliente: schemas.ClienteCreate):
    db_cliente = get_cliente(db, telefono)
    if db_cliente:
        db_cliente.nombre = cliente.nombreCliente.nombre
        db_cliente.apellido = cliente.nombreCliente.apellido
        db_cliente.edad = cliente.edad
        db.commit()
        db.refresh(db_cliente)
    return db_cliente

def delete_cliente(db: Session, telefono: str):
    db_cliente = get_cliente(db, telefono)
    if db_cliente:
        db.delete(db_cliente)
        db.commit()
    return db_cliente
