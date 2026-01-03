-- Ahora, analizaremos la tabla Ventas.

USE Aurelion;

-- Primero, veamos todas las columnas y filas de la tabla para saber qué podríamos analizar

SELECT * FROM Ventas;
 
-- Podemos conocer la cantidad de ventas que se realizaron con cada medio de pago
SELECT medio_pago, COUNT(*) AS cantidad_ventas
FROM Ventas
GROUP BY medio_pago
ORDER BY cantidad_ventas DESC
LIMIT 5;

/*
El resultado nos muestra que el medio de pago, efectivo, tiene la mayor cantidad de ventas, con 37 ventas totales,
seguido de qr con 30, transferencia con 27 y tarjeta con 26.
*/


-- Podemos conocer la cantidad de ventas que se realizaron con cada mes
SELECT Mes, COUNT(*) AS cantidad_ventas
FROM Ventas
GROUP BY Mes
ORDER BY cantidad_ventas DESC;

/*
El resultsdo nos muestra que el mes con mayor cantidad de ventas en el mes de January (Enero) con 24,
seguido de May (Mayo) con 22, June (Junio) con 21, March (Marzo) con 21, February (Febrero) 20 y April (Abril) con 12.
*/


-- Podemos conocer los 5 id_clientes (clientes) con mas cantidad de compras realizadas, listando de mayor a menor
SELECT id_cliente, COUNT(*) AS cantidad_de_compras
FROM Ventas
GROUP BY id_cliente
ORDER BY cantidad_de_compras DESC
LIMIT 5;

/*
El resultado nos muestra que el id_cliente (cliente) con la mayor cantidad de compras realizadas es el id 56, con 5 compras.
Seguido de los id_clientes 42, 49, 5, 39, con 4 ventas cada uno.
*/


-- Podemos conocer los 5 id_clientes (clientes) con menor cantidad de compras realizadas, listando de mayor a menor
SELECT id_cliente, COUNT(*) AS cantidad_de_compras
FROM Ventas
GROUP BY id_cliente
ORDER BY cantidad_de_compras ASC
LIMIT 5;

/*
El resultado nos muestra que los 5 id_cliente (clientes) con menos compras, una por cada id_cliente,
son: 2, 3, 10, 13, 8. 
*/


-- Podemos conocer la cantidad de transacciones que se realizaron con cada metodo de pago en cada mes.
SELECT Mes, medio_pago, COUNT(medio_pago) AS cantidad_transacciones
FROM Ventas
GROUP BY Mes, medio_pago
ORDER BY cantidad_transacciones DESC;


-- Tambien podemos elegir el medio de pago para conocer el total de las transacciones del medio de pago en cada mes, añadiendo WHERE
SELECT Mes, medio_pago, COUNT(medio_pago) AS cantidad_transacciones
FROM Ventas
WHERE medio_pago = "efectivo"
GROUP BY Mes, medio_pago
ORDER BY cantidad_transacciones DESC;


-- Podemos conocer la preferencia de medio de pago de cada cliente
SELECT Mes, medio_pago, COUNT(medio_pago) AS cantidad_transacciones
FROM Ventas
GROUP BY Mes, medio_pago
ORDER BY cantidad_transacciones DESC;

-- Podemos elegir el medio de pago para saber que clientes lo prefieren mas
SELECT id_cliente, medio_pago, COUNT(medio_pago) AS cantidad_transacciones
FROM Ventas
WHERE medio_pago = "efectivo"
GROUP BY id_cliente, medio_pago
ORDER BY cantidad_transacciones DESC;

-- Tambien podemos elegir el id_cliente (cliente) para conocer los medios de pago que suele usar y la cantidad de transacciones que a realizado con cada uno
SELECT id_cliente, medio_pago, COUNT(medio_pago) AS cantidad_transacciones
FROM Ventas
WHERE id_cliente = 1
GROUP BY id_cliente, medio_pago
ORDER BY cantidad_transacciones DESC;

