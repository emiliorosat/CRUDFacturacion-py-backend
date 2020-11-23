from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from clienteController import addClientInDb, readClientsInDb
from articuloController import addItemInDb, readItemsInDb
from facturaController import addInvoceInDb, findByIdInvoceInDb, readInvocesInDB, updateInvoceInDb, deleteInvoceInDb
from models import Cliente, Articulo, Factura


app = FastAPI(
    docs_url="/",
    redoc_url=None,
    title="CRUD Facturacion",
    description="Aplicacion Backend + Frontend para Facturar Articulos"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE", "PATCH"],
    allow_headers=["*"],
)

@app.post("/api/clients", tags=["Cliente"])
def createClient(client : Cliente):
    return addClientInDb(client)
    
@app.get("/api/clients", tags=["Cliente"])
def getClients():
    return readClientsInDb()

@app.post("/api/items", tags=["Articulo"])
def createItem(item: Articulo):
    return addItemInDb(item)

@app.get("/api/items", tags=["Articulo"])
def getItems():
    return readItemsInDb()

@app.get("/api/invoces", tags=["Factura"])
def getInvoces():
    return readInvocesInDB()

@app.post("/api/invoces", tags=["Factura"])
def createInvoce(invoce: Factura):
    return addInvoceInDb(invoce)

@app.patch("/api/invoces", tags=["Factura"])
def updateInvoce(invoce: Factura ):
    return updateInvoceInDb(invoce)

@app.get("/api/invoces/{id}", tags=["Factura"])
def getInvoceById(id: int):
    return findByIdInvoceInDb(id)

@app.delete("/api/invoces/{id}", tags=["Factura"])
def deleteInvoce(id: int):
    return deleteInvoceInDb(id)

