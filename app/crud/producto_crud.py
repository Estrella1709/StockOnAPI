from sqlalchemy.orm import Session
from app.models.models import Producto
from app.schemas.producto_schema import ProductoCreate, ProductoUpdate

def crear_producto(db: Session, producto: ProductoCreate):
    nuevo_producto = Producto(**producto.dict())
    db.add(nuevo_producto)
    db.commit()
    db.refresh(nuevo_producto)
    return nuevo_producto

def obtener_productos_por_inventario(db: Session, id_inventario: int):
    return db.query(Producto).filter(Producto.id_inventario == id_inventario).all()

def obtener_producto_por_id(db: Session, producto_id: int):
    return db.query(Producto).filter(Producto.id == producto_id).first()

def actualizar_producto(db: Session, producto_id: int, producto_update: ProductoUpdate):
    producto = db.query(Producto).filter(Producto.id == producto_id).first()
    if not producto:
        return None
    for key, value in producto_update.dict(exclude_unset=True).items():
        setattr(producto, key, value)
    db.commit()
    db.refresh(producto)
    return producto

def eliminar_producto(db: Session, producto_id: int):
    producto = db.query(Producto).filter(Producto.id == producto_id).first()
    if not producto:
        return None
    db.delete(producto)
    db.commit()
    return producto
