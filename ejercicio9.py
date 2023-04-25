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

#NOTA: Si yo pido la contrasena afuera, ese dato me va a servir para inicilizar el ciclo. Pero una vez que ciclo comience, y la contrasena sea incorrecta, este va a volver ejecutar el input, el cual es la orden que se pone despues de los dos puntos. O sea, si son diferentes ejecuta este bloque de codigo, el bloque es el input. Y asi la escriba correcta el siempre va a volver a ejecutar el input, porque no le estoy dando un nuevo valor a password, siempre se va mantener el primer valor que escribi la primera vez que se ejecuto el password = input("Introduce la contrasena: "). Por esa razon de VOLVER A PEDIR UN NUEVO VALOR PARA PASSWORD DENTRO DEL CICLO. Esto para entender porque no funcionaba esto:

"""
key = "contrasena"

password = input("Introduce la contrasena correcta: ")

while password != key:
    input("Introduce la contrasena: ")

print("Contrasena correcta.")

"""





  
