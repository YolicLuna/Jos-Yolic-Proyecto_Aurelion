# 📊 Análisis de Ventas y Clientes - Proyecto Aurelion

> **Proyecto educativo de análisis de datos desarrollado con GitHub Copilot**

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-green.svg)](https://pandas.pydata.org/)
[![NumPy](https://img.shields.io/badge/NumPy-Numerical%20Computing-yellow.svg)](https://numpy.org/)
[![Matplotlib](https://img.shields.io/badge/Matplotlib-Visualization-red.svg)](https://matplotlib.org/)
[![Seaborn](https://img.shields.io/badge/Seaborn-Statistical%20Visualization-purple.svg)](https://seaborn.pydata.org/)
[![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-orange.svg)](https://jupyter.org/)
[![Status](https://img.shields.io/badge/Status-Fase%202%20Completada-brightgreen.svg)]()

---

## 🎯 Descripción del Proyecto

Este proyecto realiza un **análisis completo de datos de ventas y clientes** de una tienda, implementando técnicas de limpieza, normalización, y análisis estadístico descriptivo. Desarrollado como proyecto educativo para practicar análisis de datos con Python utilizando `pandas`, `numpy`, `matplotlib` y `seaborn`.

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
└── 📁 Analisis_estadistico_descriptivo/      # Notebooks de análisis
    ├── Clientes_Analisis.ipynb
    ├── Productos_Analisis.ipynb
    ├── Ventas_Analisis.ipynb
    ├── Detalle_ventas_Analisis.ipynb
    ├── Analisis_Relacional.ipynb             # ⭐ Vista 360° integrada
    └── 📋 PROCESO_ANALISIS_DETALLADO.md      # Metodología de análisis
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

### **🔄 Fase 3: Visualización Power BI** *(PENDIENTE)*

Dashboards ejecutivos y visualizaciones interactivas.

### **🔄 Fase 4: Machine Learning** *(PENDIENTE)*

Modelos predictivos y análisis avanzado.

---

## 🤖 Colaboración Humano-IA

Este proyecto demuestra una **colaboración efectiva entre razonamiento humano y asistencia de IA**:

### **📊 Distribución de Aportes**

| Contribuyente | Porcentaje | Tipo de Aporte |
|--------------|------------|----------------|
| **👨‍🏫 Usuario (José Yolic)** | **57%** | Razonamiento estratégico, decisiones metodológicas, interpretación de negocio |
| **🤖 GitHub Copilot** | **43%** | Implementación técnica, código, documentación, optimizaciones |

### **🎯 Valor de Cada Contribuyente**

**👨‍🏫 Aporte del Usuario:**
- ✅ Identificación de variables analíticas vs únicas
- ✅ Decisiones críticas sobre normalización y duplicados
- ✅ Interpretación de patrones de negocio
- ✅ Dirección estratégica del análisis
- ✅ Validación de metodología y resultados

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

**⭐ Recomendación:** Comenzar con `Analisis_Relacional.ipynb` para una vista integrada 360° del negocio.

### **3️⃣ Programa Interactivo de Documentación**

```bash
python main.py
```

Accede a un menú interactivo con:
1. Tema, problema y solución
2. Origen de los datos
3. Estructura y tipos de datos
4. Proceso de limpieza detallado
5. Proceso de análisis estadístico
6. Escalas de medición
7. Sugerencias y mejoras con Copilot
8. Salir

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

---

## 🛠️ Tecnologías Utilizadas

- **Python 3.8+** - Lenguaje principal
- **Pandas** - Manipulación y análisis de datos
- **NumPy** - Operaciones numéricas
- **Matplotlib** - Visualizaciones básicas
- **Seaborn** - Visualizaciones estadísticas avanzadas
- **Jupyter Notebook** - Entorno de desarrollo interactivo
- **GitHub Copilot** - Asistente de IA para desarrollo

---

## 📋 Documentación Completa

Para información detallada sobre cada fase del proyecto:

- 📄 **[DOCUMENTACION.md](DOCUMENTACION.md)** - Documentación general completa
- 🧹 **[PROCESO_LIMPIEZA_DETALLADO.md](Limpieza_de_datos/PROCESO_LIMPIEZA_DETALLADO.md)** - Metodología de limpieza paso a paso
- 📊 **[PROCESO_ANALISIS_DETALLADO.md](Analisis_estadistico_descriptivo/PROCESO_ANALISIS_DETALLADO.md)** - Metodología de análisis estadístico

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

### **✅ Documentación**
- Proceso metodológico completo documentado
- Decisiones técnicas justificadas
- Reproducibilidad garantizada

---

## 🏆 Conclusión

Este proyecto demuestra un **enfoque profesional de Data Analysis**, combinando:

- ✅ **Metodología estructurada** con criterios claros
- ✅ **Técnicas estadísticas apropiadas** para cada tipo de variable
- ✅ **Integración relacional completa** para insights multidimensionales
- ✅ **Colaboración efectiva** entre razonamiento humano y asistencia de IA
- ✅ **Documentación exhaustiva** para reproducibilidad

**🎯 Datos listos para:**
- Dashboards ejecutivos y visualizaciones Power BI
- Estrategias de marketing basadas en insights
- Optimización de portfolio de productos
- Modelos predictivos y machine learning avanzado

---

## 👤 Autor

**José Yolic**  
Proyecto educativo de análisis de datos

---

## 🤖 Desarrollado Con

**GitHub Copilot** - Asistente de IA para implementación técnica, optimizaciones y documentación

---

## 📅 Fecha

**Octubre 2025**

---

## 📜 Licencia

Ver archivo [LICENSE](LICENSE) para detalles.

---

**⭐ Si este proyecto te resulta útil, considera darle una estrella en GitHub!**
