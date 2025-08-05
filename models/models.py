from sqlalchemy import Column, String, Integer, BigInteger, DECIMAL, ForeignKey, DateTime, Text, Boolean
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
from sqlalchemy import Integer

Base = declarative_base()

class Empresa(Base):
    __tablename__ = 'empresa'
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    numeroRegistro = Column(String(14))
    nombre = Column(String(255))
    tipo = Column(String(255))
    correo = Column(String(255))
    contrasena = Column(String(255))
    numTelefono = Column(String(20))
    pais = Column(String(50))
    region = Column(String(50))
    direccion = Column(String(300))
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

class Producto(Base):
    __tablename__ = 'productos'
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100))
    precioUnitario = Column(DECIMAL(10, 2))
    dimensiones = Column(Text)
    peso = Column(DECIMAL(10, 2))
    precauciones = Column(Text)
    cantidad = Column(Integer)
    caracteristicas = Column(Text)
    codigoBarras = Column(String(200))
    material = Column(Text)
    id_inventario = Column(BigInteger, ForeignKey('inventarios.id'))
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

class Inventario(Base):
    __tablename__ = 'inventarios'
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    nombre = Column(String(255))
    id_empresa = Column(BigInteger, ForeignKey('empresa.id'))
    id_tipoInventario = Column(BigInteger, ForeignKey('tipo_inventarios.id'))
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

class TipoInventario(Base):
    __tablename__ = "tipo_inventarios"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    nombre = Column(String(255), unique=True, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow)

class Carrito(Base):
    __tablename__ = 'carritos'
    id = Column(Integer, primary_key=True, autoincrement=True)
    producto_id = Column(BigInteger, ForeignKey('productos.id'))
    cantidad = Column(Integer)
    precio = Column(DECIMAL(10,2))
    precioTotal = Column(DECIMAL(10,2))
    fecha = Column(DateTime)
    id_empresa = Column(BigInteger, ForeignKey('empresa.id'))
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

class Venta(Base):
    __tablename__ = 'ventas'
    id = Column(Integer, primary_key=True, autoincrement=True)
    producto_id = Column(BigInteger, ForeignKey('productos.id'))
    cantidad = Column(Integer)
    precio = Column(DECIMAL(10, 2))
    precioTotal = Column(DECIMAL(10, 2))
    fecha = Column(DateTime)
    id_empresa = Column(BigInteger, ForeignKey('empresa.id'))
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

class VentaProducto(Base):
    __tablename__ = 'venta_productos'
    id = Column(Integer, primary_key=True, autoincrement=True)
    id_venta = Column(BigInteger, ForeignKey('ventas.id'))
    id_producto = Column(BigInteger, ForeignKey('productos.id'))
    cantidad = Column(Integer)
    precio_unitario = Column(DECIMAL(10, 2))
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

class Empleado(Base):
    __tablename__ = 'empleados'
    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(100))
    apellido = Column(String(100))
    correo = Column(String(125))
    telefono = Column(String(20))
    horario = Column(String(150))
    genero = Column(String(100))
    area = Column(String(150))
    salario = Column(DECIMAL(12, 2))
    contrasena = Column(String(200))
    id_empresa = Column(BigInteger, ForeignKey('empresa.id'))
    id_puesto = Column(BigInteger, ForeignKey('puestos.id'))
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

class Puesto(Base):
    __tablename__ = 'puestos'
    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(50))
    id_empresa = Column(BigInteger, ForeignKey('empresa.id'))
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

class Usuario(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    email = Column(String(255))
    email_verified_at = Column(DateTime)
    password = Column(String(255))
    remember_token = Column(String(100))
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

class Admin(Base):
    __tablename__ = 'admins'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255))
    email = Column(String(255))
    email_verified_at = Column(DateTime)
    password = Column(String(255))
    role = Column(Integer)
    remember_token = Column(String(100))
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

class Proveedor(Base):
    __tablename__ = 'proveedores'
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100), nullable=False)
    correo = Column(String(100), nullable=False)
    numTelefono = Column(String(20))
    tiposProducto = Column(String(255))
    condicionesPago = Column(String(255))
    frecuenciaSuministro = Column(String(255))
    horarioAtencion = Column(String(255))
    pais = Column(String(100))
    ciudad = Column(String(100))
    id_empresa = Column(BigInteger, ForeignKey('empresa.id'))
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

class Request(Base):
    __tablename__ = 'request'
    id = Column(Integer, primary_key=True, autoincrement=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    id_empresa = Column(BigInteger, ForeignKey('empresa.id'))
    pregunta = Column(Text)
    fecha = Column(DateTime)
    status = Column(Boolean)

class Answer(Base):
    __tablename__ = 'answer'
    id = Column(Integer, primary_key=True, autoincrement=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    id_pregunta = Column(BigInteger, ForeignKey('request.id'))
    respuesta = Column(Text)
    fecha = Column(DateTime)
