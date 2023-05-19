"""
Escribir un programa que pida al usuario un número entero positivo mayor que 2 y muestre por pantalla si es un número primo o no.
"""
#n = int(input("Numero entero > 2: "))
#i = 2

#while i < n: #hace que el ciclo se ejecute hasta el numero anterior al numero del usuario.
 #   y = n%i
  #  i += 1

    #if y == 0:
    #print(...)
    #else:
    #print(...)
#--------------------------------------------------
n = int(input("Introduce un número entero positivo mayor que 2: "))
i = 2
while n % i != 0:
    i += 1
if i == n:
    print(str(n) + " es primo")
else:
    print(str(n) + " no es primo")

# -> WHILE: Mientras el modulo del numero introducido con i (i empieza en 0) por el usuario sea diferente de 0, sumale un 1 a i. Esta es la condicion del while. 

# -> IF: Si i es igual al numero introducido por el usuario, si i en cada iteracion va aumentando en 1, y llega a ser igual al numero introducido por el usuario, imprime: es primo. Esto es porque si el valor de i efectivamente va aumentando 1, entonces la condicion del while se cumple, o sea, el modulo entre el numero que introdujo el usuario y el i en cada iteracion es distinto de cero, y fue distinto de cero hasta llegar a igualarse con el numero que introdujo el usuario. Y como en cada iteracion no fue nunca cero el modulo, entonces es primo.

# -> ELSE: Sino, imprime: no es primo. Esto es porque, si i no llega a igualarse con el numero que introdujo el usuario nunca, entonces la condicion del while no se cumple, o sea el modulo entre el numero del usuario y i, es cero, entonces no es primo. 

#DIFERENCIAS CON MI SOLUCION:
#Se pone la operacion en la misma condicion, no despues del while. Esto hace que la operacion no se ejecute en cada vuelta del ciclo y no se imprima en cada vuelta del ciclo el: es primo o no es primo, segun lo que corresponda. Entonces, poner la operacion en la misma condicion, es una manera de "sacar" la condicion del while.


#https://www.mclibre.org/consultar/python/lecciones/python-while.html
#https://www.freecodecamp.org/espanol/news/explicacion-del-bucle-while-de-while/






















 





    




        




