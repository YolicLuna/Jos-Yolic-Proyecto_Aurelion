
# 1 Tema, problema y solución

## Documentación del Análisis de Ventas y Clientes

Este es un proyecto creado para
 practicar el análisis, visualización y modelado de datos utilizando python y bibliotecas como pandas, matplotlib, numpy, etc. Vamos a simular la gestión de una tienda realizando un proyecto basándose en datos generados con fines educativos.

### 🎯 Estado Actual del Proyecto
- ✅ **Fase 1:** Limpieza de datos COMPLETADA
- ✅ **Fase 2:** Análisis estadístico descriptivo COMPLETADA

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

### 🏆 Resultados Obtenidos
**✅ Análisis completado exitosamente:**
- **Vista integral** del negocio con todas las dimensiones integradas
- **Insights accionables** extraídos de 4 datasets relacionales  
- **Metodología reproducible** documentada completamente
- **Colaboración efectiva** humano-IA (Usuario 57% - IA 43%)

---

# 2 Origen de los datos

Los datos que usaremos para el análisis provienen de una base de datos de ventas y clientes de una tienda. La base de datos está conformada por 4 archivos CSV, cada archivo contiene una de las tablas que se describen más adelante.

### 📊 Datasets Procesados
**Datos originales → Datos limpios:**
- `Clientes.xlsx` → `Clientes_limpio.csv`
- `Productos.xlsx` → `Productos_limpio.csv`  
- `Ventas.xlsx` → `Ventas_limpio.csv`
- `Detalle_ventas.xlsx` → `Detalle_ventas_limpio.csv`

### 🔗 Integración Relacional
- **Tabla relacional integrada** con 22 columnas
- **Vista 360° del negocio** unificando todas las dimensiones
- **Joins SQL-like** implementados para análisis completo

---

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

---

# 4 🧹 PROCESO DE LIMPIEZA DE DATOS

> **Desarrollado con GitHub Copilot** - Proceso completo de limpieza y normalización de 4 datasets relacionales

## 4.1 Metodología de Limpieza Aplicada

### **5 Fases Sistemáticas**
```
1. 🔍 ANÁLISIS DE PROBLEMAS      → Explorar estructura y detectar errores
2. 🧹 LIMPIEZA DE DATOS          → Corregir errores y duplicados
3. 📊 ESTANDARIZACIÓN           → Homogenizar formatos y tipos
4. 🔄 NORMALIZACIÓN             → Optimizar estructura relacional  
5. ✅ VALIDACIÓN Y EXPORTACIÓN  → Verificar calidad y guardar
```

### **Principios Clave del Proceso**
- **🔗 Preservar integridad relacional**: Mantener conexiones entre tablas
- **⚠️ Duplicados inteligentes**: Distinguir duplicados reales vs transacciones válidas
- **🎯 Normalización**: Eliminar redundancias respetando el modelo de datos
- **📈 One-hot encoding**: Preparar variables categóricas para análisis

## 4.2 Transformaciones Aplicadas por Dataset

### **👥 CLIENTES** 
**Transformaciones aplicadas:**
- **Eliminación de duplicados** → Filas idénticas removidas
- **Normalización de fechas** → Convertidas a datetime + columna `mes_alta`
- **Estandarización de ciudades** → "Cdmx" → "Ciudad de México"
- **Normalización de nombres** → Espacios extra eliminados, formato título
- **Normalización de emails** → Minúsculas, duplicados eliminados

### **🛍️ PRODUCTOS**  
**Transformaciones aplicadas:**
- **Eliminación de duplicados** → Solo duplicados completos
- **Normalización de precios** → Valores absolutos, formato numérico
- **Estandarización de categorías** → "Electronica" → "Electrónica"
- **One-hot encoding** → `categoria` convertida a variables dummy (`cat_Limpieza`, `cat_Alimentos`)

### **💰 VENTAS**
**Transformaciones aplicadas:**
- **⚠️ Eliminación de columnas redundantes** → `nombre_cliente`, `email` (ya están en tabla Clientes)
- **Normalización de fechas** → Datetime + columnas derivadas (`año_venta`, `mes_venta`)
- **One-hot encoding** → `medio_pago` convertido a variables dummy (`pago_Efectivo`, `pago_Qr`, `pago_Tarjeta`, `pago_Transferencia`)

### **📋 DETALLE_VENTAS** ⭐ **Más crítico**
**Transformaciones aplicadas:**
- **⚠️ Eliminación de columna redundante** → `nombre_producto` (disponible en tabla Productos)
- **🔗 Duplicados relacionales** → SOLO eliminación de duplicados completos (preserva transacciones válidas)
- **💰 Recálculo de importes** → `importe = cantidad × precio_unitario` para consistencia
- **🔢 Normalización numérica** → Todos los valores como números, valores absolutos

## 4.3 Decisiones Metodológicas Críticas

