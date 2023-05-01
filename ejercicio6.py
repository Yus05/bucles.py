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


altura = int(input("Introduce un numero: "))

contador = 0

    
while altura >= 1:
    contador += 1

    print(contador * "*")

    if contador == altura:
        break

#EXPLICACION: Obtuve el numero del usuario. / La variable contador comienza en 0. / En la condicion el dato del usuario debe ser mayor o igual a 1. / Dentro del codigo, el contador comienza a sumar un 1 en cada ciclo y ese dato del contador se va multiplicando por el string "*" en cada ciclo, imprimiendolo. / Con un if creo la condicion, de que al momento en el que se iguala el contador con el numero introducido por el usuario, para la impresion. 

#QUE ESTA PASANDO EN ESTE CICLO WHILE????
#-> El ciclo inicia con la altura, dato proporcionado por el usuario (En este ejemplo, es:5). Si 5 es mayor o igual a 1, ejecuta la linea de codigo siguiente. 
# - La linea de codigo es darle un nuevo valor a la variable contador, sumarle un numero 1, ahora contador vale: 1. Continua con la siguiente linea de codigo.
# - En la siguiente linea de codigo, multiplica ese nuevo valor de contador por el string "*". O sea, 1 * "*". Continua con la siguiente linea de codigo.
# - En la siguiente linea de codigo, vamos con una condicional. La condicional dice que si la variable contador iguala a la variable altura (Dato proporcionado por el usuario), para el ciclo. Como aun el contador no iguala, es 1, entonces el ciclo vuelve a empeza. 
# - El ciclo vuelve a empezar ahora pero con un nuevo valor para contador, que vale 1. Y va a ir sumando de 1 en cada vuelta, hasta que iguale el valor de la altura.

