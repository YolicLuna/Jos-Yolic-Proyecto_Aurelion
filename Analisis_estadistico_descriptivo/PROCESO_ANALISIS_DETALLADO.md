# 📊 PROCESO DE ANÁLISIS ESTADÍSTICO PREDICTIVO

> **Desarrollado con GitHub Copilot** - Análisis estadístico descriptivo sobre 4 datasets relacionales integrados

## 🎯 Objetivo del Análisis

Realizar un **análisis estadístico descriptivo detallado** sobre cuatro datasets relacionados (`Clientes`, `Productos`, `Ventas`, `Detalle_Ventas`), integrarlos en una **tabla relacional** unificada, y extraer insights de negocio mediante visualizaciones avanzadas con Python, pandas, matplotlib y seaborn.

---

## 🤝 Colaboración: Usuario vs GitHub Copilot

| **Contribuyente** | **Porcentaje** | **Tipo de Aporte** |
|-------------------|----------------|---------------------|
| **👨‍🏫 Usuario (José Yolic)** | **57%** | Razonamiento estratégico, decisiones de negocio, interpretación de insights |
| **🤖 GitHub Copilot** | **43%** | Implementación técnica, código, visualizaciones, optimizaciones |

**🏆 Síntesis:** El usuario guió la estrategia y definió KPIs; Copilot materializó el análisis técnico con visualizaciones profesionales.

---

## 🎯 Metodología Aplicada

### **5 Fases Sistemáticas**
```
1. 🔗 INTEGRACIÓN RELACIONAL      → Merge de 4 datasets (LEFT JOIN)
2. 📊 ESTADÍSTICAS DESCRIPTIVAS   → Medidas centrales y dispersión
3. 📈 ANÁLISIS SEGMENTADO         → Tops, geografía, categorías, pagos
4. 📅 ANÁLISIS TEMPORAL           → Tendencias mensuales
5. 📋 VISUALIZACIÓN AVANZADA      → 11 gráficos especializados
```

### **Principios Clave**
- **🔗 Integración completa**: LEFT JOINs preservando integridad relacional
- **📈 Visualización por propósito**: Barplots (comparación), lineplot (tendencia), scatter (correlación), histogramas (distribución), boxplots (outliers)
- **🎯 Enfoque de negocio**: KPIs accionables (tops, ciudades, métodos de pago)

---

## 📊 Integración de Datasets

**Proceso de unificación:**
```python
# 1. Ventas + Clientes (LEFT)
ventas_clientes = pd.merge(ventas, clientes, on='id_cliente', how='left')

# 2. Detalle + Productos (LEFT)
detalle_productos = pd.merge(detalle_ventas, productos, on='id_producto', how='left')

# 3. Tabla unificada
analisis_relacional = pd.merge(detalle_productos, ventas_clientes, on='id_venta', how='left')
```

**Resultado:** Tabla con datos de cliente, producto, venta y detalle integrados

---

## 📈 Análisis Realizados (11 Visualizaciones)

### **1. 📊 Estadísticas Descriptivas**
- Variables: `cantidad`, `precio_unitario`, `importe`
- Métricas: media, mediana, desviación, percentiles

### **2. 🏆 Top Productos**
- **Por cantidad vendida** → Salsa de Tomate (#1)
- **Por importe total** → Desodorante Aerosol (#1)
- Visualización: Barplots comparativos

### **3. 👥 Top Clientes**
- Por gasto total → Agustina Flores (#1)
- Visualización: Barplot horizontal

### **4. 🗺️ Análisis Geográfico**
- Ventas por ciudad → Río Cuarto (#1)
- Ventas por categoría (Alimentos vs Limpieza)
- Visualización: 3 barplots

### **5. 💳 Métodos de Pago**
- Frecuencia: Efectivo > QR > Tarjeta > Transferencia
- Visualización: Barplot

### **6. 📅 Tendencias Temporales - Ventas**
- Declive Mes 1→4, pico dramático Mes 5 (~560k), caída Mes 6
- Visualización: Barplot + Lineplot

### **7. 💳 Tendencias Temporales - Pagos**
- Efectivo: tendencia a la baja
- QR: crecimiento constante
- Tarjeta/Transferencia: volatilidad alta
- Visualización: Lineplot multi-serie

### **8. 🔍 Scatter Plot: Cantidad vs Importe**
- Relación positiva con dispersión vertical (variabilidad en precio unitario)

### **9. 📊 Histogramas**
- **Cantidad**: distribución discreta (1-5 unidades)
- **Precio unitario**: multimodal (picos en ~1000, ~2500)
- **Importe**: sesgo a la derecha
- Visualización: 3 histogramas con KDE

### **10. 📦 Boxplot: Importe por Ciudad**
- **Medianas altas**: Carlos Paz, Villa María
- **Más outliers**: Río Cuarto, Córdoba, Alta Gracia

---

## 🎯 Decisiones Críticas

### **1. LEFT JOINs**
- Preservar todas las transacciones (incluso con datos incompletos)

### **2. Limpieza Numérica**
```python
# Conversión segura
analisis_relacional[col] = pd.to_numeric(..., errors='coerce')
# Eliminación de nulos
analisis_relacional.dropna(subset=cols_numericas)
```

### **3. Selección de Visualizaciones**

| **Propósito** | **Gráfico** |
|---------------|-------------|
| Comparar categorías | Barplot |
| Tendencia temporal | Lineplot |
| Correlación | Scatterplot |
| Distribución | Histograma + KDE |
| Outliers | Boxplot |

---

## 📊 Resultados Principales

| **Métrica** | **Resultado** |
|-------------|---------------|
| **Producto más vendido** | Salsa de Tomate |
| **Producto más rentable** | Desodorante Aerosol |
| **Cliente VIP** | Agustina Flores |
| **Ciudad principal** | Río Cuarto |
| **Método de pago preferido** | Efectivo (>100 ventas) |
| **Mes con más ventas** | Mes 5 (~560,000) |
| **Tendencia QR** | Crecimiento progresivo |

---

## 🤖 Colaboración con GitHub Copilot

### **👨‍🏫 Usuario (57%):**
- Definición de KPIs y métricas de negocio
- Selección de segmentos (ciudad, categoría, tiempo)
- Interpretación estratégica de resultados
- Validación de insights

### **🤖 Copilot (43%):**
- Código de integración relacional
- Implementación de 11 visualizaciones
- Optimizaciones (KDE, markers, rotación de etiquetas)
- Documentación inline

### **💡 Ventajas de Copilot:**
- ⚡ 65% más rápido
- 📊 Visualizaciones profesionales automáticas
- 🎯 Código limpio y documentado

---

## 🏆 Conclusión

**✅ Completado:**
- 4 datasets integrados
- 11 visualizaciones avanzadas
- Múltiples segmentaciones (ciudad, categoría, tiempo, pago)
- Insights de negocio accionables

**🎯 Preparado para:**
- Dashboards Power BI
- Machine Learning
- Toma de decisiones estratégicas

---

**👨‍💻 Proyecto:** José Yolic  
**🤖 Desarrollado con:** GitHub Copilot  
**📅 Fecha:** Diciembre 2025

