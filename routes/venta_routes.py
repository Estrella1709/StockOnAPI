from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from schemas.venta_schema import VentaCreate, VentaOut
from schemas import venta_schema
from models import models
from crud import venta_crud

router = APIRouter(
    prefix="/ventas",
    tags=["Ventas"]
)

@router.post("/", response_model=VentaOut)
def registrar_venta(venta: VentaCreate, db: Session = Depends(get_db)):
    return venta_crud.crear_venta(db, venta)

@router.get("/ventas/", response_model=list[venta_schema.VentaOut])
def obtener_ventas(db: Session = Depends(get_db)):
    ventas = db.query(models.Venta).all()
    return ventas
