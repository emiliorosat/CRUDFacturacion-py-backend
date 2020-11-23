from db import select, insertUpdate, delete
from models import Factura, Detalle
from uuid import uuid4
from random import sample

def addInvoceInDb(invoce: Factura):
    code = "".join(sample(format(id(uuid4()), "x"), 8))
    sql = "INSERT INTO facturas (fecha, descripcion, cliente_id, codigo) VALUES (?,?,?,?)"
    queryF = insertUpdate(sql, (invoce.Fecha, invoce.Descripcion, invoce.ClienteId, code) )
    if queryF:
        sql = "SELECT id FROM facturas WHERE codigo = '" + code +"';" 
        fid = select(sql)
        nT = buildTupleDetails(invoce.Detalles, fid[0][0])
        sql = "INSERT INTO detalles (articulo_id, factura_id, cantidad, precio) VALUES (?,?,?,?)"
        queryD = insertUpdate(sql, nT)
        if queryD:
            return {
                "status": True, "message": "Factura creada correctamente", "data": fid[0][0]
            }
    return {
                "status": False, "message": "Error al crear factura"
            }

def buildTupleDetails(arr: list, fid: int):
    data = []
    for d in range( len( arr ) ):
        data.append((arr[d].ArticuloId, fid, arr[d].Cantidad, arr[d].Precio))
    return data

def updateInvoceInDb(invoce: Factura):
    sql = "UPDATE facturas SET descripcion = ? WHERE id = ?"
    query = insertUpdate(sql, (invoce.Descripcion, invoce.Id))
    if query:
        sql = "DELETE FROM detalles WHERE factura_id = "+ str(invoce.Id) + ";"
        query = delete(sql)
        if query:
            nT = buildTupleDetails(invoce.Detalles, invoce.Id)
            sql = "INSERT INTO detalles (articulo_id, factura_id, cantidad, precio) VALUES (?,?,?,?)"
            query = insertUpdate(sql, nT)
            if query:
                return {
                "status": True, "message": "Factura actualizada correctamente"
            }
    return {
                "status": False, "message": "Error al actualizar factura"
            }

def readInvocesInDB():
    sql = "SELECT f.id, f.codigo, f.fecha, f.descripcion, c.nombre FROM facturas f INNER JOIN clientes c on f.cliente_id = c.id"
    query = select(sql)
    sql = "SELECT f.id, a.id, a.nombre, a.codigo, d.cantidad, d.precio FROM facturas f INNER JOIN detalles d ON f.id = d.factura_id INNER JOIN articulos a ON d.articulo_id = a.id;"
    queryE = select(sql)
    obj = []
    for i in query:
        art = []
        for a in queryE:
            if a[0] == i[0]:
                art.append({
                    "id": a[1], "nombre": a[2], "codigo": a[3], "cantidad": a[4], "precio": a[5]
                }) 
        obj.append({
            "id":i[0], "codigo":i[1], "fecha":i[2], "descripcion":i[3], "cliente": i[4], "articulos": art 
        })
    return {
        "status": True, "data": obj
    }

def readInvoceDetailsInDB():
    return
    
def findByIdInvoceInDb(id: int):
    sql = "SELECT f.id, f.codigo, f.fecha, f.descripcion, c.nombre, c.rnc FROM facturas f INNER JOIN clientes c ON f.cliente_id = c.id WHERE f.id = " + str(id) + ";"
    query = select(sql)
    if query:
        sql = "SELECT a.id, a.codigo, a.nombre, d.precio, d.cantidad FROM detalles d INNER JOIN articulos a ON d.articulo_id = a.id WHERE d.factura_id = " + str(id) + ";"
        queryD = select(sql)
        art = []
        if queryD:
            for i in queryD:
                art.append({"id":i[0], "codigo":i[1], "nombre":i[2], "precio":i[3], "cantidad":i[4]})
        return {
            "status": True, "data": {
                "id": query[0][0], "codigo": query[0][1], "fecha": query[0][2], "descripcion": query[0][3], "cliente":query[0][4], "RNC":query[0][5], "articulos": art
            }
        }
    else:
        return {
            "status": False, "message": "Factura no encontrada"
        }

def deleteInvoceInDb(id: int):
    sql = "DELETE FROM facturas WHERE id = "+ str(id) + ";"
    print(sql)
    query = delete(sql)
    if query:
        sql = "DELETE FROM detalles WHERE factura_id = "+ str(id) + ";"
        query = delete(sql)
        if query:
            return {
                "status": True, "message": "Factura borrada correctamente"
            }
        else:
            return {
                "status": False, "message": "Error al borrar Detalles"
            }
    else:
        return {
                "status": False, "message": "Error al borrar Factura"
            }

