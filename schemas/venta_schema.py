from pydantic import BaseModel
from typing import List
from datetime import datetime

class DetalleVenta(BaseModel):
    id_producto: int
    cantidad: int
    precio: float

class VentaCreate(BaseModel):
    productos: List[DetalleVenta]
    id_empresa: int

class VentaOut(BaseModel):
    id: int
    precioTotal: float
    fecha: datetime

    class Config:
        from_attributes = True
