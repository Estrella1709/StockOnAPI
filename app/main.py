from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware 

from app.seed_tipo_inventario import seed_tipo_inventario
from app.routes import empresa_routes
from app.routes import inventario_routes
from app.routes import producto_routes
from app.routes import venta_routes
from app.routes import puesto_routes
from app.routes import empleado_routes
from app.routes import proveedor_routes
from app.models import models
from app.database import engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="API Stock On",
    description="Stock On",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

seed_tipo_inventario()

app.include_router(empresa_routes.router, prefix="/empresa", tags=["Empresa"])
app.include_router(inventario_routes.router, prefix="/inventarios", tags=["Inventarios"])
app.include_router(producto_routes.router)
app.include_router(venta_routes.router)
app.include_router(puesto_routes.router)
app.include_router(empleado_routes.router)
app.include_router(proveedor_routes.router)
