"""
Escribir un programa que pida al usuario una palabra y luego muestre por pantalla una a una las letras de la palabra introducida empezando por la última.
"""

p = input("Escribe una palabra: ")
p = p[::-1]

for caracter in p:
    print(caracter)





