# 📊 Proyecto Aurelion. 
### (Curso Fundamentos de Inteligencia Artificial de IBM y Guayerd)

> **Proyecto educativo de análisis de datos desarrollado con GitHub Copilot**

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-green.svg)](https://pandas.pydata.org/)
[![NumPy](https://img.shields.io/badge/NumPy-Numerical%20Computing-yellow.svg)](https://numpy.org/)
[![Matplotlib](https://img.shields.io/badge/Matplotlib-Visualization-red.svg)](https://matplotlib.org/)
[![Seaborn](https://img.shields.io/badge/Seaborn-Statistical%20Visualization-purple.svg)](https://seaborn.pydata.org/)
[![Scikit-learn](https://img.shields.io/badge/Scikit--learn-Machine%20Learning-orange.svg)](https://scikit-learn.org/)
[![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-orange.svg)](https://jupyter.org/)
[![Power BI](https://img.shields.io/badge/Power%20BI-Dashboard-FFC300.svg)](https://powerbi.microsoft.com/)
[![Status](https://img.shields.io/badge/Status-Fase%204%20Completada-brightgreen.svg)]()

---

## 🎯 Descripción del Proyecto

Este proyecto realiza un **análisis completo de datos de ventas y clientes** de una tienda, implementando técnicas de limpieza, normalización, análisis estadístico predictivo y modelos de Machine Learning. Desarrollado como proyecto educativo para practicar análisis de datos con Python utilizando `pandas`, `numpy`, `matplotlib`, `seaborn` y `scikit-learn`.

### **Objetivos del Análisis**

Determinar estrategias de negocio mediante el análisis de:
- 🛍️ **Productos:** Identificar los menos vendidos, menos rentables y tiempos de rotación
- 👥 **Clientes:** Segmentar por frecuencia de compra, identificar inactivos y estrategias de reactivación
- 💰 **Ventas:** Analizar tendencias temporales, métodos de pago y patrones de consumo
- 📊 **Rentabilidad:** Optimizar el catálogo de productos y estrategias de marketing

---

## 📂 Estructura del Proyecto

```
JoséYolic-Proyecto_Aurelion/
│
├── 📄 README.md                              # Este archivo (resumen ejecutivo)
├── 📋 DOCUMENTACION.md                       # Documentación completa del proyecto
├── 🐍 main.py                                # Programa interactivo de consulta
│
├── 📁 Base_de_datos/                         # Datos originales (Excel)
├── 📁 Base_de_datos_limpia/                  # Datos procesados (CSV)
│   ├── Clientes_limpio.csv
│   ├── Productos_limpio.csv
│   ├── Ventas_limpio.csv
│   └── Detalle_ventas_limpio.csv
│
├── 📁 Limpieza_de_datos/                     # Notebooks de limpieza
│   ├── Clientes.ipynb
│   ├── Productos.ipynb
│   ├── Ventas.ipynb
│   ├── Detalle_ventas.ipynb
│   └── 📋 PROCESO_LIMPIEZA_DETALLADO.md     # Metodología de limpieza
│
├── 📁 Analisis_estadistico_descriptivo/      # Notebooks de análisis
│   ├── Analisis_Relacional.ipynb             # ⭐ Vista 360° integrada
│   └── 📋 PROCESO_ANALISIS_DETALLADO.md      # Metodología de análisis
│
├── 📁 IBM_Ml/                                 # Machine Learning
│   ├── aurelion_ml.ipynb                      # ⭐ Modelos K-Means y Regresión
│   └── 📋 IMPLEMENTACION_ML.md                # Metodología de ML
│
└── 📁 Dasboard_Power_BI/                      # Dashboard y visualización Power BI
    ├── Dashboard_Aurelion.md                  # 📋 Documentación completa
    ├── Dashboard_Aurelion.pbix                # 📊 Archivo Power BI Desktop
    ├── Visuales_dashboard.ipynb               # 📓 Jupyter con análisis visuales
    └── 📁 imagenes/                           # Capturas y gráficos del dashboard
```

---

## 🗃️ Datasets Utilizados

El proyecto trabaja con **4 datasets relacionales** que conforman un modelo estrella:

### **👥 Clientes** (`Clientes_limpio.csv`)
```
Columnas: id_cliente, nombre_cliente, email, ciudad, fecha_alta, mes_alta
```

### **🛍️ Productos** (`Productos_limpio.csv`)
```
Columnas: id_producto, nombre_producto, precio_unitario, cat_Alimentos, cat_Limpieza
```

### **💰 Ventas** (`Ventas_limpio.csv`)
```
Columnas: id_venta, fecha, id_cliente, año_venta, mes_venta, 
          pago_Efectivo, pago_Qr, pago_Tarjeta, pago_Transferencia
```

### **📋 Detalle Ventas** (`Detalle_ventas_limpio.csv`)
```
Columnas: id_venta, id_producto, cantidad, precio_unitario, importe
```

---

## 🔄 Fases del Proyecto

### **✅ Fase 1: Limpieza de Datos** *(COMPLETADA)*

Proceso sistemático de normalización y preparación de datos:

- 🧹 **Eliminación de duplicados inteligente** (distinguiendo transacciones válidas)
- 📊 **Normalización de formatos** (fechas, precios, nombres, emails)
- 🔗 **Optimización relacional** (eliminación de redundancias, modelo 3NF)
- 📈 **One-hot encoding** de variables categóricas (`categoria`, `medio_pago`)
- ✅ **Validación de integridad** (recálculo de importes, verificación de FKs)

> 📋 **Detalles completos:** Ver [`Limpieza_de_datos/PROCESO_LIMPIEZA_DETALLADO.md`](Limpieza_de_datos/PROCESO_LIMPIEZA_DETALLADO.md)

### **✅ Fase 2: Análisis Estadístico Descriptivo** *(COMPLETADA)*

Análisis exhaustivo con estadísticas descriptivas y visualizaciones:

- 📊 **Análisis univariado** por cada dataset (distribuciones, tendencias centrales)
- 🔗 **Integración relacional** mediante joins SQL-like (tabla de 22 columnas)
- 📈 **Análisis multivariado** (correlaciones, scatter plots, tendencias temporales)
- 🏆 **Rankings y top insights** (productos más vendidos, clientes VIP, ventas por ciudad)
- 📅 **Análisis temporal** (estacionalidad, evolución de métodos de pago)

> 📋 **Detalles completos:** Ver [`Analisis_estadistico_descriptivo/PROCESO_ANALISIS_DETALLADO.md`](Analisis_estadistico_descriptivo/PROCESO_ANALISIS_DETALLADO.md)

### **✅ Fase 3: Implementación de Machine Learning** *(COMPLETADA)*

Modelos de clustering y regresión sobre datos integrados:

- 🤖 **K-Means Clustering** (segmentación de 64 clientes en 4 clusters)
- 📈 **Regresión Lineal** (predicción de importes de ventas)
- 📊 **4 visualizaciones ML** (dispersión, residuos, distribución errores, evaluación)
- 🎯 **Estrategias personalizadas** por cluster de clientes
- 📉 **Métricas de evaluación** (MAE, R², análisis de heterocedasticidad)

> 📋 **Detalles completos:** Ver [`IBM_Ml/IMPLEMENTACION_ML.md`](IBM_Ml/IMPLEMENTACION_ML.md)

### **✅ Fase 4: Visualización Power BI** *(COMPLETADA)*

Dashboards ejecutivos y visualizaciones interactivas:

- 📊 **Modelo relacional** con tabla de calendario dedicada
- 🧮 **11 medidas DAX** para cálculos dinámicos (Ventas Totales, Ticket Promedio, etc.)
- 📈 **KPIs ejecutivos** (3 principales: Ventas, Número de Ventas, Ticket Promedio)
- 🎨 **5 tipos de análisis** (Temporal, Geográfico, Pago, Clientes, Productos)
- 🔄 **Interactividad completa** con segmentadores vinculados y actualización dinámica
- 📈 **Jerarquías temporales** (Año → Trimestre → Mes)
- 🔍 Identificación de **tendencias, patrones estacionales y anomalías**

> 📋 **Documentación:** Ver [`Dashboard_Aurelion.md`](Dashboard_Aurelion.md)

### **🔄 Fase 5: Optimización de Modelos ML** *(PENDIENTE)*

Modelos ensemble y feature engineering avanzado. Integración de modelos predictivos en Power BI.

---

## 🤖 Colaboración Humano-IA

Este proyecto demuestra una **colaboración efectiva entre razonamiento humano y asistencia de IA**:

### **📊 Distribución de Aportes**

| Contribuyente | Porcentaje | Tipo de Aporte |
|--------------|------------|----------------|
| **👨‍🏫 Usuario (José Yolic)** | **70-72%** | Razonamiento estratégico, decisiones metodológicas, interpretación de negocio, diseño e implementación de Dashboard Power BI |
| **🤖 GitHub Copilot** | **28-30%** | Implementación técnica, código Python, documentación, optimizaciones (Fases 1-3) |

### **🎯 Valor de Cada Contribuyente**

**👨‍🏫 Aporte del Usuario:**
- ✅ Identificación de variables analíticas vs únicas
- ✅ Decisiones críticas sobre normalización y duplicados
- ✅ Interpretación de patrones de negocio
- ✅ Dirección estratégica del análisis
- ✅ Validación de metodología y resultados
- ✅ **Diseño e implementación completa del Dashboard Power BI** (Fase 4)
- ✅ Modelo relacional Power BI con tabla de calendario
- ✅ Creación de 11 medidas DAX
- ✅ Configuración de segmentadores y jerarquías temporales
- ✅ Análisis multidimensional interactivo

**🤖 Aporte de GitHub Copilot:**
- ✅ Implementación técnica completa (código Python)
- ✅ Joins relacionales complejos y análisis multivariado
- ✅ Visualizaciones profesionales (histogramas, scatter plots, series temporales)
- ✅ Documentación estructurada y reproducible
- ✅ Optimizaciones de rendimiento y buenas prácticas

> 📋 **Desglose detallado por fase:** Ver sección de colaboración en [`Analisis_estadistico_descriptivo/PROCESO_ANALISIS_DETALLADO.md`](Analisis_estadistico_descriptivo/PROCESO_ANALISIS_DETALLADO.md)

---

## 🚀 Uso del Proyecto

### **1️⃣ Instalación de Dependencias**

```bash
pip install pandas numpy matplotlib seaborn jupyter openpyxl
```

### **2️⃣ Exploración de Notebooks**

**Limpieza de datos:**
```bash
jupyter notebook Limpieza_de_datos/
```

**Análisis estadístico:**
```bash
jupyter notebook Analisis_estadistico_descriptivo/
```

**⭐ Machine Learning:**
```bash
jupyter notebook IBM_Ml/
```

**📊 Dashboard Power BI:**
```bash
# Ver archivos en Dasboard_Power_BI/
# - Dashboard_Aurelion.pbix: Archivo Power BI Desktop
# - Visuales_dashboard.ipynb: Jupyter con análisis de visuales
``` 
- Comenzar con `Analisis_Relacional.ipynb` para una vista integrada 360° del negocio
- Explorar `aurelion_ml.ipynb` para ver modelos K-Means y Regresión Lineal

### **3️⃣ Programa Interactivo de Documentación**

```bash
python main.py
```

Accede a un menú interactivo con:
1. Tema, problema y solución
2. Origen de los datos
3. Estructura y tipos de datos
4. Proceso de limpieza detallado
5. Proceso de análisis estadístico predictivo
6. Implementación de Machine Learning
7. Dashboard Power BI
8. Insights de negocio principales
9. Pseudocódigo del programa
10. Sugerencias y mejoras con Copilot
11. Diagrama de flujo
12. Salir

---

## 📊 Insights Principales Descubiertos

### **👥 Clientes**
- 🌍 Concentración geográfica en mercados principales
- 📅 Patrones estacionales en alta de clientes
- 👑 Identificación de segmento VIP por frecuencia de compra

### **🛍️ Productos**
- 💰 Análisis de estructura de precios y rangos
- 📦 Balance categórico entre Alimentos y Limpieza
- 🎯 Identificación de productos estrella y de baja rotación

### **💰 Ventas**
- 📅 Estacionalidad clara en patrones de demanda
- 💳 Evolución temporal de métodos de pago (digital vs tradicional)
- 📈 Tendencias de crecimiento por mes y año

### **🔗 Vista Relacional 360°**
- 🎯 Cross-insights entre geografía, productos y métodos de pago
- 📊 Correlaciones entre variables que emergen solo con datos integrados
- 🔄 Patrones de comportamiento de clientes por categoría y ubicación

### **🤖 Machine Learning**
- 🎯 **4 clusters de clientes** con perfiles y estrategias diferenciadas
- 👑 **Cluster VIP** identificado (16 clientes de alto gasto)
- 📈 **Modelo predictivo baseline** para importes de ventas
- ⚠️ **Áreas de mejora** identificadas (heterocedasticidad, feature engineering)

### **📊 Dashboard Power BI**
- 📈 **Evolución temporal clara** con identificación de tendencias y estacionalidad
- 🗺️ **Análisis geográfico** mostrando concentración de ventas por ciudad
- 💳 **Segmentación de métodos de pago** con tendencias digitales vs tradicionales
- 👥 **Segmentación de clientes** identificando VIP y ocasionales
- 📦 **Análisis de productos y categorías** con participación en ventas
- 🔄 **Interactividad completa** permitiendo análisis dinámicos multidimensionales
- 🎯 **KPIs sincronizados** que se recalculan automáticamente según filtros

---

## 📈 Metodología Implementada

### **🧹 Limpieza de Datos (5 Fases)**
```
1. 🔍 ANÁLISIS DE PROBLEMAS      → Exploración y detección de errores
2. 🧹 LIMPIEZA DE DATOS          → Corrección y eliminación de duplicados
3. 📊 ESTANDARIZACIÓN           → Homogenización de formatos
4. 🔄 NORMALIZACIÓN             → Optimización relacional (3NF)
5. ✅ VALIDACIÓN Y EXPORTACIÓN  → Verificación de calidad
```

### **📊 Análisis Estadístico (5 Fases)**
```
1. 🔍 EXPLORACIÓN INICIAL        → Carga y exploración de datasets limpios
2. 📊 ESTADÍSTICAS DESCRIPTIVAS  → Tendencia central y dispersión
3. 📈 ANÁLISIS UNIVARIADO        → Distribuciones individuales
4. 🔗 ANÁLISIS RELACIONAL        → Integración y análisis multivariado
5. 📋 INSIGHTS Y CONCLUSIONES    → Extracción de patrones
```

### **🤖 Machine Learning (2 Modelos)**
```
1. 🎯 K-MEANS CLUSTERING         → Segmentación de 64 clientes en 4 grupos
2. 📈 REGRESIÓN LINEAL           → Predicción de importes (baseline)
3. 📊 VISUALIZACIONES ML         → 4 gráficos de evaluación
4. 🔧 MÉTRICAS DE EVALUACIÓN     → MAE, R², análisis de residuos
5. 💡 RECOMENDACIONES            → Mejoras y modelos avanzados
```

### **📊 Business Intelligence – Power BI**
### 🧩 Preparación y Modelado en Power BI (5 Fases)
```
1. 📂 CARGA DE DATOS             → Importación de 4 archivos CSV en Power BI
2. 🧹 TRANSFORMACIÓN (Power Query) → Limpieza, eliminación de columnas y ajuste de tipos
3. 🧮 COLUMNAS DERIVADAS         → Creación de campos calculados (mes, año, periodos)
4. 🧱 MODELO DE DATOS            → Definición de relaciones y cardinalidades
5. 📅 TABLA DE CALENDARIO        → Soporte para análisis temporal y jerarquías
```
### 🧮 Cálculo de Métricas y KPIs (DAX)
```
1. 📊 MEDIDAS PRINCIPALES        → Ventas totales, número de ventas, ticket promedio
2. 📈 MÉTRICAS TEMPORALES        → Ventas mensuales, mes anterior, último mes
3. 🔄 CRECIMIENTO (%)            → Comparaciones temporales dinámicas
4. ⚠️ VALORES EXTREMOS           → Venta máxima y mínima
5. 🎯 MÉTRICAS POR CONTEXTO      → Cálculos sensibles a filtros y segmentadores
```
### 📈 Visualización e Interactividad
```
1. 📊 DISEÑO DE KPIs             → Indicadores ejecutivos en vista general
2. 📉 ANÁLISIS TEMPORAL          → Evolución mensual con jerarquías
3. 🏙️ SEGMENTACIÓN GEOGRÁFICA    → Análisis por ciudad y mapa
4. 💳 SEGMENTADORES              → Medio de pago, frecuencia de clientes, categorías
5. 🔁 INTERACCIÓN CRUZADA        → Actualización dinámica de visuales al seleccionar datos
```

---

### 🛠️ Tecnologías Utilizadas- **Python 3.8+** - Lenguaje principal
- **Pandas** - Manipulación y análisis de datos
- **NumPy** - Operaciones numéricas
- **Matplotlib** - Visualizaciones básicas
- **Seaborn** - Visualizaciones estadísticas avanzadas
- **Scikit-learn** - Machine Learning (K-Means, Regresión Lineal)
- **Jupyter Notebook** - Entorno de desarrollo interactivo
- **GitHub Copilot** - Asistente de IA para desarrollo
- **Power BI Desktop** - Creación de dashboards interactivos, modelado de datos, medidas DAX y visualización de KPIs
- **Visual Studio Code** - Editor de código para desarrollo en Python, análisis de datos y control de versiones con Git
- **Git** – Control de versiones para gestión y seguimiento de cambios en proyectos
- **GitHub** – Repositorios remotos, documentación de proyectos y portafolio de código

---

## 📋 Documentación Completa

Para información detallada sobre cada fase del proyecto:

- 📄 **[DOCUMENTACION.md](DOCUMENTACION.md)** - Documentación general completa
- 🧹 **[PROCESO_LIMPIEZA_DETALLADO.md](Limpieza_de_datos/PROCESO_LIMPIEZA_DETALLADO.md)** - Metodología de limpieza paso a paso
- 📊 **[PROCESO_ANALISIS_DETALLADO.md](Analisis_estadistico_descriptivo/PROCESO_ANALISIS_DETALLADO.md)** - Metodología de análisis estadístico
- 🤖 **[IMPLEMENTACION_ML.md](IBM_Ml/IMPLEMENTACION_ML.md)** - Metodología de Machine Learning
- 📊 **[Dashboard_Aurelion.md](Dasboard_Power_BI/Dashboard_Aurelion.md)** - Documentación del Dashboard Power BI

---

## 🎯 Resultados y Entregables

### **✅ Datasets Limpios**
- 4 archivos CSV normalizados y optimizados
- Modelo relacional en 3NF implementado
- Variables categóricas codificadas (one-hot encoding)

### **✅ Análisis Completo**
- 5 notebooks de análisis especializados
- Tabla relacional integrada (22 columnas)
- Visualizaciones profesionales (histogramas, boxplots, scatter plots, series temporales)
- 11 visualizaciones de análisis estadístico
- 4 visualizaciones de evaluación ML

### **✅ Modelos de Machine Learning**
- K-Means: 4 clusters con estrategias diferenciadas
- Regresión Lineal: modelo baseline con métricas calculadas
- Segmentación de 64 clientes completada
- Identificación de clientes VIP

### **✅ Dashboard Power BI**
- Modelo relacional con tabla de calendario dedicada
- 11 medidas DAX para cálculos dinámicos
- 3 KPIs principales (Ventas Totales, Número de Ventas, Ticket Promedio)
- 5 tipos de análisis (Temporal, Geográfico, Pago, Clientes, Productos)
- Jerarquías temporales (Año → Trimestre → Mes)
- Segmentadores interactivos con sincronización automática
- Visualizaciones multidimensionales

### **✅ Documentación**
- Proceso metodológico completo documentado
- Decisiones técnicas justificadas
- Reproducibilidad garantizada

---

## 🏆 Conclusión

Este proyecto demuestra un **enfoque profesional de Data Analysis**, combinando:

- ✅ **Metodología estructurada** con criterios claros (4 fases completadas)
- ✅ **Técnicas estadísticas apropiadas** para cada tipo de variable
- ✅ **Integración relacional completa** para insights multidimensionales
- ✅ **Machine Learning implementado** con 2 modelos funcionales
- ✅ **Dashboard Power BI ejecutivo** con análisis interactivos multidimensionales
- ✅ **Colaboración efectiva** entre razonamiento humano y asistencia de IA
- ✅ **Documentación exhaustiva** para reproducibilidad

**🎯 Datos listos para:**
- ✅ Dashboards ejecutivos y visualizaciones Power BI (implementado)
- Estrategias de marketing personalizadas por cluster
- Optimización de portfolio de productos
- Mejora de modelos predictivos (ensemble, feature engineering)
- Toma de decisiones estratégicas basadas en datos

---

## 👤 Autor

**José Yolic**  
Proyecto educativo de análisis de datos

---

## 📅 Fecha

**Diciembre 2025**

---

## 📜 Licencia

Ver archivo [LICENSE](LICENSE) para detalles.

---

**⭐ Si este proyecto te resulta útil, considera darle una estrella en GitHub!**
