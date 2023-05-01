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

    print(valor, end=", ")
    
"""
"end" es un parámetro opcional que se puede pasar a la función de impresión en Python. Este parámetro especifica el carácter o la cadena que se utilizará para finalizar la línea después de imprimir el contenido especificado.
----------------------------------------------
El valor predeterminado de end es \n, lo que significa que después de la instrucción print imprimirá una nueva línea. Entonces, simplemente le digo end que es lo que se desea imprimir después de que se haya ejecutado la instrucción print.

Por ejemplo: - print ("hello",end=" +") imprimirá hello +

El contenido de end se imprime después de lo que desea imprimir. Por defecto, contiene una nueva línea ("\n") pero se puede cambiar a otra cosa, como una cadena vacía.

"""    

#EXPLICACION: Con la funcion range puedo crear una secuencia de numeros enteros, para luego poder iterarlos. Como argumento de la funcion range paso el numero que introduce el usuario, pero antes debo sumarle a ese numero un 1, ya que la funcion range no toma el valor final en cuenta sino el anterior a ese. Con el ciclo for, itero cada uno de los valores del rango. Utilizo 3 argumentos, el 1 para que comience a iterar desde el numero 1, el numero que introdujo el usuario, y el 2 porque son los saltos que se va a dar en cada iteracion. 

#QUE ESTA PASANDO DENTRO EN ESTE CICLO FOR????
#-> Inicia en 1.
# - El limite es el valor de la variable: numero (en el ejemplo es 10). El 1 no llega al limite.
# - Entonces Le suma un 2 al 1, se convierte en 3.
# - Y ejecuta el siguiente codigo que es imprimir el valor antes de la suma del 2.
# - Ahora ya siendo 3, da la vuelta para comenzar nuevamente el ciclo con este nuevo valor (3).
# - LLega otra vez a donde esta el limite (valor de la variable: numero), no lo iguala, sigue siendo menor que el limite.
# - Continua al siguiente paso y le suma dos otra vez, se convierte en 5.
# - Y ejecuta el siguiente codigo que es imprimir el valor antes de la suma del 2. O sea, imprime el 3.
# - Vuelve a repetir el ciclo con este nuevo valor, que es 5 y sigue de largo porque no iguala el limite y suma 2, se convierte en 7.
# - Y ejecuta el siguiente codigo que es imprimir el valor antes de la suma del 2. Imprime 5.
# Vuelve a empezar el ciclo con el valor nuevo que es 7, no lo iguala, suma 2, se convierte en 9,
# - Y ejecuta el siguiente codigo que es imprimir el valor antes de la suma del 2, que es 7.
#  Vuelve a empezar con el nuevo valor que es 9, llega al limite, no lo iguala aun, le suma 2 y se convierte en 11.
# Ejecuta la impresion del valor antes de la suma, que es 9.
# Ya con el valor nuevo que es once, comienza el ciclo pero ya sobrepasa el limite, aqui PARA.

#HASTA AHORA PODRIA CONCLUIR QUE EL CICLO FOR TRANSCURRE DE MANERA HORIZONTAL. SU LINEA IMAGINARIA DE RECORRIDO ES HORIZONTAL. 
#MIENTRAS QUE LA LINEA IMAGINARIA DEL CICLO WHILE ES VERTICAL.



