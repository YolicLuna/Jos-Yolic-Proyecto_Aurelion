USE Aurelion;

-- Comenzamos con la tabla Clientes
-- Primero, vamos a ver todas las columnas y filas de la tabla para saber que podríamos analizar

SELECT * FROM Clientes;

-- En este caso, sabemos que la tabla contiene 100 filas, o sea, 100 clientes diferentes
-- Pero en caso de tener una tabla mucho más grande, podríamos conocer el número de filas con la siguiente consultas

SELECT COUNT(*) AS Numero_de_clientes 
FROM Clientes;

-- Ahora, lo que podemos analizar es la distribución de clientes por ciudad, de mayor a menor cantidad de clientes

SELECT ciudad, COUNT(*) AS Numero_de_clientes 
FROM Clientes 
GROUP BY ciudad 
ORDER BY Numero_de_clientes DESC;

/*
El resultado de la consulta anterior nos muestra que la ciudad con más clientes es Rio Cuarto con 23 clientes,
seguida por Alta Gracia con 21 clientes. Estas serian las dos ciudades con mayor concentración de clientes.
Las demás ciudades, Carlos paz y Villa Maria con 15 clientes cada una, y finalmente Cordoba y Mendiolaza con 13 clientes cada una.
 */

-- Podemos conocer la cantidad de clientes registrados cada mes

SELECT Mes, ciudad COUNT(*) AS Clientes_por_mes
FROM Clientes
GROUP BY Mes
ORDER BY Clientes_por_mes DESC;

/*
La consulta nos muestra que los meses con mayor cantidad de clientes registrados son Junary (Enero) y March (Marzo) con 31 clientes cada uno.
Segudos de February (Febrero) con 28 clientes y April (Abril) con 10 clientes.
*/

-- Podemos conocer la cantidad de clientes registrados cada mes y el nombre de la ciudad a la que pertenecen esos clientes
SELECT Mes, ciudad, COUNT(*) AS total_clientes
FROM Clientes
GROUP BY Mes, ciudad
ORDER BY mes, ciudad;

SELECT Mes, ciudad, COUNT(*) AS total_clientes
FROM Clientes
WHERE Mes = 'April'
GROUP BY Mes, ciudad
ORDER BY mes, ciudad;

SELECT Mes, ciudad, COUNT(*) AS total_clientes
FROM Clientes
WHERE ciudad = 'Cordoba'
GROUP BY Mes, ciudad
ORDER BY mes, ciudad;

/*
La primer consulta nos muestra la cantidad de clientes registrados cada mes y la ciudad a la que pertenecen.
La segunda consulta nos muestra solo la cantidad de clientes registrados el mes 'April' y la ciudad a la que pertenecen.
Y la tercer consulta nos muestra la cantidad de clientes registrados cada mes pero solo de la ciudad de cordoba.
La ultimas dos consultas pueden cambiar para mostrar el mes o la ciudad requeridos.
*/

-- Podemos conocer toda la información de los clientes por rango de fechas
SELECT *
FROM Clientes
WHERE fecha_alta BETWEEN '2023-01-01' AND '2023-01-31';
