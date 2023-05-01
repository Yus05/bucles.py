"""
Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y el número de años, y muestre por pantalla el capital obtenido en la inversión cada año que dura la inversión.
"""
#PLANTEAMIENTO:
# Debo montrar en pantalla cuanto genera el monto que ingresa el cliente, con el interes respectivo, por cada ano que dura la inversion.

cantidad = int(input("Cantidad: "))
interes = int(input("Interes: ")) 
anos = int(input("Anos: "))

anos_2 = 12

contador = 0

while anos >= 1:
    interes_2 = int((interes*cantidad)/100)
    interes_2 = int(interes_2 * anos_2)

    contador = contador + 1

    print("El interes ganado en el ano ", contador, "es de: ", interes_2)

    anos_2 = anos_2 + 12
    anos = anos - 1

#QUE ESTA PASANDO EN ESTE CICLO WHILE????
#-> El ciclo inicia con un dato proporcionado por el cliente, que es la cantidad de anos. La condicion es que esta cantidad de anos debe ser mayor que 1, si la cumple continua con la ejecucion de la siguiente linea de codigo. / La siguiente linea de codigo es darle valor a la nueva interes_2, que me va a calcular cuanto va a ganar por mes el cliente./ Continua con la siguiente linea de codigo, en esta linea me calcula la cantidad anterior por la variable anos_2, que vale 12 en este momento, para saber cuanto ganara por ano./ Ejecuta la siguiente linea de codigo, que me va a sumar a la variable contador un 1, y aumenta su valor. / Ejecuta la siguiente linea de codigo, que es la impresion de un string, mas la variable contador con su nuevo valor, mas otro string, mas el resultado de interes_2, que me muestra la ganancia por el primer ano completo. / Ejecuta la siguiente linea de codigo, que me va a sumar la variable anos_2, 12 digitos, para duplicar su valor. / Ejecuta la siguiente linea de codigo, que le resta a la variable anos, un digito, ahora vale un digito menos. Da la vuelta y vuelve a empezar, esta vez con la variable de la condicion con un numero menos pero aun sigue cumpliendo la condicion.

#-> Dentro del ciclo lo que debe incrementar en cada vuelta es la cantidad de meses por los que se va a multiplicar el monto ganado por mes. Por eso en cada vuelta le sumo 12 a la variable que contiene el valor de anos_2./ Y debo reducir en cada vuelta los anos que dura la inversion, ya que es la condicion que tiene el ciclo, por eso le esto uno en cada vuelta, para que cuando llegue a cero ya no se ejecute el ciclo. 

#-> Entra en el ciclo con el valor de anos que da el usuario, cumple la condicio y continua con el siguiente codigo. / Calcula la ganancia del usuario por mes, sigue con la siguiente linea de codigo./ Multiplica la ganancia por 12, para tener ganacia por ano, siguiente linea./ Suma a la variable contador un 1, siguiente linea. / Imprime, string mas el nuevo valor de la variable contador, mas string, mas el valor de la ganacia del usuario. Siguiente linea de codigo./ En esta aumenta la variable anos_2, le aumenta 12 para que ya no representen 12 meses sino 24. (De esta variable ira aumentando 12 en cada vuelta.), siguiente codigo. / Toma la variable anos con la que inicio, y le resta un 1. En cada vuelta se le resta un 1, para que su valor llegue a 0, y deje de cumplirse la condicion. / OJO: Cuando vuelve a iniciar en cada vuelta del ciclo, siempre debe volver a calcular la variable interes_2, para tener nuevamente el valor por mes, lo que va a hacer que ese valor modifique el valor con respecto al valor anterior es que ahora la variable por la que se va a multiplicar va a ser mayor, va a ser 12 veces mas grande, por el aumento en la linea 23. 