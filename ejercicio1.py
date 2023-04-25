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
#-> 





