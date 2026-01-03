# 🤖 IMPLEMENTACIÓN DE MACHINE LEARNING

> **Desarrollado con GitHub Copilot** - Modelos de clustering y regresión sobre datos de ventas integrados

## 🎯 Objetivo General

Aplicar técnicas de Machine Learning sobre los datos de ventas para:
1. **Segmentar clientes** mediante clustering (K-Means)
2. **Predecir importes** de ventas mediante regresión lineal

---

## 🤝 Colaboración: Usuario vs GitHub Copilot

| **Contribuyente** | **Porcentaje** | **Tipo de Aporte** |
|-------------------|----------------|---------------------|
| **👨‍🏫 Usuario (José Yolic)** | **60%** | Definición de objetivos, selección de features, interpretación de resultados |
| **🤖 GitHub Copilot** | **40%** | Implementación de algoritmos, visualizaciones, optimización de código |

**🏆 Síntesis:** El usuario definió la estrategia de ML y las variables relevantes; Copilot implementó los algoritmos con código optimizado.

---

## 📊 MODELO 1: CLUSTERING K-MEANS

### **🎯 Objetivo**
**Segmentar clientes** en grupos homogéneos según su comportamiento de compra para diseñar estrategias personalizadas.

### **🔧 Algoritmo Elegido**
**K-Means Clustering**

**Justificación:**
- Algoritmo no supervisado ideal para segmentación
- Agrupa clientes por similitud en comportamiento de compra
- Eficiente computacionalmente para datasets pequeños-medianos
- Fácil interpretación de clusters para negocio

### **📥 Datos de Entrada (Features)**
```python
# Variables seleccionadas por cliente:
- cantidad: suma total de productos comprados
- importe: gasto total acumulado
- cat_Alimentos: % de compras en categoría Alimentos (0-1) ⚠️ POST-RECLASIFICACIÓN
- cat_Limpieza: % de compras en categoría Limpieza (0-1) ⚠️ POST-RECLASIFICACIÓN

# Métricas derivadas:
- total_compras: número de transacciones
- gasto_promedio: importe / total_compras

# ⚠️ IMPORTANTE:
# Estos datos incluyen la reclasificación de 48 productos:
# - 7 productos de Limpieza (erróneamente etiquetados como Alimentos) → Limpieza
# - 41 productos de Alimentos (erróneamente etiquetados como Limpieza) → Alimentos
# Por lo tanto, las proporciones cat_Alimentos y cat_Limpieza por cliente 
# reflejan la categorización CORRECTA, no la original con errores.
```

### **⚙️ Preprocesamiento**
```python
# 1. Agregación por cliente
df_clientes = df.groupby("nombre_cliente").agg({
    "cantidad": "sum",
    "importe": "sum",
    "cat_Alimentos": "mean",
    "cat_Limpieza": "mean"
})

# 2. Escalado de variables (StandardScaler)
scaler = StandardScaler()
df_scaled = scaler.fit_transform(df_model)
```

### **⚠️ IMPACTO DE RECLASIFICACIÓN EN K-MEANS**

**Cambios en los datos de entrada:**
```
De 48 productos mal categorizados antes de clustering:
├─ 7 productos de Limpieza → reclasificados correctamente a Limpieza
└─ 41 productos de Alimentos → reclasificados correctamente a Alimentos

Efecto en las variables de entrada:
├─ cat_Alimentos (media por cliente): AUMENTÓ significativamente
├─ cat_Limpieza (media por cliente): DISMINUYÓ significativamente
└─ cantidad e importe: SIN CAMBIOS (dependen de id_venta, no de categorización)
```

**Impacto en los clusters:**
- ✅ Cantidad de clientes por cluster: **PODRÍA CAMBIAR** (reagrupación)
- ⚠️ Perfiles de categoría (% Alimentos vs % Limpieza): **DEFINITIVAMENTE CAMBIÓ**
- ✅ Cantidad e importe promedio: **SIN CAMBIOS** (invariables)
- ⚠️ Interpretación de especialización: **ACTUALIZADA**

**Acción realizada:**
- Los datos del clustering fueron regenerados automáticamente con `Productos_limpio.csv`
- Las proporciones cat_Alimentos y cat_Limpieza reflejan la **categorización correcta**
- Los resultados mostrados incluyen estos cambios

### **🔢 Configuración del Modelo**
```python
kmeans = KMeans(n_clusters=4, random_state=42)
df_clientes["cluster"] = kmeans.fit_predict(df_scaled)
```

**Parámetros:**
- **n_clusters = 4**: Número de segmentos de clientes
- **random_state = 42**: Reproducibilidad de resultados

### **📊 Visualización con PCA**
```python
# Reducción a 2 dimensiones para visualización
pca = PCA(n_components=2)
pca_result = pca.fit_transform(df_scaled)
```

