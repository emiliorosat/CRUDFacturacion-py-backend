-- SQLite
/*
INSERT INTO facturas 
(fecha, descripcion, cliente_id, codigo) 
VALUES ('19-11-2020', 'una descripcion larga', 1, '131e50c0');
*/
/*
INSERT INTO detalles (articulo_id, factura_id, cantidad, precio)
VALUES
(1,1,2, 9),
(2,1,2, 9);
*/
/*
SELECT f.id, a.id, a.nombre, a.codigo, d.cantidad, d.precio 
FROM facturas f 
INNER JOIN detalles d ON f.id = d.factura_id 
INNER JOIN articulos a ON d.articulo_id = a.id;
*/
/*
SELECT a.id, a.codigo, a.nombre, d.cantidad, d.precio
FROM detalles d INNER JOIN articulos a ON a.id = d.articulo_id
WHERE d.factura_id = 1;
*/
--UPDATE articulos SET cantidad = cantidad - 1 WHERE id = 1

-- SELECT id, codigo, fecha, descripcion, cliente_id FROM facturas WHERE id = 1
/*
SELECT a.id, a.codigo, a.nombre, d.precio, d.cantidad FROM detalles d 
INNER JOIN articulos a ON d.articulo_id = a.id WHERE d.factura_id = 1
*/

--DELETE FROM facturas WHERE id = 2

-- DELETE FROM detalles WHERE factura_id = 
