"""
Escribir un programa que muestre por pantalla las tablas de multiplicar del 1 al 10.
"""
#PLANTEAMIENTO: Primero creemos la tabla de multiplicar del 1. 

"""
numeros = range(11)

multiplo = 1
multiplo_2 = 2
multiplo_3 = 3
multiplo_4 = 4
multiplo_5 = 5
multiplo_6 = 6
multiplo_7 = 7
multiplo_8 = 8
multiplo_9 = 9
multiplo_10 = 10

for numero in numeros:

    tabla = multiplo * numero 
    tabla_2 = multiplo_2 * numero
    tabla_3 = multiplo_3 * numero
    tabla_4 = multiplo_4 * numero
    tabla_5 = multiplo_5 * numero
    tabla_6 = multiplo_6 * numero
    tabla_7 = multiplo_7 * numero
    tabla_8 = multiplo_8 * numero
    tabla_9 = multiplo_9 * numero
    tabla_10 = multiplo_10 * numero

    print(tabla, tabla_2, tabla_3, tabla_4, tabla_5, tabla_6, tabla_7, tabla_8, tabla_9, tabla_10)
    #print(numero)

#EXPLICACION: Con la funcion range, creamos una secuencia de numeros que va desde 0 hasta 10 -> numeros = range(11). Para luego iterarlos uno a uno con el ciclo for. La iteracion de dichos numeros, la multiplico por los numeros que van del uno al 10, para luego imprimir sus resultados (tablas del 1 al 10).
"""

numeros = range(1, 11)
multiplos = range(1, 11)

for numero in numeros:
    for multiplo in multiplos:
        resultado = numero * multiplo

        print(resultado)

#EXPLICACION: En esta solucion, lo que hice fue crear por medio de la funcion range dos secuencias de numeros que van desde el 1 hasta el 10. Luego por medio del ciclo for multiplique las respectivas iteraciones para imprimir los resultados. 

#OJO: ANALIZAR UNA VEZ MAS MIS SOLUCIONES PARA TRATAR DE OPTIMIZAR EL CODIGO. 
