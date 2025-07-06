from sqlalchemy.orm import Session
from app.models.models import Puesto
from app.schemas.puesto_schema import PuestoCreate, PuestoUpdate

def crear_puesto(db: Session, puesto: PuestoCreate):
    nuevo_puesto = Puesto(**puesto.dict())
    db.add(nuevo_puesto)
    db.commit()
    db.refresh(nuevo_puesto)
    return nuevo_puesto

def obtener_puestos(db: Session):
    return db.query(Puesto).all()

def obtener_puesto_por_id(db: Session, puesto_id: int):
    return db.query(Puesto).filter(Puesto.id == puesto_id).first()

def actualizar_puesto(db: Session, puesto_id: int, datos: PuestoUpdate):
    puesto = db.query(Puesto).filter(Puesto.id == puesto_id).first()
    if not puesto:
        return None
    for key, value in datos.dict(exclude_unset=True).items():
        setattr(puesto, key, value)
    db.commit()
    db.refresh(puesto)
    return puesto

def eliminar_puesto(db: Session, puesto_id: int):
    puesto = db.query(Puesto).filter(Puesto.id == puesto_id).first()
    if not puesto:
        return None
    db.delete(puesto)
    db.commit()
    return puesto
