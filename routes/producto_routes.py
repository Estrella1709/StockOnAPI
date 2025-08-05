from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from crud import producto_crud  
from schemas.producto_schema import ProductoCreate, ProductoUpdate, ProductoOut

router = APIRouter(
    prefix="/productos",
    tags=["Productos"]
)

@router.post("/", response_model=ProductoOut)
def crear_producto(producto: ProductoCreate, db: Session = Depends(get_db)):
    return producto_crud.crear_producto(db, producto)

@router.get("/inventario/{id_inventario}", response_model=list[ProductoOut])
def obtener_productos(id_inventario: int, db: Session = Depends(get_db)):
    return producto_crud.obtener_productos_por_inventario(db, id_inventario)

@router.get("/{producto_id}", response_model=ProductoOut)
def obtener_producto(producto_id: int, db: Session = Depends(get_db)):
    producto = producto_crud.obtener_producto_por_id(db, producto_id)
    if not producto:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return producto

@router.put("/{producto_id}", response_model=ProductoOut)
def actualizar_producto(producto_id: int, producto: ProductoUpdate, db: Session = Depends(get_db)):
    producto_actualizado = producto_crud.actualizar_producto(db, producto_id, producto)
    if not producto_actualizado:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return producto_actualizado

@router.delete("/{producto_id}")
def eliminar_producto(producto_id: int, db: Session = Depends(get_db)):
    producto_eliminado = producto_crud.eliminar_producto(db, producto_id)
    if not producto_eliminado:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return {"message": "Producto eliminado correctamente"}
