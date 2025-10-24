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
    print("4. Pseudocódigo del programa")
    print("5. Sugerencias y mejoras con Copilot")
    print("6. Diagrama de flujo")
    print("7. Salir")
    print("=====================")

def cargar_documentacion():
    """Función que almacena la información de cada sección"""
    # Diccionario con la información de cada opción del menú
    info = {
        1: """
=== Tema, problema y solución ===
Este es un proyecto para analizar ventas y clientes de una tienda.
Se busca determinar:
- Productos menos vendidos
- Productos con menos ganancias
- Tiempo de venta de productos
- Análisis de clientes y sus patrones de compra
""",
        2: """
=== Origen de los datos ===
Los datos provienen de una base de datos de ventas y clientes de una tienda.
La base de datos está conformada por 4 archivos CSV:
- Ventas
- Productos
- Detalle_ventas
- Clientes
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
=== Pseudocódigo del Programa ===

Inicio Programa
    // Función para limpiar la pantalla
    Función limpiar_pantalla():
        Limpiar la consola según el sistema operativo

    // Función para mostrar el menú
    Función mostrar_menu():
        Mostrar título "MENÚ PRINCIPAL"
        Mostrar opciones numeradas del 1 al 6

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
                
                Si opción es 6:
                    Mostrar mensaje de despedida
                    Romper bucle
                Sino Si opción está entre 1 y 5:
                    Mostrar sección correspondiente
                Sino:
                    Mostrar error de opción inválida
            
            Si hay error de tipo:
                Mostrar mensaje de error
                Esperar Enter

    // Inicio del programa
    Si este es el archivo principal:
        Ejecutar main()
Fin Programa"
""",
        5: """
=== Sugerencias y mejoras con Copilot ===
Pendiente de implementar sugerencias y mejoras.
""",
          6: """
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
    | Mostrar menú (1..7)    |
    | - 1 Tema/Problema      |
    | - 2 Origen datos       |
    | - 3 Estructura BD      |
    | - 4 Pseudocódigo       |
    | - 5 Sugerencias        |
    | - 6 Diagrama (esto)    |
    | - 7 Salir              |
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
        |                  | ¿Está entre 1 y 7?  |
        |                  +---------------------+
        |                  |                     |
        |                  No                    Sí
        |                  |                     v
        |           +----------------+    +--------------------------+
        |           | Mostrar error  |    | Opción válida (1..6):    |
        |           |"Ingrese número"|    | Mostrar sección          |
        |           +----------------+    +--------------------------+
        |                  |                     |
        |                  v                     v
[Esperar Enter]    [Esperar Enter]         [Esperar Enter]
        |                  |                     |
        +------------------+---------------------+
                           v
           (volver a Bucle principal)

    Si la opción es 7 -> Mostrar despedida y terminar.
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
            opcion = int(input("\nSeleccione una opción (1-7): "))
            
            # Verificamos la opción seleccionada
            if opcion == 7:
                print("\n¡Gracias por usar el programa!")
                break
            elif opcion >= 1 and opcion <= 6:
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
