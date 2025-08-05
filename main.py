from fastapi import FastAPI
from seed_tipo_inventario import seed_tipo_inventario
from routes import empresa_routes
from routes import inventario_routes
from routes import producto_routes
from routes import venta_routes
from routes import puesto_routes
from routes import empleado_routes
from routes import proveedor_routes
from models import models
from database import engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="API Stock On",
    description="Stock On",
    version="1.0.0"
)
seed_tipo_inventario()
app.include_router(empresa_routes.router, prefix="/empresa", tags=["Empresa"])
app.include_router(inventario_routes.router, prefix="/inventarios", tags=["Inventarios"])
app.include_router(producto_routes.router)
app.include_router(venta_routes.router)
app.include_router(puesto_routes.router)
app.include_router(empleado_routes.router)
app.include_router(proveedor_routes.router)