### **📈 Resultados del Clustering**

#### **⚠️ NOTA IMPORTANTE**
*Los resultados a continuación incluyen la reclasificación correcta de 48 productos. Las proporciones de Alimentos vs Limpieza reflejan la categorización actual (post-limpieza), no los datos originales con errores.*

#### **Distribución de Clientes por Cluster**

| Cluster | Cantidad de Clientes |
|---------|---------------------|
| **0**   | 25                  |
| **1**   | 16                  |
| **2**   | 13                  |
| **3**   | 10                  |

#### **Perfil de Cada Cluster**

**⚠️ Interpretación actualizada (post-reclasificación):**
- Los porcentajes de Alimentos y Limpieza representan la **distribución correcta** de productos
- 48 productos fueron reclasificados para reflejar sus categorías reales
- Las proporciones pueden haber cambiado significativamente respecto a datos con errores

| Cluster | Cantidad Promedio | Importe Promedio | % Alimentos | % Limpieza | **Interpretación** |
|---------|-------------------|------------------|-------------|------------|--------------------|
| **0**   | 10.88             | 26,465           | 49%         | 51%        | **Clientes equilibrados** - Compran ambas categorías |
| **1**   | 27.94             | 77,361           | 42%         | 58%        | **Clientes VIP** - Mayor gasto, prefieren limpieza |
| **2**   | 13.31             | 33,626           | 84%         | 16%        | **Especialistas en alimentos** |
| **3**   | 12.40             | 30,143           | 13%         | 87%        | **Especialistas en limpieza** |

#### **Visualización: Clusters en Espacio PCA**
- Gráfico de dispersión con 4 colores
- Ejes PCA1 y PCA2 (componentes principales)
- Separación clara entre grupos

### **💡 Insights de Negocio**

| Cluster | Estrategia Recomendada |
|---------|------------------------|
| **Cluster 0** | Promociones mixtas (combos alimentos + limpieza) |
| **Cluster 1** | Programas de fidelización VIP, descuentos exclusivos |
| **Cluster 2** | Campañas de alimentos, recetas, ofertas de despensa |
| **Cluster 3** | Promociones de limpieza, bundles de hogar |

---

## 📈 MODELO 2: REGRESIÓN LINEAL

### **🎯 Objetivo**
**Predecir el importe** de una venta basándose en la cantidad de productos y el precio unitario.

### **🔧 Algoritmo Elegido**
**Regresión Lineal (Linear Regression)**

**Justificación:**
- Relación matemática directa: `importe = cantidad × precio_unitario`
- Modelo interpretable y explicable para negocio
- Baseline simple para comparar con modelos más complejos
- Eficiente computacionalmente

### **📥 Entradas y Salida**

**Variables Predictoras (X):**
```python
X = df[['cantidad', 'precio_unitario_x']]
```
- `cantidad`: Número de unidades vendidas
- `precio_unitario_x`: Precio por unidad del producto

**Variable Objetivo (y):**
```python
y = df['importe']
```
- `importe`: Valor total de la transacción (lo que queremos predecir)

### **⚙️ Preprocesamiento**
```python
# Rellenar valores nulos con la mediana
df['importe'] = df['importe'].fillna(df['importe'].median())
df['precio_unitario_x'] = df['precio_unitario_x'].fillna(df['precio_unitario_x'].median())
df['cantidad'] = df['cantidad'].fillna(df['cantidad'].median())
```

### **🔢 División Train/Test y Entrenamiento**
```python
# División 80% entrenamiento, 20% prueba
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Entrenamiento del modelo
modelo_lr = LinearRegression()
modelo_lr.fit(X_train, y_train)

# Predicciones
y_pred = modelo_lr.predict(X_test)
```

### **📊 Métricas de Evaluación**

```python
MAE (Mean Absolute Error): Error promedio absoluto
R² (Coeficiente de Determinación): Capacidad explicativa del modelo (0-1)
```

**Resultados obtenidos:**
- **MAE**: Indica el error promedio en pesos entre predicción y valor real
- **R²**: Porcentaje de variabilidad explicada por el modelo

### **📈 Visualizaciones de Resultados**

#### **1. 🟠 Gráfica: Importe Real vs Importe Predicho**
```python
sns.scatterplot(x=y_test, y=y_pred)
plt.plot([min_val, max_val], [min_val, max_val], 'r--')  # Línea ideal
```

**Interpretación:**
- **Puntos cerca de la línea roja** → Predicciones acertadas
- **Dispersión vertical** → Variabilidad en las predicciones
- **Tendencia ascendente** → Modelo captura la relación general

**Hallazgos:**
- El modelo captura la tendencia general correctamente
- Mayor dispersión en importes altos
- Algunas predicciones se desvían significativamente

