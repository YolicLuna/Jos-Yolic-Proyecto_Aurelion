USE Aurelion;

-- JOIN 1: VENTAS CON CLIENTES
/*
DESCRIPCIÓN: Obtiene información completa de todas las ventas incluyendo los datos del cliente que realizó la compra.
RESULTADO: Muestra ID venta, fecha de venta, nombre del cliente, ciudad del cliente y medio de pago utilizado.
*/

SELECT v.id_venta,
       v.fecha,
       c.nombre_cliente,
       c.ciudad,
       v.medio_pago
FROM Ventas v
INNER JOIN Clientes c ON v.id_cliente = c.id_cliente;


-- JOIN 2: DETALLE DE VENTAS CON PRODUCTOS
/*
DESCRIPCIÓN: Vincula cada línea de detalle de venta con la información completa del producto que fue vendido.
RESULTADO: Muestra ID de venta, nombre del producto, categoría, cantidad vendida e importe total de cada línea de venta.
*/

SELECT dv.id_venta,
       p.nombre_producto,
       p.categoria,
       dv.cantidad,
       dv.importe
FROM Detalle_Ventas dv
INNER JOIN Productos p ON dv.id_producto = p.id_producto
ORDER BY id_venta ASC; 


-- JOIN 3: VENTAS CON DETALLE DE VENTAS
/*
DESCRIPCIÓN: Relaciona cada venta con sus detalles específicos (productos comprados en esa venta).
RESULTADO: Muestra el ID y fecha de venta, cliente que compró,
productos comprados, cantidad e importe por producto.
*/

SELECT v.id_venta,
       v.fecha,
       v.id_cliente, 
       dv.id_producto,
       dv.cantidad,
       dv.importe
FROM Ventas v
INNER JOIN Detalle_Ventas dv ON v.id_venta = dv.id_venta;


-- JOIN 4: TRIPLE JOIN - CLIENTES + VENTAS + DETALLE + PRODUCTOS
/*
DESCRIPCIÓN: Vincula todas las tablas para obtener un registro completo: cliente, venta realizada y detalles de productos comprados.
RESULTADO: Muestra nombre del cliente, fecha de compra, productos comprados, cantidad e importe de cada producto en cada venta.
*/

SELECT c.nombre_cliente,
       v.id_venta,
       v.fecha,
       p.nombre_producto,
       dv.cantidad,
       dv.importe
FROM Clientes c
INNER JOIN Ventas v ON c.id_cliente = v.id_cliente
INNER JOIN Detalle_Ventas dv ON v.id_venta = dv.id_venta
INNER JOIN Productos p ON dv.id_producto = p.id_producto;


-- JOIN 5: CUÁDRUPLE JOIN - TODAS LAS TABLAS
/*
DESCRIPCIÓN: Combina las 4 tablas principales para obtener un reporte completo y detallado de todas las transacciones.
RESULTADO: Muestra cliente, fecha de venta, producto, categoría, cantidad, precio unitario e importe total de cada línea de venta.
ORDENADO: Por fecha de venta (ascendente).
*/

SELECT c.nombre_cliente,
       v.fecha,
       p.nombre_producto,
       p.categoria,
       dv.cantidad,
       p.precio_unitario,
       dv.importe
FROM Clientes c
INNER JOIN Ventas v ON c.id_cliente = v.id_cliente
INNER JOIN Detalle_Ventas dv ON v.id_venta = dv.id_venta
INNER JOIN Productos p ON dv.id_producto = p.id_producto
ORDER BY fecha ASC;


-- JOIN 6: LEFT JOIN - CLIENTES CON SUS VENTAS
/*
DESCRIPCIÓN: Obtiene todos los clientes y cuenta cuántas ventas ha realizado cada uno. Incluye clientes sin ventas (resultado 0).
RESULTADO: Muestra nombre del cliente y total de ventas realizadas por cada cliente. Clientes sin ventas aparecen con total_ventas = 0.
AGRUPADO: Por cliente.
*/

