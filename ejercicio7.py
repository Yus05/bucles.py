"""
Escribir un programa que muestre por pantalla las tablas de multiplicar del 1 al 10.
"""
#PLANTEAMIENTO: Primero creemos la tabla de multiplicar del 1. 


numeros = range(1, 11)
multiplos = range(1, 11)

for numero in numeros:
    for multiplo in multiplos:
        resultado = numero * multiplo

        print(resultado)

#EXPLICACION: En esta solucion, lo que hice fue crear por medio de la funcion range dos secuencias de numeros que van desde el 1 hasta el 10. Luego por medio del ciclo for multiplique las respectivas iteraciones para imprimir los resultados. 

