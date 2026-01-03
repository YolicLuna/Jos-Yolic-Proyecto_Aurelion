# 🗄️ IMPLEMENTACIÓN SQL - BASE DE DATOS AURELION

> **Desarrollado por José Yolic con asistencia de GitHub Copilot** - Base de datos relacional completa con MySQL para análisis de ventas integrados

## 🎯 Objetivo General

Implementar una **base de datos relacional completa en MySQL** que replique la estructura de datos del proyecto Aurelion, permitiendo:
1. **Crear la estructura relacional** con tablas, claves primarias y foráneas
2. **Cargar los datos limpios** desde archivos CSV exportados de la fase de limpieza
3. **Explorar y transformar datos** utilizando consultas SQL
4. **Realizar análisis estadístico descriptivo** mediante SQL puro
5. **Integrar datos multitabla** con JOINs complejos para análisis relacional

---

## 🤝 Colaboración: Usuario vs GitHub Copilot

| **Contribuyente** | **Porcentaje** | **Tipo de Aporte** |
|-------------------|----------------|---------------------|
| **👨‍💻 Usuario (José Yolic)** | **~92%** | Diseño de esquema, todas las consultas de exploración y análisis, transformaciones, documentación |
| **🤖 GitHub Copilot** | **~8%** | Optimización de JOINs complejos, consultas con alias, asistencia en recordatorios técnicos |

**🏆 Síntesis:** El usuario escribió prácticamente todo el código SQL; Copilot asistió únicamente en JOINs avanzados y optimización de sintaxis.

---

## 📊 ARQUITECTURA DE LA BASE DE DATOS

### **Modelo Entidad-Relación**
**Incluido:** `1_Modelo_relacion_entidad.jpg` - Diagrama visual del modelo

**Estructura de 4 tablas normalizadas 3NF:**
- `Clientes` (1) ←→ (N) `Ventas` ←→ (N) `Detalle_Ventas` ←→ (N) `Productos`
- Relaciones con integridad referencial mediante Foreign Keys
- 612 registros totales cargados

---

## 📁 ARCHIVOS DE IMPLEMENTACIÓN

### **1️⃣ 2_Creacion_base_de_datos.sql**

**Objetivo:** Crear la estructura completa de la base de datos y sus tablas

**Tablas creadas:**
- `Clientes` - Información de clientes (id, nombre, email, ciudad, fecha_alta)
- `Productos` - Catálogo de productos (id, nombre, categoría, precio)
- `Ventas` - Transacciones (id, fecha, cliente, método pago)
- `Detalle_Ventas` - Líneas de cada venta (venta, producto, cantidad, importe)

**Características implementadas:**
- ✅ Claves primarias en cada tabla
- ✅ Claves foráneas para integridad referencial
- ✅ Tipos de datos optimizados (INT, VARCHAR, DATE, DECIMAL)
- ✅ Restricciones NOT NULL en campos críticos
- ✅ Índices únicos en emails
- ✅ AUTO_INCREMENT para generación automática de IDs

**Validación:** Integridad referencial verificada post-creación

---

### **2️⃣ 3_Carga_de_datos.sql**

**Objetivo:** Importar datos desde archivos CSV limpios al servidor MySQL

**Método:** LOAD DATA INFILE con separador coma y encabezados ignorados

**Registros cargados:**
- Clientes: 100 registros
- Productos: 100 registros
- Ventas: 120 transacciones
- Detalle_Ventas: 492 líneas de detalle
- **Total: 612 registros**

**Consideraciones:**
- Archivos en formato CSV (pre-convertidos desde XLSX)
- Ubicación: `/var/lib/mysql-files/`
- Encabezados ignorados automáticamente
- Validación: Integridad referencial OK post-carga

---

### **3️⃣ 4_Exploracion_limpieza_transformacion.sql**

**Objetivo:** Explorar los datos cargados, identificar problemas y aplicar transformaciones

#### **Exploración de Clientes**
- Análisis de duplicados por email: Sin duplicados reales detectados
- Acción: Sin transformaciones necesarias

#### **Exploración y Transformación de Productos**

**Hallazgo crítico:** 48 productos mal categorizados

- **7 productos de Limpieza** etiquetados como Alimentos
  - Desodorante Aerosol, Cepillo de Dientes, Mascarilla Capilar, Limpiavidrios 500ml, Esponjas x3, Shampoo 400ml, Servilletas x100
  - **Acción:** Reclasificados a Limpieza

- **41 productos de Alimentos** etiquetados como Limpieza
  - Pepsi 1.5L, Jugo de Naranja, Leche Entera, Pan Lactal, Cerveza, Vino, etc.
  - **Acción:** Reclasificados a Alimentos

**Resultado post-transformación:**

- Alimentos: 84 productos (84%)
- Limpieza: 16 productos (16%)

#### **Columnas Derivadas Creadas**

- `Mes` en tabla Clientes (extrayendo nombre del mes de fecha_alta)
- **Propósito:** Facilitar análisis temporal

#### **Validación Final**

- Integridad referencial OK
- Sin registros huérfanos
- Transformaciones verificadas

