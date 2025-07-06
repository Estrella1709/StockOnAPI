from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class PuestoBase(BaseModel):
    nombre: str
    id_empresa: int

class PuestoCreate(PuestoBase):
    pass

class PuestoUpdate(BaseModel):
    nombre: Optional[str] = None

class PuestoOut(PuestoBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True
