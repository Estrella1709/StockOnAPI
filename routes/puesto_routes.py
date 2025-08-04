from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from schemas import puesto_schema
from crud import puesto_crud
from database import get_db

router = APIRouter(prefix="/puestos", tags=["Puestos"])

@router.post("/", response_model=puesto_schema.PuestoOut)
def crear_puesto(puesto: puesto_schema.PuestoCreate, db: Session = Depends(get_db)):
    return puesto_crud.crear_puesto(db, puesto)

@router.get("/", response_model=list[puesto_schema.PuestoOut])
def obtener_puestos(db: Session = Depends(get_db)):
    return puesto_crud.obtener_puestos(db)

@router.get("/{puesto_id}", response_model=puesto_schema.PuestoOut)
def obtener_puesto(puesto_id: int, db: Session = Depends(get_db)):
    puesto = puesto_crud.obtener_puesto_por_id(db, puesto_id)
    if not puesto:
        raise HTTPException(status_code=404, detail="Puesto no encontrado")
    return puesto

@router.put("/{puesto_id}", response_model=puesto_schema.PuestoOut)
def actualizar_puesto(puesto_id: int, datos: puesto_schema.PuestoUpdate, db: Session = Depends(get_db)):
    puesto = puesto_crud.actualizar_puesto(db, puesto_id, datos)
    if not puesto:
        raise HTTPException(status_code=404, detail="Puesto no encontrado")
    return puesto

@router.delete("/{puesto_id}")
def eliminar_puesto(puesto_id: int, db: Session = Depends(get_db)):
    puesto = puesto_crud.eliminar_puesto(db, puesto_id)
    if not puesto:
        raise HTTPException(status_code=404, detail="Puesto no encontrado")
    return {"mensaje": "Puesto eliminado"}
