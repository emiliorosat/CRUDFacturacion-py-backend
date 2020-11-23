from db import insertUpdate, select
from models import Cliente


def addClientInDb(client: Cliente):
    sql = 'INSERT INTO clientes (nombre, rnc) values(?,?)'
    data = (client.Nombre, client.RNC)
    query = insertUpdate(sql, data )
    if query:
        return {
            "status": True, "message": "Cliente creado correctamente"
        }
    else:
        return {
            "status": False, "message": "Error al crear nuevo cliente"
        }

def readClientsInDb():
    sql = "SELECT * FROM clientes"
    query = select(sql)
    if query:
        toDics = []
        for i in query:
            toDics.append({"id": i[0], "nombre": i[1], "RNC": i[2]})
        return {
            "status": True, "data": toDics
        }
    else:
        return {
            "status": False, "message": "No existen clientes"
        }



