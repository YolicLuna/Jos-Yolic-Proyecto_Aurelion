# 📊 Dashboard de Ventas – Comercio Aurelion

## 📌 Descripción general

Este proyecto consiste en el desarrollo de un **dashboard interactivo en Power BI** orientado al análisis del desempeño comercial del comercio **Aurelion**. El objetivo principal es proporcionar una visión clara y estructurada de las ventas mediante indicadores clave, análisis temporal y segmentación por clientes, productos, medios de pago y ubicación geográfica, con el fin de apoyar la comprensión del comportamiento del negocio y la toma de decisiones.

El dashboard fue desarrollado aplicando principios de **calidad de datos**, **preparación y transformación**, **modelado relacional**, **uso de medidas DAX**, **KPIs** y **visualización efectiva**, priorizando claridad, coherencia visual y utilidad analítica.

---

## 🗂️ Fuentes de datos

Los datos utilizados provienen de **cuatro archivos en formato CSV**:

* Clientes
* Ventas
* Detalle de ventas
* Productos

Previo a su carga en Power BI, se realizó una **corrección de datos en Excel**, específicamente en la categorización de productos. Esta corrección fue necesaria para resolver inconsistencias donde algunos productos alimenticios estaban clasificados como limpieza y viceversa, lo que impactaba directamente en el análisis y las visualizaciones.

Una vez corregidos los datos en origen, los archivos fueron exportados e importados a Power BI para su posterior transformación, modelado y análisis.

---

## 🔄 Preparación y transformación de datos

Durante la fase de preparación y transformación de datos se llevaron a cabo las siguientes tareas:

* Carga de los archivos CSV corregidos en Power BI
* Revisión y corrección de tipos de datos
* Eliminación de columnas que no aportaban valor analítico
* Creación de columnas derivadas
    * Ejemplo: obtención del **mes de venta** a partir de la **fecha**
* Estandarización de campos para asegurar consistencia entre tablas

Posteriormente, se utilizó la funcionalidad de **Combinar consultas en Power Query** para crear una **tabla general**, consolidando la información relevante de clientes, ventas, productos y detalle de ventas.

Esta tabla se construyó seleccionando únicamente las columnas necesarias para el análisis y eliminando redundancias, sirviendo como base principal para el modelo de datos y las visualizaciones.

---

## 🧱 Modelo de datos

El modelo de datos fue diseñado con un **enfoque relacional**, incorporando:

* Una **tabla general** como tabla central de hechos
* Tablas auxiliares de clientes, productos, ventas y calendario
* Relaciones correctamente definidas para garantizar coherencia en los cálculos

La **tabla de calendario** permite soportar el análisis temporal y la correcta respuesta de las métricas ante filtros por año y mes.

Este enfoque facilita un modelo más claro, eficiente y comprensible, asegurando que las medidas y visualizaciones reaccionen correctamente a los segmentadores del dashboard.

---

## 🧮 Medidas y cálculos (DAX)

Los cálculos principales se realizaron mediante **medidas DAX**, priorizando este enfoque sobre columnas calculadas para permitir análisis dinámicos y dependientes del contexto de filtros.

Entre las medidas implementadas se incluyen:

* Ventas Totales
* Número de Ventas
* Cantidad Vendida
* Ticket Promedio
* Venta Máxima y Venta Mínima
* Ventas Mensuales
* Ventas del Mes Anterior
* Ventas del Último Mes
* Crecimiento Mensual (%)
* Clientes Activos
* Clientes Top
* Promedio de venta por cliente

El uso de medidas DAX permite que los KPIs y gráficos se actualicen correctamente al aplicar segmentaciones por fecha, ciudad, categoría, medio de pago o cliente.

---

## 🗓️ Análisis temporal y jerarquías

Se implementó una **tabla de calendario dedicada**, a partir de la cual se construyeron **jerarquías temporales** que incluyen:

* Año
* Trimestre
* Mes

Asimismo, se configuraron columnas auxiliares para garantizar el **orden correcto de los meses**, evitando inconsistencias visuales en los gráficos.

Estas jerarquías permiten un análisis del desempeño comercial a distintos niveles de granularidad y facilitan la detección de tendencias y variaciones temporales.

---

## 📈 KPIs principales

En la parte superior del dashboard se presentan los KPIs que brindan una visión ejecutiva inmediata del negocio:

* **Ventas Totales**
* **Número de Ventas**
* **Ticket Promedio**

El KPI principal es **Ventas Totales**, ya que refleja el resultado global del negocio. Su interpretación se complementa con el número de ventas y el ticket promedio, permitiendo identificar si el desempeño está asociado al volumen de operaciones o al valor de cada transacción.

---

## 🔍 Análisis y segmentaciones

El dashboard incorpora distintos niveles de análisis:

### 📊 Evolución temporal

* Evolución mensual de las ventas para identificar tendencias, caídas y recuperaciones.
* Se observan variaciones en el desempeño a lo largo del tiempo, influenciadas por la corrección de datos y la distribución real de las categorías.

### 🏙️ Análisis geográfico

* Segmentación de ventas por ciudad.
* Visualización mediante gráficos y mapas para reforzar el contexto espacial.
* Identificación de ciudades con mayor y menor concentración de ventas.

### 💳 Medio de pago

* Análisis del porcentaje de ventas por medio de pago.
* Identificación de preferencias claras de los clientes en los métodos utilizados.

### 👥 Clientes

* Ranking de clientes principales.
* Segmentación por frecuencia de compra (frecuente, esporádico, ocasional).
* Identificación de clientes activos y clientes top.

### 📦 Productos y categorías

* Análisis de ventas y cantidades vendidas por categoría de producto.
* Visualización corregida tras la recategorización de productos, reflejando de manera precisa el aporte real de **alimentos** y **limpieza** en las ventas.

---

## 🔄 Comportamiento interactivo del dashboard

El dashboard fue diseñado como una herramienta totalmente interactiva. Todas las métricas y visualizaciones se recalculan dinámicamente según las selecciones del usuario, como ciudades, categorías, clientes o periodos de tiempo.

Esta interactividad permite pasar de una visión general del negocio a análisis específicos con pocos clics, facilitando un enfoque exploratorio y una mejor comprensión del comportamiento comercial.

---

## 💡 Principales insights

* Las ventas presentan variaciones temporales claras a lo largo del periodo analizado.
* La distribución de ventas no es homogénea entre ciudades.
* Existen preferencias marcadas por determinados medios de pago.
* La corrección en la categorización de productos tuvo un impacto directo en los resultados y visualizaciones.
* El ticket promedio permite identificar operaciones de valor elevado incluso con un número moderado de ventas.

---

## 🎯 Conclusión

Este proyecto demuestra la importancia de la **calidad de datos** como base del análisis. La detección y corrección de errores en el origen permitió construir un modelo más confiable y un dashboard coherente con la realidad del negocio.

El dashboard ofrece una visión descriptiva y temporal del desempeño comercial, considerando ventas, clientes, productos y ubicación geográfica, y constituye una herramienta válida tanto para fines académicos como para apoyar la toma de decisiones comerciales.

---

## 🔮 Posibles mejoras futuras

* Comparaciones contra objetivos o metas comerciales
* Análisis interanual (YoY) y mensual avanzado (MoM)
* Inclusión de métricas predictivas
* Segmentación más profunda por comportamiento del cliente

---

Si luego quieres, en otro mensaje:

* pulimos el lenguaje para **LinkedIn**, o
* sacamos una versión más **técnica** del README, o
* lo adaptamos como **historia de proyecto** para entrevistas

pero tal como está, este README ya comunica **buen criterio analítico y madurez en datos** 👌