#### **2. 🟣 Gráfica: Residuos vs Valores Predichos**
```python
residuos = y_test - y_pred
sns.scatterplot(x=y_pred, y=residuos)
plt.axhline(0, color='red', linestyle='--')
```

**Interpretación:**
- **Patrón de abanico** → Heterocedasticidad detectada
- **Errores pequeños** en importes bajos
- **Errores grandes** en importes altos
- **Valores atípicos** identificados

**Hallazgos:**
- El modelo es **menos confiable en importes grandes**
- Presencia de heterocedasticidad (varianza no constante)
- Sugiere que una regresión lineal simple puede no ser óptima

#### **3. 🟢 Gráfica: Distribución de Errores (Histograma)**
```python
sns.histplot(residuos, kde=True)
plt.axvline(0, color='red', linestyle='--')
```

**Interpretación:**
- **Distribución centrada en cero** → Modelo sin sesgo sistemático
- **Forma de campana** → Cumple parcialmente supuesto de normalidad
- **Simetría** → No predice consistentemente alto o bajo

**Hallazgos:**
- El modelo **no tiene sesgo fuerte**
- Errores distribuidos normalmente (buena señal)
- Cumple supuesto de normalidad de residuos

### **📊 Evaluación del Modelo**

| **Aspecto** | **Resultado** | **Interpretación** |
|-------------|---------------|--------------------|
| **Tendencia general** | ✅ Capturada | El modelo entiende la relación cantidad-precio-importe |
| **Precisión en importes bajos** | ✅ Buena | Errores pequeños y consistentes |
| **Precisión en importes altos** | ⚠️ Regular | Mayor dispersión y errores |
| **Heterocedasticidad** | ⚠️ Presente | Varianza no constante en residuos |
| **Normalidad de errores** | ✅ Cumplida | Distribución simétrica centrada en 0 |
| **Sesgo** | ✅ Ausente | No predice sistemáticamente alto/bajo |

### **💡 Conclusiones del Modelo de Regresión**

**Fortalezas:**
- ✅ Captura la relación lineal básica entre variables
- ✅ Sin sesgo sistemático en predicciones
- ✅ Errores distribuidos normalmente
- ✅ Buena precisión en transacciones de bajo importe

**Debilidades:**
- ⚠️ Heterocedasticidad detectada
- ⚠️ Menor confiabilidad en importes altos
- ⚠️ Presencia de outliers no manejados

**Recomendaciones para mejora:**
1. **Transformación de variables** (log, sqrt) para estabilizar varianza
2. **Modelos robustos** (RANSAC, Huber) para manejar outliers
3. **Regresión polinomial** para capturar relaciones no lineales
4. **Feature engineering** (categoría producto, ciudad, época del año)
5. **Modelos ensemble** (Random Forest, Gradient Boosting) para mayor precisión

---

## 🏆 Resumen General

### **Modelos Implementados**

| **Modelo** | **Tipo** | **Objetivo** | **Resultado** | **Post-Reclasificación** |
|------------|----------|--------------|---------------|-------------------------|
| **K-Means** | Clustering | Segmentar clientes | ✅ 4 clusters bien diferenciados | ⚠️ Datos categorizados correctamente |
| **Regresión Lineal** | Supervisado | Predecir importe | ⚠️ Funcional con limitaciones | ✅ Invariable (sin cambios) |

### **Logros Alcanzados**
- ✅ Segmentación exitosa de ~64 clientes en 4 grupos (con datos post-reclasificación)
- ✅ Identificación de clientes VIP (Cluster 1) basada en categorías correctas
- ✅ Modelo predictivo baseline implementado (invariable a reclasificación)
- ✅ Visualizaciones completas de ambos modelos
- ✅ Métricas de evaluación calculadas

### **Consideraciones por Reclasificación de Productos**

**En K-Means:**
- ⚠️ Los perfiles de especialización (% Alimentos vs % Limpieza) **fueron actualizados**
- ⚠️ La composición de clusters **podría haber cambiado**
- ✅ La metodología y número de clusters **se mantiene válida**
- ✅ Las estrategias de negocio **siguen siendo aplicables**

**En Regresión Lineal:**
- ✅ **SIN CAMBIOS** - El modelo predice importes basándose en cantidad y precio unitario
- ✅ Variables predictoras (cantidad, precio) no fueron afectadas

### **Preparado para:**
- 📊 Estrategias de marketing personalizadas por cluster (basadas en categorización correcta)
- 🎯 Optimización de modelos predictivos
- 🔄 Implementación de modelos más avanzados
- 💼 Toma de decisiones basada en ML con datos íntegros

---

**👨‍💻 Proyecto:** José Yolic  
**🤖 Desarrollado con:** GitHub Copilot  
**📅 Fecha:** Diciembre 2025