SELECT c.nombre_cliente,
       COUNT(v.id_venta) as total_ventas
FROM Clientes c
LEFT JOIN Ventas v ON c.id_cliente = v.id_cliente 
GROUP BY c.id_cliente, c.nombre_cliente;


-- JOIN 7: LEFT JOIN - PRODUCTOS VENDIDOS Y NO VENDIDOS
/*
DESCRIPCIÓN: Obtiene todos los productos y cuenta cuántas veces ha sido vendido cada uno. Identifica productos nunca vendidos.
RESULTADO: Muestra nombre del producto y cantidad de veces que ha sido vendido. Los productos no vendidos aparecen con veces_vendido = 0.
AGRUPADO: Por producto.
*/

SELECT p.nombre_producto, 
       COUNT(dv.id_venta) as veces_vendido  
FROM Productos p
LEFT JOIN Detalle_Ventas dv ON p.id_producto = dv.id_producto  
GROUP BY p.id_producto, p.nombre_producto;  


-- JOIN 8: VENTAS POR CLIENTE, CIUDAD Y MEDIO DE PAGO
/*
DESCRIPCIÓN: Analiza las ventas agrupadas por cliente, ciudad y medio de pago, mostrando cantidad de transacciones y gasto total.
RESULTADO: Muestra nombre del cliente, ciudad, medio de pago utilizado, cantidad de ventas realizadas y monto total gastado.
AGRUPADO: Por cliente, ciudad y medio de pago.
*/

SELECT c.nombre_cliente,           
       c.ciudad,                   
       v.medio_pago,               
       COUNT(v.id_venta) as cantidad_ventas,  
       SUM(dv.importe) as total_gastado       
FROM Clientes c
INNER JOIN Ventas v ON c.id_cliente = v.id_cliente
INNER JOIN Detalle_Ventas dv ON v.id_venta = dv.id_venta
GROUP BY c.id_cliente, c.nombre_cliente, c.ciudad, v.medio_pago;


-- JOIN 9: PRODUCTOS MÁS VENDIDOS POR CATEGORÍA
/*
DESCRIPCIÓN: Análisis de ventas por producto y categoría, mostrando la cantidad total vendida de cada producto y sus ingresos generados.
RESULTADO: Muestra categoría del producto, nombre del producto, cantidad total vendida e ingresos totales generados.
AGRUPADO: Por categoría y producto.
ORDENADO: Primero por categoría, luego por ingresos (mayor a menor).
*/

SELECT p.categoria,                
       p.nombre_producto,         
       SUM(dv.cantidad) as cantidad_total,  
       SUM(dv.importe) as ingresos         
FROM Productos p
INNER JOIN Detalle_Ventas dv ON p.id_producto = dv.id_producto
GROUP BY p.categoria, p.id_producto, p.nombre_producto
ORDER BY p.categoria, ingresos DESC;  


-- JOIN 10: CLIENTES POR CIUDAD CON GASTO TOTAL
/*
DESCRIPCIÓN: Obtiene un resumen de clientes agrupados por ciudad, mostrando cuántas compras ha hecho cada cliente y cuánto ha gastado.
RESULTADO: Muestra ciudad, nombre del cliente, número de compras realizadas y gasto total de cada cliente.
AGRUPADO: Por ciudad y cliente.
ORDENADO: Primero por ciudad, luego por gasto total (mayor a menor).
NOTA: LEFT JOINs incluyen clientes sin ventas (con NULL en las agregaciones).
*/

SELECT c.ciudad,                   
       c.nombre_cliente,          
       COUNT(v.id_venta) as num_compras,   
       SUM(dv.importe) as gasto_total      
FROM Clientes c
LEFT JOIN Ventas v ON c.id_cliente = v.id_cliente
LEFT JOIN Detalle_Ventas dv ON v.id_venta = dv.id_venta
GROUP BY c.ciudad, c.id_cliente, c.nombre_cliente
ORDER BY c.ciudad, gasto_total DESC;
