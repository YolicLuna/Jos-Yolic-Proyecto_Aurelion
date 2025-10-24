
# 1 Tema, problema y solución

## Documentación del Análisis de Ventas y Clientes

Este es un proyecto creado para practicar el análisis, visualización y modelado de datos utilizando python y bibliotecas como pandas, matplotlib, numpy, etc. Vamos a simular la gestion de una tienda realizando un proyecto basandonos en datos generados con fines educativos.

## Descripción del problema a resolver o analizar

Realizar un análisis de las ventas por producto para determinar:
- Qué productos son los menos vendidos.
- Cuáles generan menos ganancias.
- Medir el tiempo que tardan en venderse.
- Decidir si darles más publicidad o retirarlos del catálogo.

De igual forma, se podría analizar a los clientes para identificar:
- Quiénes compran más.
- Si existen clientes inactivos.
- Estrategias para aumentar la frecuencia de compra y recuperar clientes inactivos.

# 2 Origen de los datos

Los datos que usaremos para el análisis provienen de una base de datos de ventas y clientes de una tienda. La base de datos está conformada por 4 archivos CSV, cada archivo contiene una de las tablas que se describen más adelante.

# 3 Descripción de la estructura, tipos de datos y escala de la base de datos

### Tabla: Ventas

| Campo           | Tipo   | Escala    |
|-----------------|--------|-----------|
| id_venta        | int    | Ordinal   |
| fecha           | date   | Intervalo |
| id_cliente      | int    | Ordinal   |
| nombre_cliente  | string | Nominal   |
| email           | string | Nominal   |
| medio_pago      | string | Nominal   |

**Descripción de los campos:**

- `id_venta`: Identificador único de la venta.
- `fecha`: Fecha en que se realizó la venta.
- `id_cliente`: Identificador del cliente.
- `nombre_cliente`: Nombre del cliente.
- `email`: Correo electrónico del cliente.
- `medio_pago`: Medio de pago utilizado.

### Tabla: Productos

| Campo           | Tipo   | Escala  |
|-----------------|--------|---------|
| id_producto     | int    | Ordinal |
| nombre_producto | string | Nominal |
| categoria       | string | Nominal |
| precio_unitario | int    | Razón   |

**Descripción de los campos:**

- `id_producto`: Identificador único del producto.
- `nombre_producto`: Nombre del producto.
- `categoria`: Categoría del producto.
- `precio_unitario`: Precio por unidad.

### Tabla: Detalle_ventas

| Campo           | Tipo   | Escala  |
|-----------------|--------|---------|
| id_venta        | int    | Ordinal |
| id_producto     | int    | Ordinal |
| nombre_producto | string | Nominal |
| cantidad        | int    | Razón   |
| precio_unitario | int    | Razón   |
| importe         | int    | Razón   |

**Descripción de los campos:**

- `id_venta`: Identificador de la venta.
- `id_producto`: Identificador del producto.
- `nombre_producto`: Nombre del producto.
- `cantidad`: Cantidad vendida.
- `precio_unitario`: Precio por unidad.
- `importe`: Importe total de la venta.

### Tabla: Clientes

| Campo          | Tipo   | Escala    |
|----------------|--------|-----------|
| id_cliente     | int    | Ordinal   |
| nombre_cliente | string | Nominal   |
| email          | string | Nominal   |
| ciudad         | string | Nominal   |
| fecha_alta     | date   | Intervalo |

**Descripción de los campos:**

- `id_cliente`: Identificador único del cliente.
- `nombre_cliente`: Nombre del cliente.
- `email`: Correo electrónico del cliente.
- `ciudad`: Ciudad de residencia.
- `fecha_alta`: Fecha de alta del cliente.

# 3 Información, pasos, pseudocodigo y diagrama del programa (Sprint 1)

Vamos a crear un programa en Python con el que se pueda visualizar de manera interactiva la documentación, paara que los usuarios puedas acceder de manera sencilla a la información clave del proyecto.

## 3.1 Contenidos accesibles desde el menú

    1. Tema, problema y solución
    2. Origen de los datos
    3. Descripción de la estructura, tipos de datos y escala de la base de datos
    4. Escalas de medición
    5. Sugerencias y mejorsas con Copilot
    6. Salir

## 3.2 Pasos

    1. Cargar en memoria la información de esta documentación.
    2. Mostrar un menú númerico con las secciones enumeradas.
    3. Según la opción que el usuario elija, se imprimirá la información correspondiente a esa sección.
    4. El programa seguirá mostrando el menú hasta que el usuario elija la opción de salir.

## 3.3 Diagrama de flujo: en carpeta

+------------------------+
    |        INICIO          |
    +------------------------+
               |
               v
    +------------------------+
    | Cargar documentación   |
    |    en memoria          |
    +------------------------+
               |
               v
    +------------------------+
    | Bucle principal (siem- |
    | pre)                   |
    +------------------------+
               |
               v
    +------------------------+
    | Limpiar pantalla       |
    +------------------------+
               |
               v
    +------------------------+
    | Mostrar menú (1..7)    |
    | - 1 Tema/Problema      |
    | - 2 Origen datos       |
    | - 3 Estructura BD      |
    | - 4 Pseudocódigo       |
    | - 5 Sugerencias        |
    | - 6 Diagrama (esto)    |
    | - 7 Salir              |
    +------------------------+
               |
               v
    +------------------------+
    | Leer entrada del       |
    | usuario (input)        |
    +------------------------+
               |
               v
    +-------------------------------+
    | ¿La entrada es un número?     |
    +-------------------------------+
        |                           |
       No                           Sí
        |                           v
        |                  +---------------------+
        |                  | ¿Está entre 1 y 7?  |
        |                  +---------------------+
        |                  |                     |
        |                  No                    Sí
        |                  |                     v
        |           +----------------+    +--------------------------+
        |           | Mostrar error  |    | Opción válida (1..6):    |
        |           |"Ingrese número"|    | Mostrar sección          |
        |           +----------------+    +--------------------------+
        |                  |                     |
        |                  v                     v
[Esperar Enter]    [Esperar Enter]         [Esperar Enter]
        |                  |                     |
        +------------------+---------------------+
                           v
           (volver a Bucle principal)

    Si la opción es 7 -> Mostrar despedida y terminar.