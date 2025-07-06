from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.crud import inventario_crud as crud
from app.schemas import inventario_schema as schema

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=schema.InventarioOut)
def crear(inventario: schema.InventarioCreate, db: Session = Depends(get_db)):
    return crud.crear_inventario(db, inventario)

@router.get("/empresa/{empresa_id}", response_model=list[schema.InventarioOut])
def listar(empresa_id: int, db: Session = Depends(get_db)):
    return crud.obtener_inventarios_por_empresa(db, empresa_id)

@router.put("/{inventario_id}", response_model=schema.InventarioOut)
def actualizar(inventario_id: int, data: schema.InventarioUpdate, db: Session = Depends(get_db)):
    inventario = crud.actualizar_inventario(db, inventario_id, data)
    if not inventario:
        raise HTTPException(status_code=404, detail="Inventario no encontrado")
    return inventario

@router.delete("/{inventario_id}")
def eliminar(inventario_id: int, db: Session = Depends(get_db)):
    inventario = crud.eliminar_inventario(db, inventario_id)
    if not inventario:
        raise HTTPException(status_code=404, detail="Inventario no encontrado")
    return {"message": "Inventario eliminado"}
