"""
Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla la cuenta atrás desde ese número hasta cero separados por comas.
"""

numero = int(input("Escribe un numero entero positivo: "))

numero = numero + 1

while numero >= 1:
    numero = numero - 1
    print(numero, end=",")

#EXPLICACION: Pido el numero al usuario, al numero le sumo un 1 para que al momento en el que el ciclo comience a ejecutar la primera resta, muestre a partir del numero que el usuario introdujo. EN EL CICLO: Mientras el numero sea mayor o igual a 1, ejecuta la resta de 1 al numero y ve imprimiendo cada resta.

#QUE ESTA PASANDO EN ESTE CICLO WHILE????
#-> El ciclo inicia con un valor de la variable numero, si ese valor es mayor o igual a 1, ejecuta la siguiente linea de codigo.
#-> La siguiente linea de codigo es volver a asignarle un nuevo valor a la variable numero. Y ese valor va a ser restarle un 1 a la variable que ya tenia la condicion del ciclo. 
#-> Ejecuta la siguiente linea de codigo, que es imprimir el NUEVO valor de la variable numero y una coma.
#-> Vuelve a "subir" para comenzar con ese nuevo valor de la variable numero a ver si sigue siendo mayor o igual a 1. 

#EMPIEZA CON 4, RESTA A 4 UN 1, SE CONVIERTE EN 3, IMPRIME 3 Y UNA COMA, AHORA ES 3, RESTA UN 1, AHORA ES 2, IMPRIME 2 Y UNA COMA. AHORA EMPIEZA CON 2, RESTA A 2 UN 1, SE CONVIERTE EN 1, IMPRIME 1 Y UNA COMA. EMPIEZA CON 1, RESTA 2. PARA.