import os
import time
import numpy as np


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

def main():
    datos_generados = []

    while True:
        mostrar_pantalla_principal()
        seleccion = input("Selecciones una opción: ")
        
        if seleccion == "1":
            print("\n\nIndique el rango de valores a usar aleatoriamente:")
            rango_desde = int(input("\nDesde el número: "))
            rango_hasta = int(input("\nHasta el numero: "))
            if rango_hasta <= rango_desde:
                print("\nEl valor 'Hasta el número' debe ser mayor que 'Desde el número'. Vuelve a intentarlo.")
                input("\nPresiona Enter para continuar...")
                continue
            cantidad_datos = int(input("\nCantidad de datos aleatorios a genera: "))
            if cantidad_datos <= 0:
                print("\nLa cantidad de datos debe ser un número positivo. Vuelve a intentarlo.")
                input("\nPresiona Enter para continuar...")
                continue
            datos_generados = np.random.choice(range(rango_desde, rango_hasta), size=cantidad_datos, replace=True)
            pantalla_generado_datos()

            
        elif seleccion == "2":
            if len(datos_generados) < 1:
                print("\nNo tienes datos generados, vuelve a intentarlo")
                input("\nPresiona Enter para continuar...")
            else:
                limpiar_pantalla()
                print("""
                ╔═══════════════════════════════════════════════════╗
                ║                 ESTADÍSTICAS                      ║
                ╚═══════════════════════════════════════════════════╝
                """)
                print(f"📊 Media: {np.mean(datos_generados):.4f}")
                print(f"📈 Desviación Estándar: {np.std(datos_generados, ddof=1):.4f}")
                print(f"📋 Varianza: {np.var(datos_generados, ddof=1):.4f}")
                print(f"🎯 Esperanza (Valor Esperado): {np.mean(datos_generados):.4f}")
                print(f"📏 Cantidad de datos: {len(datos_generados)}")
                
                input("\nPresiona Enter para continuar...")
        elif seleccion == "0":
            print("\nGracias por usar nuestros programa!!!!! Hasta la vista!!!!")
            break
        else:
            print("\nValor no válido, vuelva a intentarlo")
            input("\nPresiona Enter para continuar...")

main()