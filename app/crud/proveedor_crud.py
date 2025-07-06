from sqlalchemy.orm import Session
from app.models.models import Proveedor
from app.schemas.proveedor_schema import ProveedorCreate, ProveedorUpdate

def crear_proveedor(db: Session, proveedor: ProveedorCreate):
    nuevo_proveedor = Proveedor(**proveedor.model_dump(by_alias=True))
    db.add(nuevo_proveedor)
    db.commit()
    db.refresh(nuevo_proveedor)
    return nuevo_proveedor

def obtener_proveedores(db: Session, id_empresa: int):
    return db.query(Proveedor).filter(Proveedor.id_empresa == id_empresa).all()

def obtener_proveedor_por_id(db: Session, proveedor_id: int):
    return db.query(Proveedor).filter(Proveedor.id == proveedor_id).first()

def actualizar_proveedor(db: Session, proveedor_id: int, proveedor_update: ProveedorUpdate):
    proveedor = db.query(Proveedor).filter(Proveedor.id == proveedor_id).first()
    if not proveedor:
        return None
    for key, value in proveedor_update.dict(exclude_unset=True).items():
        setattr(proveedor, key, value)
    db.commit()
    db.refresh(proveedor)
    return proveedor

def eliminar_proveedor(db: Session, proveedor_id: int):
    proveedor = db.query(Proveedor).filter(Proveedor.id == proveedor_id).first()
    if not proveedor:
        return None
    db.delete(proveedor)
    db.commit()
    return proveedor