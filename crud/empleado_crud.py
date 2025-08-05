from sqlalchemy.orm import Session
from models.models import Empleado
from schemas.empleado_schema import EmpleadoCreate, EmpleadoUpdate

def crear_empleado(db: Session, datos: EmpleadoCreate):
    nuevo = Empleado(**datos.dict())
    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)
    return nuevo

def obtener_empleados(db: Session):
    return db.query(Empleado).all()

def obtener_empleado_por_id(db: Session, empleado_id: int):
    return db.query(Empleado).filter(Empleado.id == empleado_id).first()

def actualizar_empleado(db: Session, empleado_id: int, datos: EmpleadoUpdate):
    empleado = db.query(Empleado).filter(Empleado.id == empleado_id).first()
    if not empleado:
        return None
    for key, value in datos.dict(exclude_unset=True).items():
        setattr(empleado, key, value)
    db.commit()
    db.refresh(empleado)
    return empleado

def eliminar_empleado(db: Session, empleado_id: int):
    empleado = db.query(Empleado).filter(Empleado.id == empleado_id).first()
    if not empleado:
        return None
    db.delete(empleado)
    db.commit()
    return empleado
