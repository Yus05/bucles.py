"""
Escribir un programa que pida al usuario una palabra y la muestre por pantalla 10 veces.
"""

palabra = input("Escribe una palabra: ")
contador = 1

while contador <= 10:
    print(palabra)

    contador += 1

#EXPLICACION:
# El usuario introduce la palabra.
# Creamos un contador que comienza en 1.
# En el ciclo: Mientras el contador sea menor o igual a 10, ejecuta.
# -> Imprime la palabra que introdujo el usuario, dentro del ciclo el contador aumenta su valor en 1 y como el valor de contador vuelve a ser <= a 10, se vuelve a recorrer el ciclo. Se imprime 10 veces la palabra introducida por el usuario. 

#QUE ESTA PASANDO EN ESTE CICLO WHILE????
#-> El ciclo inicia ya teniendo el valor de la variable contador. Si es menor o igual a 10  ejecuta la linea de codigo que sigue. / La linea que viene es la impresion de la variable palabra, ejecuta esta linea y continua con la linea que sigue. / La linea que sigue es sumarle un uno al valor que ya tomo de contador, al valor con el que inicio. / Le suma un 1 y ya contador no vale 1 sino 2, entonces da la vuelta y vuelve a analizar la condicion, como sigue siendo menor o igual a 10, continua y vuelve a ejecutar la linea de codigo siguiente, y asi continua haciendo esta vuelta hasta que contador deja de ser menor o igual a 10, hasta que contador se hace 11, ahi para y ya no ejecuta los codigos que siguen. 





