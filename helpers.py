import os
import time
import numpy as np
import matplotlib.pyplot as plt

def limpiar_pantalla():
    os.system("cls")


def mostrar_pantalla_principal():
    limpiar_pantalla()
    print("""
    ╔═══════════════════════════════════════════════════╗
    ║             MÁQUINA DE PROBABILIDAD               ║
    ║               Análisis de Emails                  ║
    ╚═══════════════════════════════════════════════════╝

            1) Generar nuevo datos.
            2) Ver estadísticas.
            3) Ver gráficos.
            0) Salir

    """)


def pantalla_generado_datos():
    limpiar_pantalla()
    print("""
        ╔═══════════════════════════════════════════════════╗
        ║               Generando los datos,                ║
        ║               Por favor espere...                 ║
        ╚═══════════════════════════════════════════════════╝
        """)
    time.sleep(3)
    limpiar_pantalla()
    print("""
        ╔═══════════════════════════════════════════════════╗
        ║          Datos generados con éxito!!!             ║
        ╚═══════════════════════════════════════════════════╝
        """)
    input("\nPresiona Enter para continuar...")


def pantalla_calculando_datos():
    limpiar_pantalla()
    print("""
        ╔═══════════════════════════════════════════════════╗
        ║               Contando los elementos              ║
        ║               Por favor espere...                 ║
        ╚═══════════════════════════════════════════════════╝
        """)
    time.sleep(3)
    limpiar_pantalla()
    print("""
        ╔═══════════════════════════════════════════════════╗
        ║          Datos generados con éxito!!!             ║
        ╚═══════════════════════════════════════════════════╝
        """)
    input("\nPresiona Enter para continuar...")


def mostrar_graficos(datos):
    """Función para mostrar diferentes tipos de gráficos"""
    limpiar_pantalla()
    print("""
    ╔═══════════════════════════════════════════════════╗
    ║                    GRÁFICOS                       ║
    ╚═══════════════════════════════════════════════════╝
    
            1) Histograma
            2) Gráfico de línea
            3) Gráfico de barras (frecuencias)
            4) Mostrar todos los gráficos
            0) Volver al menú principal
    """)
    
    opcion = input("Selecciona el tipo de gráfico: ")
    
    if opcion == "1":
        mostrar_histograma(datos)
    elif opcion == "2":
        mostrar_grafico_linea(datos)
    elif opcion == "3":
        mostrar_grafico_barras(datos)
    elif opcion == "4":
        mostrar_todos_graficos(datos)
    elif opcion == "0":
        return
    else:
        print("\nOpción no válida")
        input("\nPresiona Enter para continuar...")

def mostrar_histograma(datos):
    """Muestra un histograma de los datos"""
    plt.figure(figsize=(10, 6))
    plt.hist(datos, bins=min(20, len(np.unique(datos))), alpha=0.7, color='skyblue', edgecolor='black')
    plt.title('📊 Distribución de los Datos Generados', fontsize=14, fontweight='bold')
    plt.xlabel('Valores')
    plt.ylabel('Frecuencia')
    plt.grid(True, alpha=0.3)
    
    # Agregar estadísticas en el gráfico
    media = np.mean(datos)
    plt.axvline(media, color='red', linestyle='--', linewidth=2, label=f'Media: {media:.2f}')
    plt.legend()
    
    plt.tight_layout()
    plt.show()

def mostrar_grafico_linea(datos):
    """Muestra un gráfico de línea de los datos"""
    plt.figure(figsize=(12, 6))
    plt.plot(range(len(datos)), datos, marker='o', markersize=3, linewidth=1, alpha=0.7)
    plt.title('📈 Secuencia de Datos Generados', fontsize=14, fontweight='bold')
    plt.xlabel('Índice')
    plt.ylabel('Valor')
    plt.grid(True, alpha=0.3)
    
    # Línea de la media
    media = np.mean(datos)
    plt.axhline(media, color='red', linestyle='--', linewidth=2, label=f'Media: {media:.2f}')
    plt.legend()
    
    plt.tight_layout()
    plt.show()

def mostrar_grafico_barras(datos):
    """Muestra un gráfico de barras con las frecuencias"""
    valores_unicos, frecuencias = np.unique(datos, return_counts=True)
    
    plt.figure(figsize=(12, 6))
    plt.bar(valores_unicos, frecuencias, alpha=0.7, color='lightgreen', edgecolor='black')
    plt.title('📋 Frecuencia de Cada Valor', fontsize=14, fontweight='bold')
    plt.xlabel('Valores')
    plt.ylabel('Frecuencia')
    plt.grid(True, alpha=0.3, axis='y')
    
    # Rotar etiquetas si hay muchos valores
    if len(valores_unicos) > 10:
        plt.xticks(rotation=45)
    
    plt.tight_layout()
    plt.show()

def mostrar_todos_graficos(datos):
    """Muestra todos los gráficos en una sola ventana"""
    fig, axes = plt.subplots(2, 2, figsize=(15, 10))
    fig.suptitle('📊 Análisis Completo de los Datos', fontsize=16, fontweight='bold')
    
    # Histograma
    axes[0, 0].hist(datos, bins=min(20, len(np.unique(datos))), alpha=0.7, color='skyblue', edgecolor='black')
    axes[0, 0].set_title('Histograma')
    axes[0, 0].set_xlabel('Valores')
    axes[0, 0].set_ylabel('Frecuencia')
    axes[0, 0].grid(True, alpha=0.3)
    
    # Gráfico de línea
    axes[0, 1].plot(range(len(datos)), datos, marker='o', markersize=2, linewidth=1, alpha=0.7)
    axes[0, 1].set_title('Secuencia de Datos')
    axes[0, 1].set_xlabel('Índice')
    axes[0, 1].set_ylabel('Valor')
    axes[0, 1].grid(True, alpha=0.3)
    
    # Gráfico de barras
    valores_unicos, frecuencias = np.unique(datos, return_counts=True)
    axes[1, 0].bar(valores_unicos, frecuencias, alpha=0.7, color='lightgreen', edgecolor='black')
    axes[1, 0].set_title('Frecuencias')
    axes[1, 0].set_xlabel('Valores')
    axes[1, 0].set_ylabel('Frecuencia')
    axes[1, 0].grid(True, alpha=0.3, axis='y')
    
    # Box plot
    axes[1, 1].boxplot(datos, patch_artist=True, boxprops=dict(facecolor='lightcoral'))
    axes[1, 1].set_title('Box Plot')
    axes[1, 1].set_ylabel('Valores')
    axes[1, 1].grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.show()