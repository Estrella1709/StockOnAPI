from sqlalchemy.orm import Session
from app.models.models import Inventario
from app.schemas.inventario_schema import InventarioCreate, InventarioUpdate

def crear_inventario(db: Session, inventario: InventarioCreate):
    nuevo = Inventario(**inventario.dict())
    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)
    return nuevo

def obtener_inventarios_por_empresa(db: Session, empresa_id: int):
    return db.query(Inventario).filter(Inventario.id_empresa == empresa_id).all()

def obtener_inventario(db: Session, inventario_id: int):
    return db.query(Inventario).filter(Inventario.id == inventario_id).first()

def actualizar_inventario(db: Session, inventario_id: int, datos: InventarioUpdate):
    inv = obtener_inventario(db, inventario_id)
    if inv:
        for key, value in datos.dict().items():
            setattr(inv, key, value)
        db.commit()
        db.refresh(inv)
    return inv

def eliminar_inventario(db: Session, inventario_id: int):
    inv = obtener_inventario(db, inventario_id)
    if inv:
        db.delete(inv)
        db.commit()
    return inv
