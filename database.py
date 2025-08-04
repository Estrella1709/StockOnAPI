from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from dotenv import load_dotenv
import os

# Cargar variables del archivo .env
load_dotenv()

# Obtener variables de entorno
DB_TYPE = os.getenv("DB_TYPE", "sqlite")  # por defecto sqlite
DB_NAME = os.getenv("DB_NAME", "mi_api.db")
DB_USER = os.getenv("DB_USER", "")
DB_PASSWORD = os.getenv("DB_PASSWORD", "")
DB_HOST = os.getenv("DB_HOST", "")
DB_PORT = os.getenv("DB_PORT", "")

# Construir DATABASE_URL según el tipo de base de datos
if DB_TYPE == "sqlite":
    DATABASE_URL = f"sqlite:///./{DB_NAME}"
    connect_args = {"check_same_thread": False}
elif DB_TYPE == "postgresql":
    DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    connect_args = {}
elif DB_TYPE == "mysql":
    DATABASE_URL = f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    connect_args = {}
else:
    raise ValueError(f"Tipo de base de datos no soportado: {DB_TYPE}")

# Crear engine
engine = create_engine(DATABASE_URL, connect_args=connect_args)

# Crear sesión y base
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Función para obtener la sesión
def get_db():
    db: Session = SessionLocal()
    try:
        yield db
    finally:
        db.close()
