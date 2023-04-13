"""
Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y el número de años, y muestre por pantalla el capital obtenido en la inversión cada año que dura la inversión.
"""

#PLANTEAMIENTO: Inicialmente debo obtener una serie de formulas que me van a dar los resultados que me estan pidiendo. 
# COMO HAGO QUE EL CONTADOR SE DETENGA????

cantidad = int(input("Introduce la cantidad a invertir: "))

interes = int(input("Introduce el interes anual: "))

anos = int(input("Introduce los anos: "))

#Debo hacerle algo a la cantidad de anos para reducirla a cero. 

while anos >= 1:
    anos_2 = anos * 12

    formula_1 = (interes * cantidad) / 100

    resultado = formula_1 * anos_2

    print("El capital obtenido en tu inversion es de: ", resultado)

    anos = 0

#Explicacion: Obtuve los datos proporcionados por el cliente / Inicie el ciclo con la condicion dada por los anos que me iba a brindar el cliente / Dentro del ciclo cree las formulas que me iban a calcular las ganancias del clientes / Y para detener el ciclo, lleve el numero de anos a 0 para que la condicion del while deje de cumplirse y me devuelva el return. 