---

### **4️⃣ 6_JOIN'S.sql**

**Objetivo:** Crear consultas que integren múltiples tablas para análisis relacional

**JOINs implementados:** 9 consultas de diferentes complejidades

| # | Tipo | Propósito | Resultado |
|---|------|----------|-----------|
| **1** | INNER | Ventas con Clientes | Cada venta enriquecida con datos del cliente |
| **2** | INNER | Detalle_Ventas con Productos | Líneas de venta con info de producto |
| **3** | INNER | Ventas con Detalle_Ventas | Transacciones con sus líneas de detalle |
| **4** | INNER Triple | Clientes + Ventas + Detalle + Productos | Relación Cliente → Venta → Producto |
| **5** | INNER Cuádruple | Todas las tablas | Reporte 360° de transacciones |
| **6** | LEFT | Clientes sin Ventas | Identifica clientes inactivos |
| **7** | LEFT | Productos no Vendidos | Identifica SKUs sin movimiento |
| **8** | INNER | Cliente, Ciudad, Método Pago | Gasto multidimensional por cliente |
| **9** | INNER | Productos por Categoría | Ranking de best-sellers por categoría |

**Impacto:** Proporciona múltiples perspectivas de análisis relacional

---

### **5️⃣ 5_Analisis_estadistico_descriptivo/ (Carpeta)**

**Objetivo:** Análisis estadístico detallado de cada tabla mediante SQL puro

**4 scripts incluidos:**

#### **1_Tabla_Clientes.sql**
**Análisis realizados:**
- Total de clientes: 100
- Distribución por ciudad (top: Rio Cuarto 23, Alta Gracia 21)
- Distribución por mes de registro (top: Enero y Marzo con 31 c/u)
- Análisis cruzado Mes + Ciudad
- Filtrado por rango de fechas

**Insights:** Rio Cuarto y Alta Gracia concentran 44% de clientes

#### **2_Tabla_Productos.sql**
**Análisis realizados:**
- Distribución por categoría: Alimentos 84%, Limpieza 16%
- Top 5 más caros y Top 5 más baratos
- Análisis de modalidad de precios
- Extremos por categoría (Top 3 / Bottom 3)
- Búsqueda por palabra clave

**Insights:** 
- Rango de precios: ~500 a ~4000
- Mayoría de precios únicos
- Catálogo orientado a alimentos

#### **3_Tabla_Ventas.sql**
**Análisis realizados:**
- Preferencia de método de pago
- Distribución mensual de ventas
- Clientes más y menos activos
- Análisis temporal por método de pago
- Filtrado por método específico

**Insights:**
- Efectivo preferido: 37 ventas (31%)
- QR: 30 ventas (25%)
- Cliente 56 más activo: 5 compras
- Enero y Mayo: mayor actividad

#### **4_Tabla_Detalle_Ventas.sql**
**Análisis realizados:**
- Total vendido: 1,016 unidades, $2,651,417
- Top 3 productos por cantidad
- Top 3 productos por importe
- Bottom 3 productos
- Estadísticas descriptivas (MIN, MAX, AVG, STDDEV)

**Insights:**
- Producto 43: más vendido (27 pz)
- Producto 91: mayor ingreso ($93,800)
- Dispersión significativa en importes
- Oportunidad análisis ABC (Pareto)

---

## 📊 IMPACTO DE LA RECLASIFICACIÓN DE PRODUCTOS

**Cambio crítico realizado en SQL:**
```
48 productos reclasificados en script 4_Exploracion_limpieza_transformacion.sql:
├─ 7 productos: Limpieza → correctamente clasificados (from Alimentos)
└─ 41 productos: Alimentos → correctamente clasificados (from Limpieza)

Resultado final:
├─ Alimentos: 84 productos (84%)
└─ Limpieza: 16 productos (16%)
```

**Impacto en análisis SQL:**
- ✅ Todos los análisis ejecutados con categorización correcta
- ✅ Consultas GROUP BY categoria reflejan distribución real
- ✅ Integridad de datos post-transformación verificada

---

## 🎯 DECISIONES DE DISEÑO

### **1. Modelo Relacional Normalizado**
- **3NF (Tercera Forma Normal):** Eliminación de redundancias
- **Integridad referencial:** Foreign Keys en todas las relaciones
- **Escalabilidad:** Estructura preparada para crecimiento

### **2. Estrategia de Exploración**
- **Nivel 1:** Exploración individual de cada tabla
- **Nivel 2:** JOINs para relaciones binarias
- **Nivel 3:** JOINs múltiples para análisis complejos
- **Nivel 4:** Agregaciones y estadísticas descriptivas

### **3. Transformaciones Inteligentes**
- Reclasificación de 48 productos con verificación post-transformación
- Creación de columnas derivadas para análisis temporal
- Preservación de integridad referencial en todas las operaciones

---

## 🏆 LOGROS ALCANZADOS

### **✅ Estructura Implementada**
- Base de datos relacional completa con 4 tablas
- 612 registros totales cargados exitosamente
- Integridad referencial garantizada
- Índices y restricciones establecidos

