"""
Escribir un programa que muestre el eco de todo lo que el usuario introduzca hasta que el usuario escriba “salir” que terminará.
"""

usuario = " "
out = "salir"

while usuario != out:
    usuario = input("Escribe: ")
    print(usuario)
    if usuario == out:
        print("Bye")
        break

#QUE OCURRE DENTRO DE ESTE CODIGO??
# - Declaro la variable usuario fuera, con un string vacio. Declaro la variable que tendra el valor de salida. 

#- En el ciclo: La condicion es que si el valor que esta por introducir el usuario es diferente a la variable que da la salida, ejecuta la siguiente linea de codigo. 

#- En la siguiente linea de codigo ejecuto el input, y le asigno el valor a la variable usuario. POR QUE EJECUTO EL INPUT DENTRO DEL CICLO? Si lo ejecuto afuera, se crea un ciclo infinito si usuario es distinto a out.

#- Imprimo ese input que me va a dar el usuario. 

#- La condicion del if, me dice que si ese input es igual al valor de salida, simplemente pare el script.

#REVISA LA SOLUCION DE ALF.
