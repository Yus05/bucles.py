"""
Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla todos los números impares desde 1 hasta ese número separados por comas.
"""

numero = int(input("Escribe un numero entero positivo: "))

numero = int(numero + 1)

"""rango = range(numero)

print(rango)

for valor in rango:
    print(valor)"""

for valor in range(1, numero, 2):
    #print(valor,",")
    print(valor, end=", ")
    
"""
"end" es un parámetro opcional que se puede pasar a la función de impresión en Python. Este parámetro especifica el carácter o la cadena que se utilizará para finalizar la línea después de imprimir el contenido especificado.
----------------------------------------------
El valor predeterminado de end es \n, lo que significa que después de la instrucción print imprimirá una nueva línea. Entonces, simplemente le digo end que es lo que se desea imprimir después de que se haya ejecutado la instrucción print.

Por ejemplo: - print ("hello",end=" +") imprimirá hello +

El contenido de end se imprime después de lo que desea imprimir. Por defecto, contiene una nueva línea ("\n") pero se puede cambiar a otra cosa, como una cadena vacía.

"""    

#EXPLICACION: Con la funcion range puedo crear una secuencia de numeros enteros, para luego poder iterarlos. Como argumento de la funcion range paso el numero que introduce el usuario, pero antes debo sumarle a ese numero un 1, ya que la funcion range no toma el valor final en cuenta sino el anterior a ese. Con el ciclo for, itero cada uno de los valores del rango. Utilizo 3 argumentos, el 1 para que comience a iterar desde el numero 1, el numero que introdujo el usuario, y el 2 porque son los saltos que se va a dar en cada iteracion. 



