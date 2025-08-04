from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
from schemas.tipo_inventario_schema import TipoInventarioCreate, TipoInventarioOut
from crud import tipo_inventario_crud

router = APIRouter(prefix="/tipo-inventario", tags=["Tipo Inventario"])

@router.post("/", response_model=TipoInventarioOut)
def create_tipo(tipo: TipoInventarioCreate, db: Session = Depends(get_db)):
    return tipo_inventario_crud.create_tipo_inventario(db, tipo)

@router.get("/", response_model=list[TipoInventarioOut])
def list_tipos(db: Session = Depends(get_db)):
    return tipo_inventario_crud.get_tipos_inventario(db)
