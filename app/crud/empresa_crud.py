from sqlalchemy.orm import Session
from app.models.models import Empresa
from app.schemas.empresa_schema import EmpresaCreate
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_empresa_by_correo(db: Session, correo: str):
    return db.query(Empresa).filter(Empresa.correo == correo).first()

def create_empresa(db: Session, empresa: EmpresaCreate):
    hashed_password = pwd_context.hash(empresa.contrasena)
    db_empresa = Empresa(
        numeroRegistro=empresa.numeroRegistro,
        nombre=empresa.nombre,
        tipo=empresa.tipo,
        correo=empresa.correo,
        contrasena=hashed_password,
        numTelefono=empresa.numTelefono,
        pais=empresa.pais,
        region=empresa.region,
        direccion=empresa.direccion
    )
    db.add(db_empresa)
    db.commit()
    db.refresh(db_empresa)
    return db_empresa

def authenticate_empresa(db: Session, correo: str, contrasena: str):
    empresa = get_empresa_by_correo(db, correo)
    if not empresa:
        return None
    if not pwd_context.verify(contrasena, empresa.contrasena):
        return None
    return empresa
