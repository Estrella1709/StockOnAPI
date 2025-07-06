from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas.venta_schema import VentaCreate, VentaOut
from app.crud import venta_crud

router = APIRouter(
    prefix="/ventas",
    tags=["Ventas"]
)

@router.post("/", response_model=VentaOut)
def registrar_venta(venta: VentaCreate, db: Session = Depends(get_db)):
    return venta_crud.crear_venta(db, venta)
