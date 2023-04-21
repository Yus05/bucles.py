"""
Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo rectángulo como el de más abajo.

1
3 1
5 3 1
7 5 3 1
9 7 5 3 1
"""

#YA TIENES LA EXPLICACION DE QUE ES LO QUE PASA ADENTRO, AHORA ANALIZA EL EJERCICIO EN GLOBAL. 

#Solucion de la web:
#n = int(input("Introduce la altura del triángulo (entero positivo): "))
#for i in range(1, n+1, 2):
 #   for j in range(i, 0, -2):
  #      print(j, end=" ")
   # print("")
#------------------------------------------------
#Explicacion etapa I: Range de una range. 

"""n = int(input("Numero entero: "))

for i in range(n+1):
    #print(i)
    for j in range(i):
        print(j)"""

#El metodo range me permite iterar una secuencia de numeros que van desde 0 hasta el numero que coloque como argumento del metodo.
#  Entonces si itero por medio de un for otra secuencia que ya fue iterada, QUE RESULTADO ME DA? - Posiblemente me itera cada uno de los numeros de la secuencia anterior. O sea, me itera el 3-> 2 1 0 / Me itera el 2-> 1 0 / Me itera el 0 -> 0

#------------------------------------------------
#Explicacion etapa II: Argumentos.

n = int(input("Numero entero: "))

for i in range(1, n+1, 2):
    for j in range(i, 0, -2):
        print(j, end=" ")



#PRIMER FOR: 
#-> La secuencia del i con los argumentos(n+1), usando el numero 3:  0, 1, 2, 3
#-> La secuencia del i con los argumentos(1, n+1, 2), usando el numero 3: 1, 3 => Empieza en 1, y da dos saltos hasta el 3.

#SEGUNDO FOR:
#-> Cuando aplico el segundo for, con argumento en range(i) y poniendo el 3 como numero. Me va a iterar solo los numeros: 1 y 3. Entonces el resultado en consola es: 2, 1, 0, 0. / 3-> 2,1,0 / 1->0.

#ARGUMENTOS DEL 2do RANGE (i, 0, -2):
#-> Creo, el primer argumento representa el inicio. Entonces si yo uso el i, como primer argumento, quiere decir que comienza ahi, que comience a partir de ese valor en cada iteracion.
#-> Creo, el segundo argumento en realidad es el limite. El limite en este caso es hasta donde "debe llegar la iteracion", en el primer for ese limite es el numero que pone el usuario, en este ejemplo es 0, pero no 0 sino el numero aterior a 0.
# #-> Tercer argumento, saltos de -2. Para que vaya restando a cada valor. 
#-> Debo ver los argumentos como: (inicio, limite,saltos).
#-> El ciclo del segundo for va asi: Inicia en el valor de i, si i vale 3 entonces inicia ahi, el limite es 0, por lo tanto continua, se le restan a ese 3 menos 2, se convierte en 1. Vuelve a empezar, se imprime ese 1, que no llega al limine que es 0, entonces se le restan menos 2, se convierte en -2, ya paso su limite, no se imprime mas.
#--> ENTONCES, SI EL NUMERO DEL USUARIO ES 5 Y SOLO IMPRIME J, SIN EL END=" ": Toma cada uno de los numeros y les va restando 2, y los va imprimiendo cada uno en una linea.

#CON EL END=" " EN EL 2DO FOR:
#-> Me imprime el mismo resultado de arriba pero, en horizontal.

#CON EL print("") DEL PRIMER FOR. 
#-> https://www.youtube.com/watch?v=uhbpAFbwc50 min:6. NECESITO ENTENDER ESTO.








#----------------------------------------------
#NOTA:QUE PASA DENTRO DE UN CICLO FOR CON RANGE???
#-> for valor in range(5, 21, 2):
#-> Entra en 5, se imprime ese valor (Es su inicio).
#-> Su limite es 21 -1, o sea es 20. Aun no llega a ese numero, por lo tanto vuelte continua.
# ->  A ese cinco le suma 2, se convierte en 7.
#-> Se imprime el 7.
#-> Sigue sin llegar al limite.
#-> Le suma 2, se convierte en 9.
#-> Se imprime el 9.
#-> No llega al limite aun.
#-> Vuelve a sumar 2, se es 11.
#-> Se imprime el 11.
#-> Sigue sin llegar al limite.
#-> Suma 2, ahora es 13.
#-> Se imprime, no llega al limite, suma 2 y ahora es 15, se imprime ese 15, no llega al limite, se suman 2 mas, ahora es 17, se imprime y no llega al limite, se suman 2 y es 19. Se imprime el 19, aun no llega al limite, se le suman 2 mas, y ya llega al 21. No se vuelve a imprimir, ya cumplio el ciclo. 












