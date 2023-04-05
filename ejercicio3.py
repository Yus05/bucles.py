"""
Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla todos los números impares desde 1 hasta ese número separados por comas.
"""

"""OJO:ME FALTA SEPARARLOS POR ,"""

numero = int(input("Escribe un numero entero positivo: "))

numero = int(numero + 1)

"""rango = range(numero)

print(rango)

for valor in rango:
    print(valor)"""

for valor in range(1, numero, 2):
    print(valor)

#EXPLICACION: Con la funcion range puedo crear una secuencia de numeros enteros, para luego poder iterarlos. Como argumento de la funcion range paso el numero que introduce el usuario, pero antes debo sumarle a ese numero un 1, ya que la funcion range no toma el valor final en cuenta sino el anterior a ese. Con el ciclo for, itero cada uno de los valores del rango. Utilizo 3 argumentos, el 1 para que comience a iterar desde el numero 1, el numero que introdujo el usuario, y el 2 porque son los saltos que se va a dar en cada iteracion. 



