"""
Escribir un programa que muestre por pantalla las tablas de multiplicar del 1 al 10.
"""

numeros = range(1, 11)
multiplos = range(1, 11)

for numero in numeros:
    for multiplo in multiplos:
        resultado = numero * multiplo

        print(resultado)

#EXPLICACION: En esta solucion, lo que hice fue crear por medio de la funcion range dos secuencias de numeros que van desde el 1 hasta el 10. Luego por medio del ciclo for multiplique las respectivas iteraciones para imprimir los resultados. 

#QUE ESTA PASANDO EN ESTE CICLO FOR????
#-> Creo dos variables con una secuencia de numeros que van desde 1 hasta 10.
#-> Itero cada una de estas secuencia de numeros. En la primera iteracion: Para numero en numeros, en donde comienza en 1 y el limite es 11. Comienza la primera vuelta en 1, va sumando 1 valor en cada vuelta hasta que se convierte en 11 y detiene la iteracion. 
#-> En el segundo for, para exactamente igual al for anterior. Ciclo horizontal.
#-> Cumple las respectivas iteraciones, para continuar con la siguiente linea de codigo. En donde multiplica entre si, cada uno de los resultados de esta iteracion para continuar con la siguiente linea de codigo, en donde imprime cada una de estas miltiplicaciones. 

#for numero in range(1, 11):
#-> Entra siendo 1, pasa al limite y aun no lo alcanza, suma 1. Entra siendo 2, pasa al limite y aun no lo alcanza, suma 1. Entra siendo 3... Hasta que se convierte en 11 y para.
