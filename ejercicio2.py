"""
Escribir un programa que pregunte al usuario su edad y muestre por pantalla todos los años que ha cumplido (desde 1 hasta su edad).
"""
#Debo restar 1 en la edad en cada vuelta.

edad = int(input("Escribe tu edad: "))
contador = 0

while edad >= 1:
    edad = edad - 1

    contador += 1
    
    print(contador)

#En este caso lo que necesito imprimir no es la edad que el usuario me da como tal, es el numero de vueltas que va a dar el ciclo dependiendo de la edad que escriba el usuario, y a esta edad debo restarle un 1 en cada vuelta hasta que sea 0. Al llegar a cero, deja de cumplirse la condicion del ciclo y el contador deja de sumar. 

#Explicacion:

#2- El contador sera quien me de el resultado de la sumatoria, ira sumando en cada vuelta. 

#3- while edad >= 1: -> Mientras la edad sea mayor o igual a 1, ejecuta...

#4- edad = edad - 1 dentro de la condicion -> El usuario pone su edad, le resto uno en cada vuelta hasta que deje de cumplir la condicion, o sea cuando deje de ser menor o igual a uno, se para el bucle y me da el return.

#5- contador += 1 -> Se va imprimiendo la sumatoria en cada vuelta.

#RESUMEN: En el ciclo, resta 1 a la edad y suma uno al contador e imprime contador. Y asi hasta que la edad deja de ser mayor o igual a 1. 


    


