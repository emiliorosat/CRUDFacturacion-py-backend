from db import insertUpdate, select
from models import Articulo

def addItemInDb(item : Articulo):
    sql = 'INSERT INTO articulos (codigo, nombre, precio, cantidad) values(?,?,?,?)'
    query = insertUpdate( sql, (item.Codigo, item.Nombre, item.Precio, item.Cantidad) )
    if query:
        return {
            "status": True, "message": "Cliente creado correctamente"
        }
    else:
        return {
            "status": False, "message": "Error al crear nuevo cliente"
        }

def readItemsInDb():
    sql = 'SELECT * FROM articulos'
    query = select(sql)
    if query:
        toDics = []
        for i in query:
            toDics.append({"id": i[0], "codigo": i[1], "nombre": i[2], "precio": i[3], "cantidad": i[4]})
        return {
            "status": True, "data": toDics
        }
    else:
        return {
            "status": False, "message": "No existen articulos"
        }
    return