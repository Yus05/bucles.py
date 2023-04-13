"""
Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo rectángulo como el de más abajo, de altura el número introducido.

*
**
***
****
*****
"""

#Planteamiento:
# Debo imprimir lineas con asteriscos. La cantidad de lineas que debo imprimir me las va a dar el usuario. La cantidad de asteriscos que va a tener cada linea coincide con la posicion de la linea. 

"""
-> Mi primera etapa del ejercicio con el triangulo volteado:

altura = int(input("Introduce un numero: "))
altura = altura + 1

while altura >= 1:
    altura = altura - 1

    print( altura * "*")
"""

altura = int(input("Introduce un numero: "))

contador = 0

    
while altura >= 1:
    contador += 1

    print(contador * "*")

    if contador == altura:
        break

#EXPLICACION: Obtuve el numero del usuario. / La variable contador comienza en 0. / En la condicion el dato del usuario debe ser mayor o igual a 1. / Dentro del codigo, el contador comienza a sumar un 1 en cada ciclo y ese dato del contador se va multiplicando por el string "*" en cada ciclo, imprimiendolo. / Con un if creo la condicion, de que al momento en el que se iguala el contador con el numero introducido por el usuario, para la impresion. 

