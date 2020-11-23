
CREATE TABLE IF NOT EXISTS articulos(
    id INTEGER NOT NULL  PRIMARY KEY AUTOINCREMENT,
    codigo VARCHAR(20) NOT NULL,
    nombre VARCHAR(200) NOT NULL,
    precio FLOAT DEFAULT 0.0,
    cantidad INTEGER DEFAULT 0
);

CREATE TABLE IF NOT EXISTS clientes(
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    nombre VARCHAR(200) NOT NULL,
    rnc VARCHAR(30)
);

CREATE TABLE IF NOT EXISTS facturas(
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    codigo VARCHAR(20),
    fecha DATE,
    descripcion TEXT,
    cliente_id INTEGER,
    CONSTRAINT fk_clientes FOREIGN KEY (cliente_id) REFERENCES clientes (id)
);

CREATE TABLE IF NOT EXISTS detalles(
    articulo_id INTEGER NOT NULL,
    factura_id INTEGER NOT NULL,
    cantidad INT DEFAULT 0,
    precio FLOAT DEFAULT 0,
    CONSTRAINT fk_articulos FOREIGN KEY (articulo_id) REFERENCES articulos (id),
    CONSTRAINT fk_facturas FOREIGN KEY (factura_id) REFERENCES facturas (id)
);