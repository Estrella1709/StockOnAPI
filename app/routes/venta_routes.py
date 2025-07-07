from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas.venta_schema import VentaCreate, VentaOut
from app.schemas import venta_schema
from app.models import models
from app.crud import venta_crud

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
