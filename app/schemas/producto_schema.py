from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class ProductoBase(BaseModel):
    nombre: str
    precioUnitario: float
    dimensiones: Optional[str] = None
    peso: Optional[float] = None
    cantidad: int
    caracteristicas: Optional[str] = None
    codigoBarras: Optional[str] = None
    material: Optional[str] = None
    id_inventario: int

class ProductoCreate(ProductoBase):
    pass

class ProductoUpdate(BaseModel):
    nombre: Optional[str] = None
    precioUnitario: Optional[float] = None
    dimensiones: Optional[str] = None
    peso: Optional[float] = None
    cantidad: Optional[int] = None
    caracteristicas: Optional[str] = None
    codigoBarras: Optional[str] = None
    material: Optional[str] = None

class ProductoOut(ProductoBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True
