-- Ahora, analicemos la tabla Productos.

USE Aurelion;

-- Primero, veamos todas las columnas y filas de la tabla para saber qué podríamos analizar

SELECT * FROM Productos;

-- Primero, podríamos conocer la cantidad de productos totales por categoria, de mayor a menor cantidad

SELECT categoria, COUNT(*) AS Numero_de_productos 
FROM Productos
GROUP BY categoria
ORDER BY Numero_de_productos DESC;

/*
Podemos observar que la categoria alimentos tiene la mayor cantidad de productos, con un total de 84 Productos disponibles.
Mientras que la categoria Limpieza tienen 16 productos disponibles.
*/

-- Ahora, podemos conocer los 5 productos más caros y los 5 productos más baratos de todo el catalogo

SELECT nombre_producto, precio_unitario
FROM Productos
ORDER BY precio_unitario DESC
LIMIT 5;

SELECT nombre_producto, precio_unitario
FROM Productos
ORDER BY precio_unitario ASC
LIMIT 5;

/*
Los 5 productos más caros son: Miel Pura 250g, Pepsi 1.5L, Sprite1.5L, Suavitel 1L y Yerba Mate Intensa 1kg.
Los 5 productos más baratos son: Pan Lactal Integral, Helado Vainilla 1L, Turrón 50g, Vodka 700ml y Té Negro 20 saquitos.
*/

-- Podríamos conocer si existe una moda en el precio unitario

SELECT precio_unitario, COUNT(*) AS Frecuencia
FROM Productos
GROUP BY precio_unitario
ORDER BY Frecuencia DESC;

/*
EL resultado nos arrojo que el precio unitario de 2512.00 esta presente en dos productos diferentes,
mientras que todos los demás precios solo se encuentran una sola vez.
*/

-- Podemos conocer los 3 productos mas caros y baratos de cada categoria

SELECT categoria, nombre_producto, precio_unitario
FROM Productos
WHERE categoria = "Alimentos"
ORDER BY precio_unitario DESC
LIMIT 3;

SELECT categoria, nombre_producto, precio_unitario
FROM Productos
WHERE categoria = "Alimentos"
ORDER BY precio_unitario ASC
LIMIT 3;

SELECT categoria, nombre_producto, precio_unitario
FROM Productos
WHERE categoria = "Limpieza"
ORDER BY precio_unitario ASC
LIMIT 3;

SELECT categoria, nombre_producto, precio_unitario
FROM Productos
WHERE categoria = "Limpieza"
ORDER BY precio_unitario DESC
LIMIT 3;

-- Tambien podemos buscar productos por medio de una palabra clave en su nombre, ejemplo, leche

SELECT nombre_producto, precio_unitario
FROM Productos
WHERE nombre_producto LIKE '%Leche%';


-- Podemos conocer los productos y su categoria filtrando mediante un rango en precio unitario y la categoria
SELECT nombre_producto, categoria, precio_unitario
FROM Productos
WHERE precio_unitario BETWEEN 1000 AND 2000
    AND categoria = 'Limpieza'
ORDER BY precio_unitario DESC;


-- Podemos hacer algo parecido a la consulta anterior pero solo para los productos que tengan un precio unitario igual o mayor a la cantidad requerida
SELECT nombre_producto, categoria, precio_unitario
FROM Productos
WHERE precio_unitario >= 4000
    AND categoria = 'Alimentos'
ORDER BY precio_unitario DESC;