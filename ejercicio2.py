"""
Escribir un programa que pregunte al usuario su edad y muestre por pantalla todos los años que ha cumplido (desde 1 hasta su edad).
"""
#Debo restar 1 en la edad en cada vuelta.

edad = int(input("Escribe tu edad: "))
contador = 0

while edad >= 1:
    edad = edad - 1

    contador += 1
    
    print("Haz cumplido", contador, "anios")

#PROCEDIMIENTO: En este caso lo que necesito imprimir no es la edad que el usuario me da como tal, es el numero de vueltas que va a dar el ciclo dependiendo de la edad que escriba el usuario, y a esta edad debo restarle un 1 en cada vuelta hasta que sea 0. Al llegar a cero, deja de cumplirse la condicion del ciclo y el contador deja de sumar. 

#Explicacion:

#1- El contador sera quien me de el resultado de la sumatoria, ira sumando en cada vuelta. 

#2- while edad >= 1: -> Mientras la edad sea mayor o igual a 1, ejecuta...

#3- edad = edad - 1 dentro de la condicion -> El usuario pone su edad, le resto uno en cada vuelta hasta que deje de cumplir la condicion, o sea cuando deje de ser menor o igual a uno, se para el bucle y me da el return.

#4- contador += 1 -> Se va imprimiendo la sumatoria en cada vuelta.

#RESUMEN: En el ciclo, resta 1 a la edad y suma uno al contador e imprime contador. Y asi hasta que la edad deja de ser mayor o igual a 1. 

#QUE ESTA PASANDO EN ESTE CICLO WHILE????
#-> El contador inicia conociendo el valor de la variable edad, si NO es mayor o igual a 1 entonces para, si SI es mayor o igual a 1, ejecuta la siguiente linea de codigo que sigue. / La siguiente linea de codigo que sigue es darle un nuevo valor a la variable edad, en ese nuevo valor se le resta un 1. Ya la variable edad tiene un nuevo valor, un digito menos. / Continua con la siguiente linea de codigo, que es sumarle un 1 a la variable contador (Esta variable tenia un valor ya asignado cuando el ciclo se ejecuto, y este es el valor que el ciclo conoce), es a este valor que ya conoce que se le suma 1. Despues de sumar ese valor a contador, continua con la siguiente linea de codigo. / En la siguiente linea de codigo, imprime strings mas el valor nuevo de contador. / Da la vuelta y comienza de nuevo el ciclo pero con un valor nuevo para edad, un valor con un digito menos. / Vuelve a ejecutar cada linea de codigo hasta que la edad se convierta en 0, despues de tantas restas.
    


