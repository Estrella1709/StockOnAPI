from pydantic import BaseModel, EmailStr
from typing import Optional

class EmpresaCreate(BaseModel):
    numeroRegistro: str
    nombre: str
    tipo: str
    correo: EmailStr
    contrasena: str
    numTelefono: Optional[str] = None
    pais: Optional[str] = None
    region: Optional[str] = None
    direccion: Optional[str] = None

class EmpresaOut(BaseModel):
    id: int
    nombre: str
    correo: EmailStr

    model_config = {
        "from_attributes": True
    }