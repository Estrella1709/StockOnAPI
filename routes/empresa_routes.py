from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal
from schemas import empresa_schema
import crud.empresa_crud as empresa_crud

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/register", response_model=empresa_schema.EmpresaOut)
def register_empresa(empresa: empresa_schema.EmpresaCreate, db: Session = Depends(get_db)):
    db_empresa = empresa_crud.get_empresa_by_correo(db, empresa.correo)
    if db_empresa:
        raise HTTPException(status_code=400, detail="Correo ya registrado")
    return empresa_crud.create_empresa(db, empresa)

@router.post("/login")
def login_empresa(correo: str, contrasena: str, db: Session = Depends(get_db)):
    empresa = empresa_crud.authenticate_empresa(db, correo, contrasena)
    if not empresa:
        raise HTTPException(status_code=401, detail="Credenciales inválidas")
    return {"message": "Login exitoso", "empresa_id": empresa.id}
