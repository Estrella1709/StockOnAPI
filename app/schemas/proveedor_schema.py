from pydantic import BaseModel, EmailStr, Field
from datetime import datetime

class ProveedorBase(BaseModel):
    nombre: str
    correo: EmailStr
    numTelefono: str = Field(..., alias="num_telefono")
    tipoProducto: str = Field(..., alias="tipo_producto")
    condicionesPago: str = Field(..., alias="condiciones_pago")
    frecuenciaSuministro: str = Field(..., alias="frecuencia_suministro")
    horarioAtencion: str = Field(..., alias="horario_atencion")
    pais: str
    ciudad: str
    id_empresa: int

    class Config:
        populate_by_name = True
        from_attributes = True

class ProveedorCreate(ProveedorBase):
    pass

class ProveedorUpdate(BaseModel):
    nombre: str | None = None
    correo: EmailStr | None = None
    numTelefono: str | None = None
    tipoProducto: str | None = None
    condicionesPago: str | None = None
    frecuenciaSuministro: str | None = None
    horarioAtencion: str | None = None
    pais: str | None = None
    ciudad: str | None = None

class ProveedorOut(ProveedorBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True