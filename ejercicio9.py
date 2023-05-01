"""
Escribir un programa que almacene la cadena de caracteres contraseña en una variable, pregunte al usuario por la contraseña hasta que introduzca la contraseña correcta.
"""
#PLANTEAMIENTO: Cada vez que el usuario de una contrasena incorrecta, debo volver a pedirle que escriba la contrasena correcta.


key = "contrasena"

password = ""

while password != key:
    password = input("Introduce la contrasena: ")
#mientras que el password y la llave sean diferentes -> Busca el valor del password.  

print("Contrasena correcta.")
#Si no son diferentes, quiere decir que son iguales. No se cumple la condicion del while, entonces solo ejecuta la linea 12 y luego directamente el print.

#-> Pide el password adentro del ciclo, para ahorra codigo. Ya que si lo pedia afuera, de igual forma iba a necesitar pedirlo adentro.

#NOTA: Si yo pido la contrasena afuera, ese dato me va a servir para inicilizar el ciclo. Pero una vez que ciclo comience, y la contrasena sea incorrecta, este va a volver ejecutar el input, el cual es la orden que se pone despues de los dos puntos. O sea, si son diferentes ejecuta este bloque de codigo, el bloque es el input. Y asi la escriba correcta el siempre va a volver a ejecutar el input, porque no le estoy dando un nuevo valor a password, siempre se va mantener el primer valor que escribi la primera vez que se ejecuto el password = input("Introduce la contrasena: "). Por esa razon de VOLVER A PEDIR UN NUEVO VALOR PARA PASSWORD DENTRO DEL CICLO. 

#QUE ESTA PASANDO EN ESTE CICLO WHILE????
#-> Mientra el password sea diferente que key, ejecuta el siguiente codigo. 
#-> La siguiente linea de codigo es obtener el valor de password. En caso de ser iguales, se sale el ciclo, se rompe el ciclo, entonces lo que hace es ejecutar la siguiente linea que este fuera del ciclo, y en este caso es imprimir "Contrasena correcta.". 
#-> Pero en caso de que la contrasena que se introduce sea diferente de key, el ciclo se vuelve a ejecutar, la linea imaginaria da una vuelta y vuelve a ejecutar el input, vuelve a pedir la contrasena hasta que se escriba la contrasena correcta.






  