### **✅ Análisis Completado**
- 4 archivos de análisis estadístico por tabla
- 9 JOINs de diferentes complejidades documentados
- Transformaciones de datos ejecutadas y validadas
- Consultas reutilizables para reporting

### **✅ Calidad de Datos**
- 48 productos reclasificados correctamente
- Validación de Foreign Keys OK
- Sin duplicados críticos
- Estructura lista para análisis avanzado

---

## 📈 COMPARATIVA: PYTHON vs SQL

| **Aspecto** | **Python (Pandas)** | **SQL (MySQL)** |
|-------------|-------------------|-----------------|
| **Carga de datos** | read_csv() | LOAD DATA INFILE |
| **Transformaciones** | loc, update | UPDATE ... WHERE |
| **Análisis exploratorio** | describe(), groupby() | SELECT ... GROUP BY |
| **JOINs** | pd.merge() | INNER/LEFT JOIN |
| **Visualizaciones** | Integrado (matplotlib/seaborn) | Requiere herramienta externa |
| **Performance datos grandes** | Requiere RAM | Más eficiente |
| **Documentación** | # Comentarios | /* */ Comentarios |

**Conclusión:** SQL es más eficiente para consultas complejas y análisis; Python para visualización.

---

## 🎓 APRENDIZAJES TÉCNICOS

### **SQL Concepts Implementados**
- ✅ DDL: CREATE DATABASE, CREATE TABLE, ALTER TABLE
- ✅ DML: INSERT (via LOAD DATA), UPDATE, SELECT
- ✅ Joins: INNER, LEFT, múltiples tablas (hasta 4-way joins)
- ✅ Agregaciones: COUNT, SUM, AVG, GROUP BY, ORDER BY
- ✅ Subconsultas y filtrado avanzado (WHERE, BETWEEN, LIKE, IN)
- ✅ Funciones: MONTHNAME, DISTINCT, LIMIT, CASE

### **Buenas Prácticas Aplicadas**
- ✅ Nombres descriptivos para columnas y tablas
- ✅ Comentarios explicativos en cada sección
- ✅ Verificación de integridad post-operación
- ✅ Uso de alias para mejorar legibilidad
- ✅ Separación lógica en múltiples scripts

---

## 🚀 POSIBLES EXTENSIONES FUTURAS

1. **Vistas (Views)** - Crear vistas para reportes recurrentes
2. **Procedimientos Almacenados** - Automatizar transformaciones complejas
3. **Índices Avanzados** - Optimizar consultas frecuentes
4. **Triggers** - Mantener integridad con actualizaciones automáticas
5. **Data Warehouse** - Migrar a modelo OLAP
6. **Replicación** - Backup automático
7. **Integración BI** - Conexión directa desde Power BI/Tableau

---

## 📌 ESTRUCTURA DE CARPETAS

```
5_SQL_Aurelion/
├── 1_Modelo_relacion_entidad.jpg          (Diagrama ER)
├── 2_Creacion_base_de_datos.sql           (DDL - Estructura)
├── 3_Carga_de_datos.sql                   (DML - Importación)
├── 4_Exploracion_limpieza_transformacion.sql (Análisis + Transformaciones)
├── 6_JOIN'S.sql                           (Integraciones multitabla)
├── 5_Analisis_estadistico_descriptivo/    (Carpeta de análisis)
│   ├── 1_Tabla_Clientes.sql
│   ├── 2_Tabla_Productos.sql
│   ├── 3_Tabla_Ventas.sql
│   └── 4_Tabla_Detalle_Ventas.sql
└── Documentacion_MySQL_Aurelin.md         (Este archivo)
```

---

## 🎯 ESTADO DEL MÓDULO SQL

**✅ Completado:**
- Base de datos relacional implementada
- Datos cargados y validados
- Transformaciones aplicadas y verificadas
- Análisis multitabla completado
- 9 JOINs documentados
- 4 análisis estadísticos por tabla

**🔄 Integración con proyecto:**
- Réplica en SQL de procesos Python (Limpieza + Análisis)
- Extra académico para demostrar múltiples tecnologías
- Datos consistentes con fases anteriores

---

## 🏆 CONCLUSIÓN

Este módulo SQL demuestra la **implementación completa de una base de datos relacional**, desde diseño hasta análisis. La estructura normalizada, integridad referencial y transformaciones de datos garantizan un repositorio confiable para análisis de negocio.

**Validación:** Todos los datos cargados, transformaciones aplicadas y análisis completados exitosamente. Base de datos lista para integración con herramientas BI y análisis avanzados.

**Valor agregado:** Proporciona una alternativa SQL pura a los análisis realizados en Python, demostrando competencia en múltiples plataformas de análisis de datos.

---

**👨‍💻 Proyecto:** José Yolic  
**🤖 Asistencia:** GitHub Copilot (~8% - optimización de JOINs)  
**📅 Fecha:** Enero 2026  
**🔧 Tecnología:** MySQL 8.0+  
**📊 Registros:** 612 registros totales | 4 tablas | 3NF normalizado
