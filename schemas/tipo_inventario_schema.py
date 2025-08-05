from pydantic import BaseModel
from datetime import datetime

class TipoInventarioCreate(BaseModel):
    nombre: str

class TipoInventarioOut(BaseModel):
    id: int
    nombre: str
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True 
