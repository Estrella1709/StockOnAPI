from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas.proveedor_schema import ProveedorCreate, ProveedorUpdate, ProveedorOut
from app.crud import proveedor_crud

router = APIRouter(
    prefix="/proveedores",
    tags=["Proveedores"]
)

@router.post("/", response_model=ProveedorOut)
def crear_proveedor(proveedor: ProveedorCreate, db: Session = Depends(get_db)):
    return proveedor_crud.crear_proveedor(db, proveedor)

@router.get("/empresa/{id_empresa}", response_model=list[ProveedorOut])
def obtener_proveedores(id_empresa: int, db: Session = Depends(get_db)):
    return proveedor_crud.obtener_proveedores(db, id_empresa)

@router.get("/{proveedor_id}", response_model=ProveedorOut)
def obtener_proveedor(proveedor_id: int, db: Session = Depends(get_db)):
    proveedor = proveedor_crud.obtener_proveedor_por_id(db, proveedor_id)
    if not proveedor:
        raise HTTPException(status_code=404, detail="Proveedor no encontrado")
    return proveedor

@router.put("/{proveedor_id}", response_model=ProveedorOut)
def actualizar_proveedor(proveedor_id: int, proveedor: ProveedorUpdate, db: Session = Depends(get_db)):
    actualizado = proveedor_crud.actualizar_proveedor(db, proveedor_id, proveedor)
    if not actualizado:
        raise HTTPException(status_code=404, detail="Proveedor no encontrado")
    return actualizado

@router.delete("/{proveedor_id}")
def eliminar_proveedor(proveedor_id: int, db: Session = Depends(get_db)):
    eliminado = proveedor_crud.eliminar_proveedor(db, proveedor_id)
    if not eliminado:
        raise HTTPException(status_code=404, detail="Proveedor no encontrado")
    return {"message": "Proveedor eliminado correctamente"}
