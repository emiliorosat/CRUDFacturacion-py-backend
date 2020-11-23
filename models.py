from pydantic import BaseModel 
from typing import List, Optional
from datetime import date

class Cliente(BaseModel):
    Id: int = None
    Nombre: str
    RNC: str

class Articulo(BaseModel):
    Id: int
    Codigo: str
    Nombre: str
    Precio: float
    Cantidad: int

class Detalle(BaseModel):
    ArticuloId: int
    FacturaId: int
    Cantidad: int
    Precio: float

class Factura(BaseModel):
    Id: int
    Fecha: date
    Codigo: Optional[str] = None
    Descripcion: str
    ClienteId: int
    Detalles: List[Detalle]

