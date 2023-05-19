"""
Escribir un programa en el que se pregunte al usuario por una frase y una letra, y muestre por pantalla el número de veces que aparece la letra en la frase.
"""

"""frase = input("Escribe una frase: ")
letra = input("Escribe una letra: ")
contador = 0

for caracter in frase:
    if letra == caracter:
        contador += 1
        print(contador)"""

#QUE PASA DENTRO DE ESTE CICLO??
#-> For caracrter in palabra: -> Estamos iterando dentro de la frase. Vamos a recorrer cada una de las letras de la frase.
#-> if letra == caracter: -> Dentro del ciclo for para tomar cada uno de los valores que va a tener caracter en cada iteracion, condicionamos, si la letra dada por el mismo usuario es igual al caracter, ejecuta el siguiente bloque de codigo.
#-> contador += 1 -> Este es el siguiente bloque de codigo, es quien va a contar las vueltas cada vez que letra y caracter coincidan.
#-> print(contador) -> Me va a imprimir el valor de contador en cada vuelta.

#---------------------------------------------------
frase = input("Introduce una frase: ")
letra = input("Introduce una letra")
contador = 0
for i in frase:
    if i == letra:
        contador += 1
print("La letra '%s' aparece %2i veces en la frase '%s'." % (letra, contador, frase))

#Que es %s?
#Que es %2i?
#¿Qué es el formato % string  en Python?

#Estudia y averigua estos nuevos conceptos. Agregalos a las notas de la clase o a una nueva seccion.