### **🔗 Modelo Relacional Optimizado**
```
❌ ANTES: 
- Ventas: id_cliente + nombre_cliente + email
- Detalle_ventas: id_producto + nombre_producto

✅ DESPUÉS: 
- Ventas: solo id_cliente (join con tabla Clientes)
- Detalle_ventas: solo id_producto (join con tabla Productos)
```
**Beneficio:** Normalización 3NF, eliminación de redundancias

---

# 5 📊 PROCESO DE ANÁLISIS ESTADÍSTICO DESCRIPTIVO

> **Desarrollado con GitHub Copilot** - Análisis estadístico descriptivo detallado sobre 4 datasets relacionales con integración completa

## 5.1 Objetivo del Análisis

Realizar un **análisis estadístico descriptivo detallado** sobre los cuatro datasets relacionados, integrándolos en una **tabla relacional** para análisis combinados. Se exploró tendencias, patrones, distribución y relaciones entre variables, usando Python con `pandas`, `numpy`, `matplotlib` y `seaborn`.

## 5.2 🤝 Colaboración Detallada: Usuario vs GitHub Copilot

### **📊 Distribución global de aportes**

| **Contribuyente** | **Porcentaje** | **Tipo de Aporte** |
|-------------------|----------------|---------------------|
| **👨‍🏫 Usuario (José Yolic)** | **57%** | Razonamiento estratégico, decisiones metodológicas, interpretación de negocio |
| **🤖 GitHub Copilot** | **43%** | Implementación técnica, código, documentación, optimizaciones |

### **🎯 Desglose Detallado por Fase**

| **Etapa del Análisis** | **Usuario** | **IA** | **Justificación** |
|------------------------|-------------|--------|-------------------|
| **🔍 Análisis Clientes** | **80%** | **20%** | Usuario definió enfoque completo; IA implementó cálculos |
| **🛍️ Análisis Productos** | **70%** | **30%** | Usuario propuso qué calcular; IA agregó visualizaciones |
| **💰 Análisis Ventas** | **65%** | **35%** | Usuario identificó relevancia; IA creó gráficos temporales |
| **📋 Análisis Detalle Ventas** | **60%** | **40%** | Usuario guió métricas; IA implementó scatter plots avanzados |
| **🔗 Integración Relacional** | **30%** | **70%** | Usuario definió relaciones; IA ejecutó joins complejos |
| **📊 Análisis Relacional** | **55%** | **45%** | Usuario definió qué comparar; IA implementó análisis |

## 5.3 Metodología de Análisis Aplicada

### **5 Fases Sistemáticas**
```
1. 🔍 EXPLORACIÓN INICIAL        → Inspección y carga de datasets limpios
2. 📊 ESTADÍSTICAS DESCRIPTIVAS  → Medidas de tendencia central y dispersión
3. 📈 ANÁLISIS UNIVARIADO        → Distribuciones y patrones individuales
4. 🔗 ANÁLISIS RELACIONAL        → Integración de tablas y análisis multivariado
5. 📋 INSIGHTS Y CONCLUSIONES    → Extracción de patrones y tendencias
```

## 5.4 Análisis Implementado por Dataset

### **👥 Análisis de Clientes**
- **Distribución geográfica** → Clientes por ciudad
- **Análisis temporal** → Altas de clientes por mes
- **Estadísticas generales** → Total clientes, ciudades, rango temporal

### **🛍️ Análisis de Productos**
- **Estadísticas de precios** → Media, mediana, moda, extremos
- **Análisis por categorías** → Distribución Alimentos vs Limpieza
- **Identificación de extremos** → Productos más caros y más baratos

### **💰 Análisis de Ventas**
- **Tendencias temporales** → Ventas por día y por mes
- **Métodos de pago** → Distribución de preferencias de pago
- **Clientes frecuentes** → Top 10 clientes con más compras

### **📋 Análisis de Detalle Ventas**
- **Top productos** → Más vendidos por cantidad y por valor
- **Correlaciones** → Scatter plots cantidad vs precio vs importe
- **Distribuciones** → Histogramas de variables numéricas

## 5.5 🔗 Integración Relacional Completa

### **Proceso de Joins Implementado**
```python
# Secuencia de integración:
1. Clientes ⟵→ Ventas         (mediante id_cliente)
2. Detalle_Ventas ⟵→ Ventas  (mediante id_venta)  
3. Productos ⟵→ Detalle_Ventas (mediante id_producto)
```

**✅ Resultado:** Tabla relacional con 22 columnas para análisis 360° del negocio

### **Análisis Relacional Implementado**
- **🏆 Top Rankings** → Productos más vendidos y clientes con mayor gasto
- **📍 Análisis geográfico** → Ventas por ciudad con segmentación
- **📦 Análisis categórico** → Ventas por categorías (Alimentos/Limpieza)
- **💳 Métodos de pago** → Distribución y tendencias temporales
- **📅 Tendencias temporales** → Evolución mensual integrada

