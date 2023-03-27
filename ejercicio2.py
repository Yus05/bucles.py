"""
Escribir un programa que pregunte al usuario su edad y muestre por pantalla todos los años que ha cumplido (desde 1 hasta su edad).
"""
#Debo restar 1 en la edad en cada vuelta.


edad = int(input("Escribe tu edad: "))
edad = edad - 1
contador = 0 


while edad >= 0:
    edad = edad - 1

    contador += 1
    
    print(contador)
    


