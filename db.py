import sqlite3 as sqlite
from typing import Optional
import os

def conexion():
    return sqlite.connect("./data/DB1.db")

def aplicandoMigracion():
    schema = open("./data/migracion.sql", "r")
    cadena = schema.readlines()
    migration = "".join(cadena)
    schema.close()
    db = conexion()
    query = db.cursor()
    query.executescript(migration)
    db.close()

def insertUpdate(sql: str, data: [tuple, list] ):
    db = conexion()
    try:
        query = db.cursor()
        if(type(data) == tuple):
            query.execute(sql, data)
        elif(type(data) == list):
            query.executemany(sql, data)
        db.commit()
        db.close()
        return True
    except:
        return False

def select(sql: str):
    db = conexion()
    try: 
        query = db.cursor()
        data = query.execute(sql).fetchall()
        db.close()
        return data
    except:
        return False

def delete(sql: str):
    db = conexion()
    try: 
        query = db.cursor()
        query.execute(sql)
        db.commit()
        db.close()
        return True
    except:
        return False

aplicandoMigracion()

"""
class BaseDBModel(Model):
    class Meta:
        database = db

class Cliente(BaseDBModel):
    Id = AutoField(unique=True)
    Nombre = CharField()
    RNC = CharField(max_length=20)

class Articulo(BaseDBModel):
    Id = AutoField(unique=True)
    Codigo = CharField()
    Nombre = CharField()
    Precio = FloatField()
    Cantidad = IntegerField()

class Factura(BaseDBModel):
    Id = AutoField(unique=True)
    Fecha = DateField()
    Descripcion = TextField()
    ClienteId = ForeignKeyField(Cliente)

class Detalle(BaseDBModel):
    ArticuloId = ForeignKeyField(Articulo)
    FacturaId = ForeignKeyField(Factura)
    Cantidad = IntegerField()
    Precio = FloatField()

    class Meta:
        primary_key = CompositeKey('ArticuloId', 'FacturaId')

db.connect()
db.create_tables([Cliente, Articulo, Factura, Detalle])
"""