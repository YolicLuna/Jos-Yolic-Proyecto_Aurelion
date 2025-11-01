# Programa para mostrar documentación de manera interactiva
# Autor: José Yolic
# Fecha: Octubre 2025

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
    print("5. Proceso de análisis estadístico descriptivo")
    print("6. Insights de negocio principales")
    print("7. Pseudocódigo del programa")
    print("8. Sugerencias y mejoras con Copilot")
    print("9. Diagrama de flujo")
    print("10. Salir")
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
Fase 2: Análisis estadístico descriptivo COMPLETADA

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
=== PROCESO DE ANÁLISIS ESTADÍSTICO DESCRIPTIVO ===

Desarrollado con GitHub Copilot - Análisis estadístico descriptivo 
detallado sobre 4 datasets relacionales con integración completa

Objetivo del Análisis:
Realizar un análisis estadístico descriptivo detallado sobre los cuatro 
datasets relacionados, integrándolos en una tabla relacional para análisis 
combinados. Se exploró tendencias, patrones, distribución y relaciones entre 
variables usando Python con pandas, numpy, matplotlib y seaborn.

Colaboración Detallada: Usuario vs GitHub Copilot

Distribución Global de Aportes:
| Contribuyente          | Porcentaje | Tipo de Aporte                    |
|------------------------|------------|-----------------------------------|
| Usuario (José Yolic)   | 57%        | Razonamiento estratégico, decisiones |
| GitHub Copilot         | 43%        | Implementación técnica, código      |

Desglose Detallado por Fase:
• Análisis Clientes: Usuario 80% - IA 20%
• Análisis Productos: Usuario 70% - IA 30%  
• Análisis Ventas: Usuario 65% - IA 35%
• Análisis Detalle Ventas: Usuario 60% - IA 40%
• Integración Relacional: Usuario 30% - IA 70%
• Análisis Relacional: Usuario 55% - IA 45%

Metodología de Análisis Aplicada:

5 Fases Sistemáticas:
1. EXPLORACIÓN INICIAL → Inspección y carga de datasets limpios
2. ESTADÍSTICAS DESCRIPTIVAS → Medidas de tendencia central y dispersión
3. ANÁLISIS UNIVARIADO → Distribuciones y patrones individuales
4. ANÁLISIS RELACIONAL → Integración de tablas y análisis multivariado
5. INSIGHTS Y CONCLUSIONES → Extracción de patrones y tendencias

Integración Relacional Completa:

Proceso de Joins Implementado:
1. Clientes ⟵→ Ventas (mediante id_cliente)
2. Detalle_Ventas ⟵→ Ventas (mediante id_venta)  
3. Productos ⟵→ Detalle_Ventas (mediante id_producto)

Resultado: Tabla relacional con 22 columnas para análisis 360° del negocio

Notebooks de Análisis Desarrollados:
• Clientes_Analisis.ipynb → Análisis demográfico y temporal
• Productos_Analisis.ipynb → Análisis de precios y categorías  
• Ventas_Analisis.ipynb → Análisis de tendencias y métodos de pago
• Detalle_ventas_Analisis.ipynb → Análisis transaccional y correlaciones
• Analisis_Relacional.ipynb → Vista integrada 360° MÁS COMPLETO
""",
        6: """
=== INSIGHTS DE NEGOCIO PRINCIPALES DESCUBIERTOS ===

Descubrimientos por Dimensión de Análisis:

Insights de Clientes:
• Concentración geográfica → Identificación de mercados principales
• Patrones de alta → Estacionalidad en adquisición de clientes
• Base de clientes → Métricas de crecimiento y cobertura

Insights de Productos:
• Estructura de precios → Rangos y distribución del portfolio
• Balance categórico → Proporción Alimentos vs Limpieza
• Productos estrella → Identificación de extremos de precio

Insights de Ventas:
• Estacionalidad → Patrones temporales de demanda
• Preferencias de pago → Adopción de métodos digitales vs tradicionales
• Clientes VIP → Segmento de alta frecuencia de compra

Insights Relacionales (Vista 360°):
• Cross-insights → Relaciones entre geografía, productos y métodos pago
• Tendencias integradas → Evolución temporal de comportamientos
• Patrones de negocio → Insights que solo emergen con datos integrados

Conclusión del Proyecto:

Proyecto completado exitosamente en 2 fases:

Logros Alcanzados:
• 4 datasets procesados con metodología estructurada
• 5 notebooks de análisis especializados desarrollados
• Tabla relacional integrada con vista 360° del negocio
• Colaboración efectiva humano-IA documentada (57%-43%)
• Insights accionables extraídos para toma de decisiones

Datos listos para fases siguientes:
• Dashboards ejecutivos y visualizaciones Power BI
• Estrategias de marketing basadas en insights de clientes
• Optimización de portfolio de productos
• Modelos predictivos y machine learning avanzado
""",
        7: """
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
        8: """
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
        9: """
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
    +------------------------+
    | Mostrar menú (1..10)   |
    | - 1 Tema/Problema      |
    | - 2 Origen datos       |
    | - 3 Estructura BD      |
    | - 4 Limpieza datos     |
    | - 5 Análisis estadístico|
    | - 6 Insights negocio   |
    | - 7 Pseudocódigo       |
    | - 8 Sugerencias        |
    | - 9 Diagrama (esto)    |
    | - 10 Salir             |
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
        |                  | ¿Está entre 1 y 10? |
        |                  +---------------------+
        |                  |                     |
        |                  No                    Sí
        |                  |                     v
        |           +----------------+    +--------------------------+
        |           | Mostrar error  |    | Opción válida (1..9):    |
        |           |"Ingrese número"|    | Mostrar sección          |
        |           +----------------+    +--------------------------+
        |                  |                     |
        |                  v                     v
[Esperar Enter]    [Esperar Enter]         [Esperar Enter]
        |                  |                     |
        +------------------+---------------------+
                           v
           (volver a Bucle principal)

    Si la opción es 10 -> Mostrar despedida y terminar.
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
            opcion = int(input("\nSeleccione una opción (1-10): "))
            
            # Verificamos la opción seleccionada
            if opcion == 10:
                print("\n¡Gracias por usar el programa!")
                break
            elif opcion >= 1 and opcion <= 9:
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
