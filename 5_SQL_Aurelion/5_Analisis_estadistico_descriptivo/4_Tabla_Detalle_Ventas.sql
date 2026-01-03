-- Ahora, analizaremos la tabla Detalle_Ventas.

USE Aurelion;

-- Primero, veamos todas las columnas y filas de la tabla para saber qué podríamos analizar

SELECT * FROM Detalle_Ventas;

-- Lo primero que podemos hacer es sumar el total de ventas general por cantidad (pz) y por importe

SELECT SUM(cantidad) AS Cantidad_total_productos
FROM Detalle_Ventas;

SELECT SUM(importe) AS Cantidad_total_importe
FROM Detalle_Ventas;

/*
Con la primer consulta obtenemos que la cantidad (pz) general de productos vendidos es de 1016.00.
Con la segunda consulta obtenemos que el importe general de ventas es de 2,651,417.00
*/


-- Ahora, podemos obtener los tres productos con la mayor cantidad (pz) vendidas
SELECT id_producto, SUM(cantidad) AS cantidad_total_por_producto
FROM Detalle_Ventas
GROUP BY id_producto
ORDER BY cantidad_total_por_producto DESC
LIMIT 3;

-- Tambien, podemos obtener los tres productos con la menos cantidad (pz) vendidad
SELECT id_producto, SUM(cantidad) AS cantidad_total_por_producto
FROM Detalle_Ventas
GROUP BY id_producto
ORDER BY cantidad_total_por_producto ASC
LIMIT 3;

/*
Con la primer consulta obtenemos que el id_producto (producto) con mayor cantidad (pz) vendidad es el id 43, con 27 piezas,
seguido del id 18 con 26 piezas y el id 79 con 24 piezas.

En la segunda consulta obtenemos que los id's con menor cantidad (pz) vendidad son:
25, 33, y 26, cada uno con 2 piezas vendidas.
*/


-- Podemos obtener la suma de los importes por id_producto (producto). Podemos limitar la cantidad de resultados añadiendo al final "LIMIT 3", por ejemplo.
SELECT id_producto, SUM(importe) AS importe_total
FROM Detalle_Ventas
GROUP BY id_producto;


-- Tambien podemos obtener los 3 id_producto (producto) con el mayor importe de ventas totales
SELECT id_producto, SUM(importe) AS importe_total
FROM Detalle_Ventas
GROUP BY id_producto
ORDER BY importe_total DESC
LIMIT 3;

/*
La consulta anterior nos muestra que el id_producto con el mayor importe de ventas total es el id 91, con 93,800.00,
seguido del id 18 con 89,544.00 y del id 76 con 85,720.00.
*/

-- Tambien podemos obtener los 3 id_productos (producto) con el menor importe de ventas totales
SELECT id_producto, SUM(importe) AS importe_total
FROM Detalle_Ventas
GROUP BY id_producto
ORDER BY importe_total ASC
LIMIT 3;

/*
La consulta anterior nos muestra que los id_producto con menores importes de ventas totales son:
id 26 con 2,002.00, id 71 con 2,032.00 y id 33 con 2,510.00.
*/


-- Podemos conocer el importe total por cada id_venta
SELECT id_venta, SUM(importe) AS importe_total
FROM Detalle_Ventas
GROUP BY id_venta;


-- Podemos conocer los 3 id_venta con el mayor importe de ventas totales
SELECT id_venta, SUM(importe) AS importe_total
FROM Detalle_Ventas
GROUP BY id_venta
ORDER BY importe_total DESC
LIMIT 3;

/*
La consulta anteriror nos muestra que los id_venta con la el mayor importe de ventas todales son:
id 50 con 61,503.00, id 57 con 57,287.00 y id 32 con 53,828.00.
*/

-- Podemos conocer los 3 id_venta con el menor importe de ventas totales
SELECT id_venta, SUM(importe) AS importe_total
FROM Detalle_Ventas
GROUP BY id_venta
ORDER BY importe_total ASC
LIMIT 3;

/*
La consulta anterior nos muestra que los id_venta con el menor importe de ventas totales son:
id 46 con 272.00, id 53 con 936.00 y id 55 con 1,876.00.
*/


-- POdemos conocer el importe maximo y el importe minimo de una venta, así como el importe promedio
SELECT MAX(importe) AS Importe_maximo
FROM Detalle_Ventas;

SELECT MIN(importe) AS Importe_minimo
FROM Detalle_Ventas;

SELECT AVG(importe) AS Importe_promedio
FROM Detalle_Ventas;

/*
Los resultados que nos muestran las consultas son:
Importe mayor 24,865.00, importe minimo 272.00, importe promedio 7,730.078717
*/
