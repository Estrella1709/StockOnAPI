from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class InventarioBase(BaseModel):
    nombre: str
    id_tipoInventario: int

class InventarioCreate(InventarioBase):
    id_empresa: int  

class InventarioUpdate(InventarioBase):
    pass

class InventarioOut(InventarioBase):
    id: int
    id_empresa: int
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True
