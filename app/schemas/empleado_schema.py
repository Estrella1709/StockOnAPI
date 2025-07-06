from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime
from decimal import Decimal

class EmpleadoBase(BaseModel):
    nombre: str
    apellido: str
    correo: EmailStr
    telefono: str
    horario: str
    genero: str
    area: str
    salario: Decimal
    contrasena: str
    id_empresa: int
    id_puesto: int

class EmpleadoCreate(EmpleadoBase):
    pass

class EmpleadoUpdate(BaseModel):
    nombre: Optional[str]
    apellido: Optional[str]
    correo: Optional[EmailStr]
    telefono: Optional[str]
    horario: Optional[str]
    genero: Optional[str]
    area: Optional[str]
    salario: Optional[Decimal]
    contrasena: Optional[str]
    id_puesto: Optional[int]

class EmpleadoOut(EmpleadoBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True