## 5.6 Notebooks de Análisis Desarrollados

```
Analisis_estadistico_descriptivo/
├── Clientes_Analisis.ipynb → Análisis demográfico y temporal
├── Productos_Analisis.ipynb → Análisis de precios y categorías  
├── Ventas_Analisis.ipynb → Análisis de tendencias y métodos de pago
├── Detalle_ventas_Analisis.ipynb → Análisis transaccional y correlaciones
└── Analisis_Relacional.ipynb → Vista integrada 360° ⭐ MÁS COMPLETO
```

---

# 6 Información, pasos, pseudocódigo y diagrama del programa (Sprint 1)

Vamos a crear un programa en Python con el que se pueda visualizar de manera interactiva la documentación, para que los usuarios puedan acceder de manera sencilla a la información clave del proyecto.

## 6.1 Contenidos accesibles desde el menú

    1. Tema, problema y solución
    2. Origen de los datos
    3. Descripción de la estructura, tipos de datos y escala de la base de datos
    4. Proceso de limpieza de datos
    5. Proceso de análisis estadístico descriptivo
    6. Escalas de medición
    7. Sugerencias y mejoras con Copilot
    8. Salir

## 6.2 Pasos

    1. Cargar en memoria la información de esta documentación.
    2. Mostrar un menú numérico con las secciones enumeradas.
    3. Según la opción que el usuario elija, se imprimirá la información correspondiente a esa sección.
    4. El programa seguirá mostrando el menú hasta que el usuario elija la opción de salir.

## 6.3 Diagrama de flujo: en carpeta

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
    | Mostrar menú (1..8)    |
    | - 1 Tema/Problema      |
    | - 2 Origen datos       |
    | - 3 Estructura BD      |
    | - 4 Limpieza datos     |
    | - 5 Análisis estadístico|
    | - 6 Escalas medición   |
    | - 7 Sugerencias        |
    | - 8 Salir              |
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
        |                  | ¿Está entre 1 y 8?  |
        |                  +---------------------+
        |                  |                     |
        |                  No                    Sí
        |                  |                     v
        |           +----------------+    +--------------------------+
        |           | Mostrar error  |    | Opción válida (1..7):    |
        |           |"Ingrese número"|    | Mostrar sección          |
        |           +----------------+    +--------------------------+
        |                  |                     |
        |                  v                     v
[Esperar Enter]    [Esperar Enter]         [Esperar Enter]
        |                  |                     |
        +------------------+---------------------+
                           v
           (volver a Bucle principal)

    Si la opción es 8 -> Mostrar despedida y terminar.

---

# 7 🔍 Insights de Negocio Principales Descubiertos

## 7.1 Descubrimientos por Dimensión de Análisis

### **👥 Insights de Clientes:**
- **🌍 Concentración geográfica** → Identificación de mercados principales
- **📅 Patrones de alta** → Estacionalidad en adquisición de clientes
- **📈 Base de clientes** → Métricas de crecimiento y cobertura

### **🛍️ Insights de Productos:**
- **💰 Estructura de precios** → Rangos y distribución del portfolio
- **📦 Balance categórico** → Proporción Alimentos vs Limpieza  
- **🎯 Productos estrella** → Identificación de extremos de precio

### **💰 Insights de Ventas:**
- **📅 Estacionalidad** → Patrones temporales de demanda
- **💳 Preferencias de pago** → Adopción de métodos digitales vs tradicionales
- **👑 Clientes VIP** → Segmento de alta frecuencia de compra

### **🌐 Insights Relacionales (Vista 360°):**
- **🎯 Cross-insights** → Relaciones entre geografía, productos y métodos pago
- **📊 Tendencias integradas** → Evolución temporal de comportamientos
- **🔄 Patrones de negocio** → Insights que solo emergen con datos integrados

---

# 8 🏆 Conclusión del Proyecto

**✅ Proyecto completado exitosamente en 2 fases:**

### **📊 Logros Alcanzados:**
- **4 datasets procesados** con metodología estructurada
- **5 notebooks de análisis** especializados desarrollados
- **Tabla relacional integrada** con vista 360° del negocio
- **Colaboración efectiva** humano-IA documentada (57%-43%)
- **Insights accionables** extraídos para toma de decisiones

### **🎯 Datos listos para fases siguientes:**
- **Dashboards ejecutivos** y visualizaciones Power BI
- **Estrategias de marketing** basadas en insights de clientes
- **Optimización de portfolio** de productos
- **Modelos predictivos** y machine learning avanzado

### **📈 Valor del análisis realizado:**
- **Metodología reproducible** completamente documentada
- **Base sólida** para análisis avanzados posteriores
- **Enfoque profesional** de Data Analysis guiado por IA
- **Documentación completa** para reproducibilidad

---

**👨‍💻 Proyecto:** José Yolic  
**🤖 Desarrollado con:** GitHub Copilot  
**📅 Fecha:** Octubre 2025
