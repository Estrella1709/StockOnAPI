from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from schemas import empleado_schema
from crud import empleado_crud

router = APIRouter(prefix="/empleados", tags=["Empleados"])

@router.post("/", response_model=empleado_schema.EmpleadoOut)
def crear_empleado(datos: empleado_schema.EmpleadoCreate, db: Session = Depends(get_db)):
    return empleado_crud.crear_empleado(db, datos)

@router.get("/", response_model=list[empleado_schema.EmpleadoOut])
def obtener_empleados(db: Session = Depends(get_db)):
    return empleado_crud.obtener_empleados(db)

@router.get("/{empleado_id}", response_model=empleado_schema.EmpleadoOut)
def obtener_empleado(empleado_id: int, db: Session = Depends(get_db)):
    empleado = empleado_crud.obtener_empleado_por_id(db, empleado_id)
    if not empleado:
        raise HTTPException(status_code=404, detail="Empleado no encontrado")
    return empleado

@router.put("/{empleado_id}", response_model=empleado_schema.EmpleadoOut)
def actualizar_empleado(empleado_id: int, datos: empleado_schema.EmpleadoUpdate, db: Session = Depends(get_db)):
    empleado = empleado_crud.actualizar_empleado(db, empleado_id, datos)
    if not empleado:
        raise HTTPException(status_code=404, detail="Empleado no encontrado")
    return empleado

@router.delete("/{empleado_id}")
def eliminar_empleado(empleado_id: int, db: Session = Depends(get_db)):
    empleado = empleado_crud.eliminar_empleado(db, empleado_id)
    if not empleado:
        raise HTTPException(status_code=404, detail="Empleado no encontrado")
    return {"mensaje": "Empleado eliminado"}
