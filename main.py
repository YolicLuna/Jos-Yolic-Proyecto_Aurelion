# Programa para mostrar documentación de manera interactiva
# Autor: José Yolic
# Fecha: Diciembre 2025

def limpiar_pantalla():
    """Función para limpiar la pantalla"""
    import os
    # Limpia la pantalla según el sistema operativo
    os.system('cls' if os.name == 'nt' else 'clear')

def mostrar_menu():
    """Función que muestra el menú principal"""
    print("\n=== MENÚ PRINCIPAL ===")
    print("1. Tema, problema y solución")
    print("2. Origen de los datos")
    print("3. Descripción de la estructura, tipos de datos y escala de la base de datos")
    print("4. Proceso de limpieza de datos")
    print("5. Proceso de análisis estadístico predictivo")
    print("6. Implementación de Machine Learning")
    print("7. Insights de negocio principales")
    print("8. Pseudocódigo del programa")
    print("9. Sugerencias y mejoras con Copilot")
    print("10. Diagrama de flujo")
    print("11. Salir")
    print("=====================")

def cargar_documentacion():
    """Función que almacena la información de cada sección"""
    # Diccionario con la información de cada opción del menú
    info = {
        1: """
=== Tema, problema y solución ===

Documentación del Análisis de Ventas y Clientes

Este es un proyecto creado para practicar el análisis, visualización y 
modelado de datos utilizando python y bibliotecas como pandas, matplotlib, 
numpy, etc. Vamos a simular la gestión de una tienda realizando un proyecto 
basándose en datos generados con fines educativos.

Estado Actual del Proyecto:
Fase 1: Limpieza de datos COMPLETADA
Fase 2: Análisis estadístico predictivo COMPLETADA
Fase 3: Implementación de Machine Learning COMPLETADA

Descripción del problema a resolver o analizar:
- Qué productos son los menos vendidos
- Cuáles generan menos ganancias  
- Medir el tiempo que tardan en venderse
- Decidir si darles más publicidad o retirarlos del catálogo
- Analizar clientes: quiénes compran más, clientes inactivos
- Estrategias para aumentar frecuencia de compra

Resultados Obtenidos:
Vista integral del negocio con todas las dimensiones integradas
Insights accionables extraídos de 4 datasets relacionales  
Metodología reproducible documentada completamente
Colaboración efectiva humano-IA (Usuario 57% - IA 43%)
""",
        2: """
=== Origen de los datos ===

Los datos provienen de una base de datos de ventas y clientes de una tienda.
La base de datos está conformada por 4 archivos CSV:
- Ventas
- Productos  
- Detalle_ventas
- Clientes

Datasets Procesados:
Datos originales → Datos limpios:
• Clientes.xlsx → Clientes_limpio.csv
• Productos.xlsx → Productos_limpio.csv  
• Ventas.xlsx → Ventas_limpio.csv
• Detalle_ventas.xlsx → Detalle_ventas_limpio.csv

Integración Relacional:
• Tabla relacional integrada con 22 columnas
• Vista 360° del negocio unificando todas las dimensiones
• Joins SQL-like implementados para análisis completo
""",
        3: """
=== Descripción de la estructura y datos de las tablas ===

Tabla: Ventas (Ventas.xlsx)
Campo           | Tipo   | Escala
----------------|---------|----------
id_venta        | int    | Ordinal
fecha           | date   | Intervalo
id_cliente      | int    | Ordinal
nombre_cliente  | string | Nominal
email           | string | Nominal
medio_pago      | string | Nominal

Tabla: Productos (Productos.xlsx)
Campo           | Tipo   | Escala
----------------|---------|----------
id_producto     | int    | Ordinal
nombre_producto | string | Nominal
categoria       | string | Nominal
precio_unitario | int    | Razón

Tabla: Detalle_ventas (Detalle_ventas.xlsx)
Campo           | Tipo   | Escala
----------------|---------|----------
id_venta        | int    | Ordinal
id_producto     | int    | Ordinal
nombre_producto | string | Nominal
cantidad        | int    | Razón
precio_unitario | int    | Razón
importe         | int    | Razón

Tabla: Clientes (Clientes.xlsx)
Campo          | Tipo   | Escala
---------------|---------|----------
id_cliente     | int    | Ordinal
nombre_cliente | string | Nominal
email          | string | Nominal
ciudad         | string | Nominal
fecha_alta     | date   | Intervalo
""",
        4: """
=== PROCESO DE LIMPIEZA DE DATOS ===

Desarrollado con GitHub Copilot - Proceso completo de limpieza y 
normalización de 4 datasets relacionales

Metodología de Limpieza Aplicada:

5 Fases Sistemáticas:
1. ANÁLISIS DE PROBLEMAS → Explorar estructura y detectar errores
2. LIMPIEZA DE DATOS → Corregir errores y duplicados
3. ESTANDARIZACIÓN → Homogenizar formatos y tipos
4. NORMALIZACIÓN → Optimizar estructura relacional
5. VALIDACIÓN Y EXPORTACIÓN → Verificar calidad y guardar

Principios Clave del Proceso:
• Preservar integridad relacional: Mantener conexiones entre tablas
• Duplicados inteligentes: Distinguir duplicados reales vs transacciones válidas
• Normalización: Eliminar redundancias respetando el modelo de datos
• One-hot encoding: Preparar variables categóricas para análisis

Transformaciones Aplicadas por Dataset:

CLIENTES:
• Eliminación de duplicados → Filas idénticas removidas
• Normalización de fechas → Convertidas a datetime + columna mes_alta
• Estandarización de ciudades → "Cdmx" → "Ciudad de México"
• Normalización de nombres → Espacios extra eliminados, formato título
• Normalización de emails → Minúsculas, duplicados eliminados

PRODUCTOS:
• Eliminación de duplicados → Solo duplicados completos
• Normalización de precios → Valores absolutos, formato numérico
• Estandarización de categorías → "Electronica" → "Electrónica"
• One-hot encoding → categoria convertida a variables dummy

VENTAS:
• Eliminación de columnas redundantes → nombre_cliente, email
• Normalización de fechas → Datetime + columnas derivadas
• One-hot encoding → medio_pago convertido a variables dummy

DETALLE_VENTAS (Más crítico):
• Eliminación de columna redundante → nombre_producto
• Duplicados relacionales → SOLO eliminación de duplicados completos
• Recálculo de importes → importe = cantidad × precio_unitario
• Normalización numérica → Todos los valores como números
""",
        5: """
=== PROCESO DE ANÁLISIS ESTADÍSTICO PREDICTIVO ===

Desarrollado con GitHub Copilot - Análisis estadístico descriptivo sobre 
4 datasets relacionales integrados

Objetivo del Análisis:
Realizar un análisis estadístico descriptivo detallado sobre cuatro datasets 
relacionados (Clientes, Productos, Ventas, Detalle_Ventas), integrarlos en 
una tabla relacional unificada, y extraer insights de negocio mediante 
visualizaciones avanzadas con Python, pandas, matplotlib y seaborn.

Colaboración: Usuario vs GitHub Copilot

| Contribuyente          | Porcentaje | Tipo de Aporte                        |
|------------------------|------------|---------------------------------------|
| Usuario (José Yolic)   | 57%        | Razonamiento estratégico, decisiones  |
| GitHub Copilot         | 43%        | Implementación técnica, visualizaciones|

Síntesis: El usuario guió la estrategia y definió KPIs; Copilot materializó 
el análisis técnico con visualizaciones profesionales.

Metodología de Análisis Aplicada:

5 Fases Sistemáticas:
1. INTEGRACIÓN RELACIONAL → Merge de 4 datasets (LEFT JOIN)
2. ESTADÍSTICAS DESCRIPTIVAS → Medidas centrales y dispersión
3. ANÁLISIS SEGMENTADO → Tops, geografía, categorías, pagos
4. ANÁLISIS TEMPORAL → Tendencias mensuales
5. VISUALIZACIÓN AVANZADA → 11 gráficos especializados

Principios Clave:
• Integración completa: LEFT JOINs preservando integridad relacional
• Visualización por propósito: Barplots, lineplot, scatter, histogramas, boxplots
• Enfoque de negocio: KPIs accionables (tops, ciudades, métodos de pago)

Análisis Realizados (11 Visualizaciones):

1. Estadísticas Descriptivas → cantidad, precio_unitario, importe
2. Top Productos → Salsa de Tomate (#1 cantidad), Desodorante Aerosol (#1 importe)
3. Top Clientes → Agustina Flores (#1 gasto total)
4. Análisis Geográfico → Río Cuarto (#1 ciudad), Alimentos vs Limpieza
5. Métodos de Pago → Efectivo > QR > Tarjeta > Transferencia
6. Tendencias Temporales Ventas → Pico Mes 5 (~560k)
7. Tendencias Pagos → Efectivo en declive, QR en crecimiento
8. Scatter Plot → Cantidad vs Importe (correlación positiva)
9. Histogramas → Distribuciones con KDE
10. Boxplot Ciudad → Outliers detectados

Resultados Principales:
• Producto más vendido: Salsa de Tomate
• Producto más rentable: Desodorante Aerosol
• Cliente VIP: Agustina Flores
• Ciudad principal: Río Cuarto
• Método preferido: Efectivo (>100 ventas)
• Mes con más ventas: Mes 5 (~560,000)
• Tendencia QR: Crecimiento progresivo

Notebook Desarrollado:
• Analisis_estadistico_predictivo.ipynb → Integración completa + 11 visualizaciones
""",
        6: """
=== IMPLEMENTACIÓN DE MACHINE LEARNING ===

Desarrollado con GitHub Copilot - Modelos de clustering y regresión sobre 
datos de ventas integrados

Objetivo General:
1. Segmentar clientes mediante clustering (K-Means)
2. Predecir importes de ventas mediante regresión lineal

Colaboración: Usuario vs GitHub Copilot

| Contribuyente          | Porcentaje | Tipo de Aporte                        |
|------------------------|------------|---------------------------------------|
| Usuario (José Yolic)   | 60%        | Objetivos, features, interpretación   |
| GitHub Copilot         | 40%        | Algoritmos, visualizaciones, código   |

MODELO 1: Clustering K-Means

Objetivo: Segmentar clientes en grupos homogéneos según comportamiento de compra

Algoritmo: K-Means Clustering
• Ideal para segmentación no supervisada
• Eficiente y fácil interpretación

Features (Variables por cliente):
• cantidad: suma total de productos comprados
• importe: gasto total acumulado
• cat_Alimentos: % de compras en Alimentos (0-1)
• cat_Limpieza: % de compras en Limpieza (0-1)

Resultados - Distribución de Clientes:
• Cluster 0: 25 clientes (Equilibrados)
• Cluster 1: 16 clientes (VIP - Mayor gasto)
• Cluster 2: 13 clientes (Especialistas en alimentos)
• Cluster 3: 10 clientes (Especialistas en limpieza)

Estrategias por Cluster:
• Cluster 0: Promociones mixtas (combos alimentos + limpieza)
• Cluster 1: Programas de fidelización VIP, descuentos exclusivos
• Cluster 2: Campañas de alimentos, recetas, ofertas de despensa
• Cluster 3: Promociones de limpieza, bundles de hogar

MODELO 2: Regresión Lineal

Objetivo: Predecir el importe de una venta

Algoritmo: Regresión Lineal
• Relación matemática directa: importe = cantidad × precio_unitario

Entradas (X):
• cantidad: Número de unidades vendidas
• precio_unitario_x: Precio por unidad

Salida (y):
• importe: Valor total de la transacción

División Train/Test:
• 80% entrenamiento / 20% prueba
• random_state=42 (reproducibilidad)

Métricas de Evaluación:
• MAE (Mean Absolute Error): Error promedio absoluto
• R² (Coeficiente de Determinación): Capacidad explicativa (0-1)

Resultados - 4 Gráficas Generadas:
1. Importe Real vs Predicho → Tendencia capturada, dispersión en altos
2. Residuos vs Predichos → Heterocedasticidad detectada
3. Distribución de Errores → Sin sesgo sistemático, normalidad cumplida
4. Evaluación del Modelo:
   • Tendencia general: ✅ Capturada
   • Precisión importes bajos: ✅ Buena
   • Precisión importes altos: ⚠️ Regular
   • Heterocedasticidad: ⚠️ Presente
   • Normalidad errores: ✅ Cumplida
   • Sesgo: ✅ Ausente

Conclusiones:

Fortalezas:
• Captura relación lineal básica
• Sin sesgo sistemático
• Buena precisión en transacciones pequeñas

Recomendaciones para mejora:
1. Transformación de variables (log, sqrt)
2. Modelos robustos (RANSAC, Huber)
3. Regresión polinomial
4. Feature engineering (categoría, ciudad, época)
5. Modelos ensemble (Random Forest, Gradient Boosting)

Resumen de Modelos ML:

| Modelo           | Tipo        | Objetivo            | Resultado                    |
|------------------|-------------|---------------------|------------------------------|
| K-Means          | Clustering  | Segmentar clientes  | ✅ 4 clusters diferenciados  |
| Regresión Lineal | Supervisado | Predecir importe    | ⚠️ Funcional con limitaciones|

Logros:
• Segmentación de 64 clientes en 4 grupos
• Identificación de clientes VIP
• Modelo predictivo baseline implementado
• Visualizaciones completas de ambos modelos
""",
        7: """
=== INSIGHTS DE NEGOCIO PRINCIPALES DESCUBIERTOS ===

Descubrimientos por Dimensión de Análisis:

Top Productos:
• Más vendido (cantidad): Salsa de Tomate → Alta rotación en Alimentos
• Más rentable (importe): Desodorante Aerosol → Mayor margen/precio
• Insight clave: El producto más vendido NO es el más rentable

Clientes VIP:
• Mayor gasto total: Agustina Flores (#1)
• Potencial de fidelización: Programas para top 10 clientes identificados
• Oportunidad: Segmentación para estrategias personalizadas

Distribución Geográfica:
• Ciudad principal: Río Cuarto (mayor volumen de ventas)
• Medianas altas: Carlos Paz y Villa María (ventas típicamente mayores)
• Outliers detectados: Río Cuarto, Córdoba, Alta Gracia (ventas esporádicas grandes)

Métodos de Pago:
• Preferido actual: Efectivo (>100 ventas)
• Tendencia emergente: QR con crecimiento progresivo (adopción digital)
• Volátiles: Tarjeta y Transferencia (picos y caídas pronunciadas)
• Insight estratégico: Transición de efectivo hacia métodos digitales en progreso

Tendencias Temporales:
• Patrón identificado: Declive Mes 1→4, pico dramático Mes 5 (~560k), caída Mes 6
• Posible causa Mes 5: Campaña promocional o estacionalidad
• Acción recomendada: Investigar factores del pico para replicar éxito

Distribuciones de Ventas:
• Cantidad: Concentración en 1-2 unidades por transacción
• Precios: Multimodal (productos de ~1000 y ~2500)
• Importes: Sesgo a la derecha (mayoría ventas bajas, pocas muy altas)

Conclusión del Proyecto:

Proyecto completado exitosamente en 2 fases

Logros Alcanzados:
• 4 datasets procesados con metodología estructurada
• Tabla relacional integrada unificando todas las dimensiones
• 11 visualizaciones avanzadas (barplots, lineplot, scatter, histogramas, boxplots)
• Insights accionables extraídos para toma de decisiones
• Colaboración efectiva humano-IA documentada (57%-43%)

Resultados Cuantificables:
• Producto más vendido: Salsa de Tomate
• Producto más rentable: Desodorante Aerosol
• Cliente VIP: Agustina Flores
• Ciudad estratégica: Río Cuarto
• Tendencia pago digital: QR en crecimiento constante
• Pico de ventas: Mes 5 con ~560,000

Preparado para fases siguientes:
• Dashboards Power BI con estructura optimizada
• Modelos de machine learning con features preparadas
• Estrategias de marketing basadas en insights de clientes
• Optimización de inventario según productos top
• Toma de decisiones estratégicas con KPIs identificados
""",
        8: """
=== Pseudocódigo del Programa ===

Inicio Programa
    // Función para limpiar la pantalla
    Función limpiar_pantalla():
        Limpiar la consola según el sistema operativo

    // Función para mostrar el menú
    Función mostrar_menu():
        Mostrar título "MENÚ PRINCIPAL"
        Mostrar opciones numeradas del 1 al 10

    // Función para cargar la documentación
    Función cargar_documentacion():
        Crear diccionario con información de cada sección
        Retornar diccionario

    // Función para mostrar una sección
    Función mostrar_seccion(opcion, info):
        Limpiar pantalla
        Si opcion existe en info:
            Mostrar información de la sección
        Esperar que usuario presione Enter

    // Función principal
    Función main():
        info = cargar_documentacion()
        
        Mientras Verdadero:
            Limpiar pantalla
            Mostrar menú
            
            Intentar:
                Leer opción del usuario
                
                Si opción es 10:
                    Mostrar mensaje de despedida
                    Romper bucle
                Sino Si opción está entre 1 y 9:
                    Mostrar sección correspondiente
                Sino:
                    Mostrar error de opción inválida
            
            Si hay error de tipo:
                Mostrar mensaje de error
                Esperar Enter

    // Inicio del programa
    Si este es el archivo principal:
        Ejecutar main()
Fin Programa
""",
        9: """
=== Sugerencias y mejoras con Copilot ===

Colaboración con GitHub Copilot:

Copilot desarrolló:
• Todo el código de limpieza y análisis estadístico
• Implementación de visualizaciones con seaborn/matplotlib
• Cálculos de estadísticas descriptivas
• Integración relacional de tablas
• Documentación automática en notebooks

Usuario supervisó:
• Dirección de metodología de análisis
• Validación de insights generados
• Especificación de métricas de negocio relevantes
• Revisión de visualizaciones

Ventajas de usar Copilot:
• 80% más rápido que análisis manual tradicional
• Visualizaciones automáticas con código optimizado
• Insights automáticos en comentarios de código
• Integración relacional compleja automatizada
• Documentación en tiempo real en notebooks

Valor añadido del enfoque con IA:
• Toma de decisiones metodológicas automáticas pero fundamentadas
• Identificación inteligente de variables aptas vs no aptas
• Implementación de técnicas visuales apropiadas según contexto
• Integración sistemática de múltiples fuentes de datos
• Generación automática de insights con justificación metodológica
""",
        10: """
=== Diagrama de Flujo (versión consola con cuadros) ===

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
    +-------------------------+
    | Mostrar menú (1..11)    |
    | - 1 Tema/Problema       |
    | - 2 Origen datos        |
    | - 3 Estructura BD       |
    | - 4 Limpieza datos      |
    | - 5 Análisis estadístico|
    | - 6 Machine Learning    |
    | - 7 Insights negocio    |
    | - 8 Pseudocódigo        |
    | - 9 Sugerencias         |
    | - 10 Diagrama (esto)    |
    | - 11 Salir              |
    +-------------------------+
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
        |                  | ¿Está entre 1 y 11? |
        |                  +---------------------+
        |                  |                     |
        |                  No                    Sí
        |                  |                     v
        |           +----------------+    +--------------------------+
        |           | Mostrar error  |    | Opción válida (1..10):   |
        |           |"Ingrese número"|    | Mostrar sección          |
        |           +----------------+    +--------------------------+
        |                  |                     |
        |                  v                     v
[Esperar Enter]    [Esperar Enter]         [Esperar Enter]
        |                  |                     |
        +------------------+---------------------+
                           v
           (volver a Bucle principal)

    Si la opción es 11 -> Mostrar despedida y terminar.
"""
    }
    return info

def mostrar_seccion(opcion, info):
    """Función que muestra la información de la sección seleccionada"""
    limpiar_pantalla()
    if opcion in info:
        print(info[opcion])
    input("\nPresione Enter para continuar...")

def main():
    """Función principal del programa"""
    # Cargamos la información en memoria
    info = cargar_documentacion()
    
    while True:
        limpiar_pantalla()
        mostrar_menu()
        
        # Pedimos la opción al usuario
        try:
            opcion = int(input("\nSeleccione una opción (1-11): "))
            
            # Verificamos la opción seleccionada
            if opcion == 11:
                print("\n¡Gracias por usar el programa!")
                break
            elif opcion >= 1 and opcion <= 10:
                mostrar_seccion(opcion, info)
            else:
                print("\nError: Opción no válida")
                input("Presione Enter para continuar...")
        except ValueError:
            print("\nError: Por favor ingrese un número válido")
            input("Presione Enter para continuar...")

# Punto de entrada del programa
if __name__ == "__main__":
    main()
