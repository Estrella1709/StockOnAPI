from sqlalchemy.orm import Session
from models.models import TipoInventario
from schemas.tipo_inventario_schema import TipoInventarioCreate

def create_tipo_inventario(db: Session, tipo_data: TipoInventarioCreate):
    nuevo_tipo = TipoInventario(nombre=tipo_data.nombre)
    db.add(nuevo_tipo)
    db.commit()
    db.refresh(nuevo_tipo)
    return nuevo_tipo

def get_tipos_inventario(db: Session):
    return db.query(TipoInventario).all()
