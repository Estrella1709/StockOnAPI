from sqlalchemy.orm import Session
from models.models import Venta, VentaProducto, Producto
from schemas.venta_schema import VentaCreate
from datetime import datetime
from decimal import Decimal

def crear_venta(db: Session, venta_data: VentaCreate):
    total = Decimal("0.00")

    venta = Venta(
        id_empresa=venta_data.id_empresa,
        fecha=datetime.utcnow()
    )
    db.add(venta)
    db.flush()  

    for item in venta_data.productos:
        subtotal = Decimal(str(item.precio_unitario)) * item.cantidad
        total += subtotal

        detalle = VentaProducto(
            id_venta=venta.id,
            id_producto=item.id_producto,
            cantidad=item.cantidad,
            precio_unitario=item.precio_unitario
        )
        db.add(detalle)

        # Reducir inventario
        producto = db.query(Producto).filter(Producto.id == item.id_producto).first()
        if producto:
            producto.cantidad -= item.cantidad

    venta.precioTotal = total
    db.commit()
    db.refresh(venta)

    return venta
