"""
Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla la cuenta atrás desde ese número hasta cero separados por comas.
"""

#Deberia tomar la secuencia de numeros, voltearla y luego recorrerla. 

numero = int(input("Escribe un numero entero positivo: "))

numero = numero + 1

while numero >= 1:
    numero = numero - 1
    print(numero, end=",")

#EXPLICACION: Pido el numero al usuario, al numero le sumo un 1 para que al momento en el que el ciclo comience a ejecutar la primera resta, muestre a partir del numero que el usuario introdujo. EN EL CICLO: Mientras el numero sea mayor o igual a 1, ejecuta la resta de 1 al numero y ve imprimiendo cada resta.