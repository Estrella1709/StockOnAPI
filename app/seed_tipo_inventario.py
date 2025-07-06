from app.models.models import TipoInventario
from app.database import SessionLocal
from datetime import datetime

def seed_tipo_inventario():
    db = SessionLocal()
    try:
        nombres = ["Compras", "Ventas"]
        for nombre in nombres:
            existe = db.query(TipoInventario).filter_by(nombre=nombre).first()
            if not existe:
                nuevo = TipoInventario(
                    nombre=nombre,
                    created_at=datetime.utcnow(),
                    updated_at=datetime.utcnow()
                )
                db.add(nuevo)
        db.commit()
    except Exception as e:
        db.rollback()
        print("Error al insertar tipo inventario:", e)
    finally:
        db.close()
