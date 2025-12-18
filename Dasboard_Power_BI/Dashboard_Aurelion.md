# 📊 Dashboard de Ventas – Comercio Aurelion

## 📌 Descripción general

Este proyecto consiste en el desarrollo de un **dashboard interactivo en Power BI** orientado al análisis del desempeño comercial del comercio **Aurelion**. El objetivo principal es proporcionar una visión clara y estructurada de las ventas mediante indicadores clave, análisis temporal y segmentación por clientes, productos, medios de pago y ubicación geográfica, con el fin de apoyar la comprensión del comportamiento del negocio y la toma de decisiones.

El dashboard fue desarrollado siguiendo principios de **modelado de datos**, **uso de medidas DAX**, **KPIs** y **visualización efectiva**, priorizando claridad, coherencia visual y utilidad analítica.

---

## 🗂️ Fuentes de datos

Los datos utilizados provienen de **cuatro archivos en formato CSV**:

* Clientes
* Ventas
* Detalle de ventas
* Productos

Todo el proceso de carga y preparación de los datos se realizó **dentro de Power BI**

---

## 🔄 Preparación y transformación de datos

Durante la fase de preparación de datos se realizaron las siguientes tareas:

* Carga de los archivos CSV en Power BI
* Eliminación de columnas que no aportaban valor al análisis
* Corrección de tipos y formatos de datos
* Creación de columnas derivadas a partir de campos existentes
 * Ejemplo: obtención del **mes** a partir de la **fecha de venta**
* Unificación y estructuración de los datos para su posterior análisis

Este proceso permitió contar con datos limpios y consistentes antes de la construcción del modelo y las visualizaciones.

---

## 🧱 Modelo de datos

El modelo de datos fue diseñado con un **enfoque relacional**, conectando las tablas de ventas con clientes, productos y detalle de ventas.
Adicionalmente, se incorporó una **tabla de calendario** para soportar el análisis temporal.

Este enfoque garantiza que las métricas respondan correctamente a los filtros y segmentadores del dashboard, asegurando coherencia en los resultados.

---

## 🧮 Medidas y cálculos (DAX)

Para los cálculos principales se utilizaron **medidas DAX**, priorizando este enfoque sobre columnas calculadas para permitir cálculos dinámicos y sensibles al contexto de filtros.

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
* Métricas orientadas al análisis de clientes (clientes activos, clientes top, promedio por cliente)

El uso de medidas permite que los KPIs y visualizaciones se actualicen correctamente al aplicar segmentaciones por fecha, ciudad, categoría, medio de pago o cliente.

---

## 🗓️ Análisis temporal y jerarquías

Se implementó una **tabla de calendario dedicada**, a partir de la cual se construyeron **jerarquías temporales** que incluyen:

* Año
* Trimestre
* Mes

Asimismo, se configuraron columnas auxiliares para asegurar el **orden correcto de los meses**, evitando inconsistencias visuales en los gráficos.

Estas jerarquías permiten una navegación temporal más intuitiva y facilitan el análisis del desempeño comercial a distintos niveles de granularidad.

---

## 📈 KPIs principales

En la parte superior del dashboard se presentan los KPIs que brindan una visión ejecutiva inmediata del negocio:

* **Ventas Totales**
* **Número de Ventas**
* **Ticket Promedio**

El KPI principal es **Ventas Totales**, ya que refleja el resultado global del negocio. Sin embargo, su interpretación se complementa con el número de ventas y el ticket promedio, lo que permite entender si el desempeño se debe a volumen o a valor por transacción.

---

## 🔍 Análisis y segmentaciones

El dashboard incorpora distintos niveles de análisis:

### 📊 Evolución temporal

* Evolución mensual de las ventas para identificar tendencias, caídas y recuperaciones.
* Se observa una caída intermedia seguida de una recuperación en meses posteriores, lo que sugiere un comportamiento estacional o una baja puntual.

### 🏙️ Análisis geográfico

* Segmentación de ventas por ciudad.
* Visualización mediante gráficos y un mapa geográfico para reforzar el contexto espacial.
* Se identifica concentración de ventas en algunas localidades, mientras que otras presentan menor desempeño.

### 💳 Medio de pago

* Análisis del porcentaje de ventas por medio de pago.
* Se observa que un método concentra una proporción significativa de las ventas, reflejando preferencias claras de los clientes.

### 👥 Clientes

* Ranking de clientes principales.
* Segmentación por frecuencia de compra (frecuente, esporádico, ocasional).
* Identificación de clientes activos y clientes top.

### 📦 Productos y categorías

* Análisis de ventas por categoría de producto.
* Identificación de categorías con mayor participación en las ventas.

---
## Comportamiento interactivo del dashboard

El dashboard fue diseñado como una herramienta totalmente interactiva, permitiendo que todas las métricas y visualizaciones se actualicen dinámicamente en función de las selecciones realizadas por el usuario. Al interactuar con distintos elementos del dashboard, como ciudades, frecuencia de clientes o clientes específicos, el resto de los indicadores se recalculan automáticamente, facilitando un análisis exploratorio más profundo.

La selección de una ciudad desde los recuadros de segmentación actualiza en tiempo real los KPIs, gráficos temporales, análisis por medio de pago y métricas de clientes, permitiendo evaluar el desempeño comercial de cada localidad de forma individual. De igual manera, al seleccionar una categoría de frecuencia de clientes o un nombre dentro del ranking de los clientes top, el dashboard ajusta los resultados para mostrar exclusivamente la información asociada a dicha selección.

Este comportamiento interactivo se logra gracias al uso de medidas DAX, relaciones correctamente definidas en el modelo de datos y segmentadores configurados para trabajar de forma conjunta. La interactividad permite pasar de una visión general del negocio a un análisis específico con pocos clics, fortaleciendo el uso del dashboard como una herramienta de análisis y apoyo a la toma de decisiones.

## 💡 Principales insights

* Las ventas presentan variaciones temporales con caídas y recuperaciones claras.
* Las ventas no se distribuyen de forma homogénea entre ciudades.
* Existe una fuerte preferencia por ciertos medios de pago.
* El ticket promedio es elevado en relación con el número de ventas, lo que indica operaciones de mayor valor.
* La diferencia entre venta máxima y mínima permite identificar posibles transacciones atípicas.

---

## 🎯 Conclusión

En conjunto, el dashboard permite analizar el desempeño comercial desde un enfoque descriptivo y temporal, considerando volumen de ventas, valor promedio, distribución geográfica y hábitos de consumo.
El proyecto prioriza claridad, coherencia visual y utilidad analítica, evitando redundancias y sobrecarga de información.

Este dashboard cumple con los objetivos académicos del proyecto y constituye una herramienta válida tanto para el análisis académico como para apoyar la toma de decisiones comerciales y estratégicas.

---

## 🔮 Posibles mejoras futuras

* Comparaciones contra objetivos o metas comerciales
* Análisis contra periodos anteriores (YoY, MoM avanzado)
* Incorporación de métricas predictivas
* Segmentación más profunda por comportamiento del cliente
