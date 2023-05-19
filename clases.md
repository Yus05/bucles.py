# 1) Clase 1-Presentacion del curso.
-------------------------------------------
# 2) Clase 2-Instalacion.
-------------------------------------------
# 3) Clase 3-Editores de texto.
-> Mediante un editor de texto podremos almacenar nuestros archivos .py 
- Si en el batch ejecuto el comando: code . se abre el VSC cargando todos los folders y archivos que se encuentren dentro de esta ruta. 
-------------------------------------------
# 4) Clase 4-Ejecutar scripts.

## -> Vamos a ejecutar nuestros programas en python. 

- Creamos un archivo nuevo en VSC, con la extension .py

- Vamos a hacer un "hola mundo". Vamos a imprimir un mensaje en consola usando la funcion print. 
print("Hola mundo")-> De esta forma es como nosotros podremos mostrar un mensaje en consola. Usando la funcion print y pasamos como argumento dentro de los parentesis el mensaje que queremos que se visualice en consola dentro de comillas simples o dobles. Ejecuto y guardo.

- Ahora vamos a ejecutar este programa, para eso nos podemos apoyar de la terminal o cmd. Abrimos la terminal y nos situamos en la misma ruta donde se encuentra el archivo. Los comando que usamos: cd para movernos entre carpetas, dir para ver los archivos internos que estan en la carpeta donde tengo mi archivo y cls para limpiar la consola. 

- Una vez nos encontremos en la ruta donde se encuentra el archivo que queremos ejecutar colocamos: 
python nombre_del_archivo.py -> python main.py
Listo, ya con esto visualizamos en consola el mensaje Hola mundo.

-------------------------------------------
# 5) Clase 5-Variables.

Una variable es una direccion en memoria donde seremos capaces de almacenar diferentes valores. 
Una variable sera representada mediante una etiqueta, o mediante un nombre. Comunmente las variables modifican su valor en tiempo de ejecucion. 

Comunmente asociamos el termino variable con una pequena caja donde almacenamos valores pero en python esta analogia NO ES la correcta, en python debemos ver a la variables como etiquetas. 

Creando variables (estructura):

1- Creamos el nombre de la varible: Debe ser un nombre descriptivo, que por si solo nos explique que valores esta almacenando. 

2- Posteriormente el signo =

3- Y despues el colocamos el valor que queremos sea almacenado en la variable. 

Ejm: 
<nombre> = <valor>

-> Mediante esta estructura seremos capaces de crear la N cantidad de variables que nosotros deseemos. 

-> Una vez que nosotros definamos una variable, podemos hacer uso de ella la N cantidad de veces que nosotros deseemos. 

Practica: 
Una variable que almacene el nombre del curso:

curso = "Curso profesional de python"

Ahora queremos imprimir en consola el valor que esta variable almacena. Con el comando: python variables.py
------

Tambien podemos modificar el valor de la variable en tiempo de ejecucion. Para hacerlo debemos solo reescribir la variable debajo de la anterior y ponerle el nuevo valor que queremos que almacene. Ejm:

curso = "Curso Python"

La ejecucion de un programa es de forma DESCENDENTE, primero se ejecuta la linea #1, despues la #3 y finalmente la #5. 

Podemos modificar los valor de una variable la N cantidad de veces que deseemos. 

Siempre que creemos una variable debemos usar un nombre lo mas descriptivo posible, debemos evitar nombres como: x, y, etc. En el ejemplo anterior podemos mejorar el nombre que creamos de la variable, podriamos llamarlo: 

titulo_curso =  "Curso profesional de Python"

-> En este caso el nombre de mi variable se encuentra conformado por 2 palabras. Siempre que utilicemos 2 o mas palabras haremos uso de la nomenclatura snake case.
Esta nomenclatura nos indica que vamos a unir estas palabras con un guion bajo y vamos a poner todas la letras de estas palabras en minusculas. Entonces por buenas practicas haremos uso de la nomenclatura snake case. Ejm:

 nombre_completo = "Yusmary Coromoto Somaza Oropeza"


Importante: En Python existen un par de palabras que no podemos utilizar para nombrar variables, ya que son palabras reservadas de Python, si las usamos entrariamos en conflicto con el lenguaje. 

-------------------------------------------
# 6) Clase 6- Constantes. 

Una constante es una variable la cual no puede modificar su valor en tiempo de ejecucion. En Python las constantes no existen, asi que si nosotros quisieramos implementar constantes en nuestros proyectos entonces deberiamos seguir una convencion, una convencion que es respetada por toda la comunidad de desarrolladores Python. 

Vamos a crear una constante que nos permita almacenar el titulo de este curso, para ello vamos a seguir la siguiente convencion:

1- Vamos a declarar una variable que tenga todas sus letras en mayusculas (De esta forma vamos a indicar que esta variable la queremos tratar como constante y unicamente la vamos a utilizar para lectura y no para escritura)(Al utilizar todas sus letras en mayusculas indico que esta variable se tratara de una constante): 

TITULO_CURSO = "Curso profesional de Python"

-> El valor que le indicamos debe ir entre comillas. 

Podemos hacer uso de esa constante de la misma forma que lo hago con una variable, obviamente. 

TITULO_CURSO = "Curso profesional de Python"

print(TITULO_CURSO)

Y ejecuto en consola con el comando: python constantes.py

IMPORTANTE destacar que esta no es una constante como la que utilizamos en otros lenguajes, ya que es simplemente una variable que tiene todas sus letras en mayusculas, por lo tanto actua como una variable. Sin embargo siempre que nos topemos con una variable que tenga todas sus letras en mayusculas quiere que debemos tratar a esta variable como una constante y UNICAMENTE la vamos a utilizar para lectura y no para escritura.   

-------------------------------------------
# 7) Clase 7- Palabras reservadas en Python.

Cómo menciamos en vídeos anteriores, existen ciertas palabras las cuales no podemos utilizar para nombrar a nuestras variables, funciones o clases. A este tipo de palabras las conoceremos como palabras reservadas. Y estan diseñadas para realizar tareas especificas por parte del lenguajes.

Aquí el listado de todas ellas:

False
class
is
return
None
def
nonlocal
while
and
del
not
with
as
elif
or
yield
assert
else
pass
break
except
raise

En el curso trabajaremos con la mayoría de las palabras reservadas, sin embargo, si quieres conocer todas ellas, puedes consultar el siguiente link: https://www.programiz.com/python-programming/keyword-list

-------------------------------------------
# 7) Clase 8- Comentarios.

En Python tenemos dos formas para que nosotros podamos comentar nuestro codigo:

Forma 1- Por medio del signo numeral (hashtag o gato) podemos comentar una sola linea de codigo:
## Esta unica linea esta comentada.


Forma 2- Por medio del triple comillas dobles podemos comentar multiples lineas de codigo:

""" 
Este es un comentario 
que posee saltos 
de linea.
"""

-------------------------------------------
# 9) Clase 9- Tipos de datos. 

En Python nosotros podemos trabajar con diferentes tipos de datos. 

Que es un tipo de dato?
-> Es la propiedad de un valor para poder determinar que valores puede tomar.  

En esta clase vamos a trabajar con 4 tipos de datos, los mas comunes. Vamos a trabajar con los datos tipo:

- String -> Este tipo de dato nos permite trabajar textos, y lo hacemos mediante comillas dobles o comillas simples.

titulo_curso = "Curso profesional de Python"
print(titulo_curso)

nombre_completo = 'Eduardo Ismael'
print(nombre_completo)

-> Utilizar comillas dobles o comillas simples es exactamente lo mismo en cuanto resultado pero,
Cuando debo usar comillas dobles o comillas simples???
Si por ejemplo dentro del texto que vamos a trabajar hay comillas dobles entonces para los string usamos comillas simples o si dentro del texto hay comillas simples usamos comillas dobles para los strings. Ejm:

mensaje = '"CodigoFacilito"'
print(mensaje)
-> En este caso quiero que el texto tenga comillas dobles, por lo tanto imprimo en consola con comillas simples. En la ejecucion vamos a ver "CodigoFacilito" ya que forman parte del texto.


Si nosotros queremos trabajar con un texto largo que posea saltos de linea como por ejemplo un texto, podemos usar triple comillas dobles o triple comillas simples y va a funcionar como un string normal pero con saltos de linea. Ejm:

mensaje = '''Te encuentras 
en el curso: Profesional de Python.
En CodigoFacilito'''
print(mensaje)
-> En consola visualizaremos el parrafo con sus saltos de linea correspondiente.
------------------------------------------------------

- Int -> Este tipo de datos nos permite trabajar con numeros enteros, pueden ser numeros enteros positivos o numeros enteros negativos. Ejm:

numero_uno = 10
print(numero_uno)
-> Esta variable es de tipo entero, ya que almacena un numero entero positivo. Tambien podria ser un -10. 


------------------------------------------------------
- Float -> Este tipo de dato nos permite almacenar numeros positivos o negativos que sean reales o sea, numeros que posean punto decimal. Ejm:

numero_dos = 3.14
print(numero_dos)


IMPORTANTE: 

Siempre que nosotros trabajemos con numeros, ya sean numero enteros o numeros flotantes podemos hacer uso de operadores aritmeticos (suma, resta, multiplicacion o division). Ejm:

numero_uno = 10 + 20
print(numero_uno)
-> El resultado de esta suma se va a almacenar en mi variable numero_uno. O sea, en consola me va a mostrar: 30

Si queremos dividir y necesitamos que el resultado de esa division sea un numero entero, entonces vamos a dividir utilizando doble slash //. Ejm:

numero_uno = 10 / 3
print(numero_uno)

En consola me muestra un numero flotante: 3.3333333335

numero_uno = 10 // 3
print(numero_uno)

En consola me muestra el numero entero: 3 


-------------------------------------------------------
- Bool -> Este tipo de dato se caracteriza porque unicamente puede almacenar dos valores, ya sea verdadero o falso. Ejm: 

valor = True
print(valor)

En consola me muestra: True

valor = False
print(false)

En consola me muestra: False

#Los valores el True y el False van a poseer su primer caracter en mayusculas. 

-------------------------------------------------
# 10) Clase 10- Tipado dinamico.

Tipado dinamico: Es la posibilidad que tienen las variables de poder almacenar diferentes tipos de datos en diferentes momentos. Ejm:

valor = "Eduardo"
valor = 2
valor = 3.1
valor = True

print(valor)

-> En consola ejecuto y me aparece True. En este caso la variable almacena un string, pero a medida que va avanzando almacena diferentes tipos de datos. 

Si imprimiera en consola los diferentes valores que tiene la variable, puedo hacerlo de la siguiente forma:

valor = "Eduardo"
print(valor)

valor = 2
print(valor)

valor = 3.1
print(valor)

valor = True
print(valor) 

IMPORTANTE: Esto es tipado dinamico, es una caracteristica propia de Python que nos permite agilizar procesos de desarrollo pero si no seguimos un estandar de codificacion y tampoco nombramos de forma correcta nuestras variables haciendo que estas almacenen datos de manera indiscriminada no es buena idea, ya que podemos tener como resultado un codigo dificil de leer. Se recomienda siempre almacenar un mismo tipo de dato para nuestras variables, por ejemplo si creamos una variable que almacena un valor de tipo entero debemos procurar que en el resto del programa esa misma variable almacene valores de tipo entero. 

--------------------------------------------------
# 11) Clase 11- Operadores relacionales.

 Existen operadores relacionales y operadores logicos. 
En programacion tanto los operadores relacionales como los operadores logicos nos permiten obtener como resultado un valor booleano ya sea verdadero o falso, valor que posteriormente podemos utilizar para condicionar nuestro codigo.  

 Los operadores relacionales son los operadores que se encuentran disenados principalmente para comparar tipos de datos numericos, ya sean numeros enteros o numeros flotantes. Los operadores relacionales son 6: 

>  -> Mayor
<  -> Menor
>= -> Mayor igual
<= -> Menor igual
== -> Igual
!= -> Diferente

-> Al nosotros implementar estos operadores sobre numeros enteros, obtendremos como resultado numeros booleanos.  

Entonces recordar que los operadores relacionales nos permiten comparar tipos de datos numericos, ya sean numeros enteros o numeros flotantes. Al implementar operadores relacionales nos dara como resultado un valor booleano, los operadores relacionales nos "permiten" poder implementar condiciones sobre dos valores, la lectura siempre sera de izquierda a derecha y siempre condicionando sobre nuestro primer valor.

numero_uno = 10
numero_dos = 20

resulto = numero_uno > numero_dos
print(resulto)
-> False

resulto = numero_uno < numero_dos
print(resulto)
-> True

resulto = numero_dos == numero_uno
print(resulto)
-> False

--------------------------------------------------
# 12) Clase 12- Operadores logicos.

"""
Los operadores logicos son: and, or y not. 

Los operadores logicos nos permiten comparar tipos booleanos. Al implementar este tipo de operadores obtendremos como resultado un valor booleano, ya sea verdadero o falso.

and -> El operador logico and nos permite comparar valores booleanos, todas las comparaciones deben de ser verdaderas para que el resultado final sea verdadero, si una sola comparacion es falsa entonces el resultado final es falso. Podemos utilizar la N cantidad de operadores logicos que deseemos. 
"""

#and:
resultado_final = True and True
print(resultado_final)

#Usando varios operadores logicos:
resultado_final = True and True and True and True
print(resultado_final)

"""
NOTA: 
Al usar operadores logicos tambien podemos utilizar operadores relacionales
"""
#logicos y relacionales juntos:
resultado_final = True and True and 10 > 20
print(resultado_final)

"""
or -> Para el operador logico or por lo menos una de las comparaciones debe de ser verdadera para que el resultado final sea verdadero. 
"""
#or:
resultado_final = False or False or 100 > 20
print(resultado_final)

resultado_final = False or False or 10 > 50
print(resultado_final)

"""
Es importante mencionar que al nosotros utilizar parentesis es posible combinar los operadores logicos, en estos casos Python resuelve primero lo que esta dentro de los parentesis. 
"""
#combinando con parentesis:
resultado_final = True and (False or 5 > 10)
#dentro del parentesis es False.
print(resultado_final)

"""
not -> Este operador nos permite negar un valor booleano, convierte a True a False y viceversa. 

"""

#not: 
resultado_final = not True
print(resultado_final)

resultado_final = not False
print(resultado_final)


--------------------------------------------------
# 13) Clase 13- Conocer tipos de datos.

Si en un caso necesitamos conocer que tipo de dato almacena una variable, podemos hacerlo con la funcion type. 

NOTA: En el VSC la explicacion de esta clase esta en el archivo de tipado.py

#Ahora vamos a imprimir en consola el tipo de dato que esta almacenando en ese momento la variable, para ello usamos la funcion type. Debemos crear para cada una, una nueva variable que vamos a llamar tipo, y dentro de esta usamos la funcion type para que nos retorne el tipo de variable de valor, y para verlo en consola debemos imprimir tipo. Ejm:

valor = "Eduardo"
tipo = type(valor)
print(tipo)

valor = 2
tipo = type(valor)
print(tipo)

valor = 3.1
tipo = type(valor)
print(tipo)

valor = True
tipo = type(valor)
print(tipo)
  
"""
La funcion type recibe como argumento (lo que va dentro de los parentesis) la variable de la cual queremos conocer su tipo. Y la funcion va a retornar, va a regresar el tipo de dato que almacena la variable. 
Hacerlo de la manera anterior funciona perfectamente pero lo ideal siempre es escribir la menor cantidad de lineas de codigo y existe una manera que es la mas comun para conocer el tipo de dato. A continuacion:
"""
#forma directa: no creamos una nueva variable, imprimimos de manera directa el tipo de valor.
valor = "Eduardo"
print = (type(valor))

valor = 2
print(type(valor))

valor = 3.1
print(type(valor))

valor = True
print(type(valor))


--------------------------------------------------
# 14) Clase 14- Leer valores por teclado.


Hasta ahora todos los datos que hemos manejado los hemos colocado directamente en nuestro script, ahora vamos a aprender a trabajar con los valores de ENTRADA que pueden provenir de diferentes lugares, como: una base de datos, una API, un archivo o directamente de lo que el usuario ingreso via teclado. 
Aprenderemos a obtener valores que el usuario ha ingresado a traves de su teclado. 

-----------------------------
Glosario:
Que es un script?? -> Los scripts son fragmentos de código que tienen como objetivo realizar o añadir funciones dentro de una página web o e-commerce.
-----------------------------

Vamos a pedir al usuario que ingrese ciertos valores personales, comenzando con su nombre completo. Para esto haremos uso de la funcion input. Colocamos, input seguido de parentesis y dentro de los parentesis de forma opcional podemos colocar el mensaje que queremos que el usuario visualice (Este mensaje va dentro de comillas). Se recomienda siempre colocar el mensaje para darle mas contexto al usuario sobre que tipo de dato debe ingresar. Ejm:

input("Ingresa tu nombre completo: ")

-> Al momento de ejecutar se visualiza el mensaje y el cursor. La funcion input se encarga de pausar la ejecucion del programa, esto hasta que se presione enter, al presionar enter el programa se va a reanudar. 
La funcion input va a regresar, va a retornar todo lo que el usuario escribio hasta que se presiono enter.

Este valor que obtenemos por medio de input podemos almacenarlo en una variable. Por ejemplo:

nombre_completo = input("Ingrese tu nombre completo: ")

-> Ejecuto el archivo y el usuario coloca sus datos, en teoria el programa ejecuta y guarda el dato. Para visualizar esos datos debo usar print. Ejm:

nombre_completo = input("Ingrese tu nombre completo: ")

print(nombre_completo)

IMPORTANTE: La funcion input SIEMPRE va a retornar un tipo de dato string, es decir una cadena de caracteres. 
Podemos comprobarlo facilmente con la funcion type. Imprimiendo en consola el tipo de dato de la variable. Ejm:

nombre_completo = input("Ingrese tu nombre completo: ")

print(nombre_completo)

print(type(nombre_completo))


--------------------------------------------------
# 15) Clase 15- Convertir tipos de datos.

Ya sabemos como obtener los datos que el usuario haya ingresado via teclado por medio de la funcion input, esta funcion siempre va a retornar un tipo de dato string. 
 Pero, que pasa si nosotros queremos trabajar con distintos tipos de datos, como enteros flotantes, booleanos, etc.
En estos casos debemos crear nuevos valores a partir de el string. Vamos a pedir al usuario que ingrese su edad, que obviamente debe estar reflejado por medio de un numero entero. Ejm:

edad = input("Ingresa tu edad: ")
print(edad)
print(type(edad))

-> Al hacer la ejecucion me devuelve un string, entonces debemos crear un numero entero a partir de este string. 

Para crear un numero entero a partir de un string debemos apoyarnos en la funcion: int()

int() -> Funcion que nos permite crear un entero a partir de un string. Debemos colocar entre los parentesis el string a partir del cual nosotros queremos generar el numero entero. La funcion int va a retornar dicho numero entero. Ejm:

edad = input("Ingresa tu edad: ")
edad = int(edad)

print(edad)
print(type(edad))

-> Nos devuelve un valor entero. 

---------------------------------
 Ahora, que pasa si queremos trabajar con valores flotantes?? 
Vamos a trabajar con la funcion float, la funcion float nos permite crear un nuevo flotante a partir de un string, basta con que coloquemos como argumento dentro de los parentesis el string a partir del cual nosotros queremos crear el flotante. Esta funcion va a retornar el valor generado. Ejm:

altura = input("Ingresa tu altura: ")
altura = float(altura)

print(altura)
print(type(altura))

----------------------------------
 Ahora vamos a obtener un tipo booleando a partir de lo que el usuario ingreso a partir del teclado. Por ejemplo, defino la variable autorizacion:

autorizacion = input("Autorizas el programa? (si/no)") -> Creamos la variable en donde le preguntamos al usuario si autoriza el programa y le dejamos dos opciones al usuario. 

 Nosotros deseamos que la variable autorizacion almacene un valor booleano verdadero o falso, todo depende de lo que el usuario haya ingresado, ya sea si o no. Y como sabemos, si nosotros utilizamos un operador relacional podremos obtener como resultado un valor booleano. Ejm:
autorizacion = autorizacion == "si" -> Aqui dice: autorizacion es igual a si, si es asi entonces autorizacion sera verdadero, en caso contrario sera falso. 

ejm completo:

autorizacion = input("Autorizas el programa? (si/no)")
autorizacion = autorizacion == "si"

print(autorizacion)

-> Nosotros comparamos utilizando el operador relacional ==, si lo que el usuario regreso es igual a si entonces autorizacion es True. 

autorizacion = input("Autorizas el programa? (si/no)")
autorizacion = autorizacion == "si"

print(autorizacion)

"""
#-------------------------
#resumen:

nombre_completo = input("Ingresa tu nombre completo: ")

edad = input("Ingresa tu edad: ")
edad = int(edad)

altura = input("Ingresa tu altura: ")
altura = float(altura)

autorizacion = input("Autorizas el programa? (si/no)")
autorizacion = autorizacion == "si"

print(autorizacion)

#Podemos reducir las lineas de codigo de la siguiente manera, ejecutando las funciones int y float directamente donde las necesitemos y en el booleano podemos implementar el operador relacional directamente en la primera linea:

nombre_completo = input("Ingresa tu nombre completo: ")

edad = int(input("Ingresa tu edad: "))


altura = float(input("Ingresa tu altura: "))


autorizacion = input("Autorizas el programa? (si/no)") == "si"

print(nombre_completo)
print(edad)
print(altura)
print(autorizacion)

OJO: REPASAR BOOLEANO, TENGO DUDA. 


--------------------------------------------------
# 16) Clase 16- Crear multiples variables. 

Vamos a crear variables en una sola linea de codigo: 

nombre = "Eduardo"
apellido = "Garcia"
titulo = "Mr."

print(nombre)
print(apellido)
print(titulo)

Puedo poner esas tres variables en una sola linea:

nombre, apellido, titulo = "Eduardo", "Garcia", "Mr."
 
print(nombre)
print(apellido)
print(titulo)

IMPORTANTE:

En python la legibilidad cuenta, esto quiere decir que siempre que utilicemos esta forma para crear variables intentemos no crear muchas variables en una misma linea de codigo maximo 4, y ademas hacerlo cuando las variables tengan un  mismo contexto, que se encuentren relacionadas. 


# ----------->MODULO_2->LISTAS



# 1) Clase 1- Que son las listas???
-> Las listas en python son concretamente una estructura de datos, es decir, es un tipo de dato que nos permite manejar grandes cantidades de otros datos. Ejm: Vamos a crear nuestra primera lista. 

Tenemos dos maneras de crear listas.

LA PRIMERA OPCION:

- Creamos el nombre de nuestra variable seguida del igual y despues colocamos la funcion list(), ejm:

lista = list() -> De esta forma le indicamos a python que la variable sera una lista. 

LA SEGUNDA OPCION, es trabajar con corchetes:

lista = [] -> De esta forma le indicamos a python que la variable sera una lista. 


 Nuestras listas nos permiten almacenar otros tipos de datos, ya sean strings, enteros, flotantes, booleanos, listas, tuplas, diccionarios, etc. Y para ello al momento de crear una lista podemos colocar dentro de los corchetes todos aquellos elementos los cuales queramos se almacenen dentro de la lista. Ejm:

lista = ["String", 10, 15.6, True]
print(lista)
-> Al imprimir en consola, visualizo cada uno de los elementos dentro del listado. 

IMPORTANTE: A cada uno de los elementos dentro de la lista, obligatoriamente le corresponde un indice dentro de la lista, es decir una posicion y los indices en python comienzan en 0. Ejm:

            0       1    2     3
lista = ["String", 10, 15.6, True]


 Si bien es cierto que las listas nos permiten mezclar los elementos a almacenar, por ejemplo strings con enteros, con flotantes, con booleanos, con listas, con tuplas, con diccionarios, etc. Lo aconsejable es que siempre que podamos creemos listas que almacenen un solo tipo de valor, listas de solo strings, listas de solo enteros, o flotantes o booleanos; de esta forma vamos a evitar posibles errores a la hora de ejecutar nuestro codigo y estaremos estandarizando nuestro codigo a la hora de codificar. Ejm:

lista_strings = ["Eduardo", "Codigo", "Curso Python"]

lista_enteros = [-19, 0, 10, 200]

lista_floats = [19.5, -20.5, 80.99, 100.00]

lista_booleanos = [True, True, (2 < 10), (4>3 and 10 != 11)]


--------------------------------------------------

# 2) Clase 2- Listas.


 Todos los valores almacenados dentro de una lista, les correspondera obligatoriamente una posicion en la misma, a esta posicion la conoceremos como indice y mediante un indice seremos capaces tanto de obtener como actualizar elementos dentro de la lista. 

 Vamos a trabajar con la siguiente variable que es un listado de strings. Vamos a obtener cada uno de estos elementos mediantes sus indices. 

lista_cursos = ["Python", "Django", "Flask", "Ruby", "Java"]

#Vamos a obtener el primer curso del listado. 
primer_curso = lista_cursos[0]
print(primer_curso)
-> En consola aparece: Python

segundo_curso = lista_cursos[1]
print(segundo_curso)

ultimo_curso = lista_cursos[4]
print(ultimo_curso)

-> Nosotros vamos a obtener los elementos con respecto a sus indices.

 Tambien podemos trabajar los indices mediante numero negativos. Por ejemplo lo que en el ejemplo anterior corresponde al indice 4, si lo trabajamos en negativos corresponderia al indice -1. Por default nosotros vamos a leer las listas de izquierda a derecha sin embargo si nosotros trabajamos con numeros negativos entonces la lista la vamos a leer de derecha a izquierda. 

                  -5        -4        -3       -2       -1
lista_cursos = ["Python", "Django", "Flask", "Ruby", "Java"]

ultimo_curso = lista_cursos[-1]
print(ultimo_curso)

Lo recomendable siempre es trabajar con numero positivos, exceptuando cuando necesitemos trabajar con el ultimo elemento, el penultimo o el antepenultimo. 


--------------------------------------------------

# 3) Clase 3- Actualizar elementos. 

 Si deseamos actualizar un elementos dentro del listado, podemos hacerlo. Nos estaremos apoyando mediante indices. Ejm: Vamos a actualizar el ultimo elemento del listado, remplazaremos Java por Rust. 

lista_cursos = ["Python", "Django", "Flask", "Ruby", "Java"]

-> Colocamos nuestro listado (la variable), abrimos corchetes y dentro de los corchetes ponemos el indice el cual nosotros queremos reemplazar, seguido del igual con el nuevo valor. 

lista_cursos[4] = "Rust"
print(lista_cursos)

-> Verificamos en consola y ya aparece el nuevo valor.

 Podemos modificar cualquier indice dentro de la lista.  


RECORDEMOS, mediante los indices seremos capaces tanto de obtener como de actualizar elementos dentro del listado. Y los indices siempre van a comenzar en 0. Una lista es dinamica, puede aumentar o decrecer su tamano en tiempo de ejecucion y seremos capaces de actualizar elementos dentro del listado en tiempo de ejecucion. 

--------------------------------------------------

# 4) Clase 4- Sublistas

Trabajando con listas en Python tenemos la posibilidad de generar sublistas. 
 Ejm: Vamos a generar una sublista que comprenda los primeros tres elementos de la siguiente lista.

lista_cursos = ["Python", "Django", "Flask", "Ruby", "Java", "Rust"] 

Pasos: Creamos una nueva variable (sub_lista) que sera igual a lista_cursos (nombre de la lista original), seguido de corchetes y dentro de los corchetes separado por dos puntos vamos a colocar el indice inicial y el indice final a partir de los cuales vamos a generar nuestra sublista. Ejm:

sub_lista = lista_cursos[0:3]
print(sub_lista)
-> En consola aparece: Python, Django y Flask. El indice final no es tomado en cuenta. 


De esta forma, al nosotros indicar un indice inicial : y un indice final, podremos crear sublistas en Python. 

[start:end] -> El indice que pondremos como indice final no es tomado en cuenta. 


- Que pasa si nosotros colocamos un indice final que no exista en la lista??? Ejm:

sub_lista = lista_cursos[1:100]
print(sub_lista)
-> NO hay ningun tipo de error, y la sublista tendra como resultado 5 elementos, los que van desde el indice uno hasta el final.  
Esto es lo que va pasar cuando trabajemos con indices que no se encuentren en la lista, Python lo que hara sera tomar todos los elementos a partir del indice inicial y con ellos va a generar una sublista. 


- Si nosotros queremos obtener los ultimos elementos de la lista, lo que nosotros podemos hacer es omitir el indice final, ejm: 

sub_lista = lista_cursos[1:]
print(sub_lista)
-> Se imprimen los ultimos elementos a partir del indice 1. 

- Si nosotros queremos obtener los primeros elementos de la lista, lo que podemos hacer es omitir el indice inicial y unicamente hacemos alusion al indice final, donde se supone que vamos a finalizar la sublista. Ejm: 

sub_lista = lista_cursos[:4]
print(sub_lista)
-> Se crea una sublista con los primero 4 elementos de la lista, recordando que el indice final (el 4) no sera tomado en cuenta. 

- Podemos generar una sublista a partir de saltos, utilizando tres valores. Ejm: [1:5:2] -> El tercer valor indica los saltos a partir de los cuales se va a generar la lista. 

lista_cursos = ["Python", "Django", "Flask", "Ruby", "Java", "Rust"] 

sub_lista = lista_cursos[1:5:2]
print(sub_lista)
-> Se obtiene: Django, Ruby. Un elemento si y otro no. 

Resumen:

[star:end] 
[star:] -> Obtenemos los ultimos elementos de la lista.
[:end] -> Obtenemos los primero elementos de la lista
[start:end:skip] -> Indicamos la cantidad de saltos.


 Con esto ya seremos capaces de generar sublistas a partir de indices. 

 Ninguno de los valores a colocar son obligatorios, pueden ser opcionales, ejm:
[:] -> Vamos a generar una sublista con todos los elementos de la lista original. 
[::2] -> Vamos a generar una sublista con saltos de 2 en 2.
[::-1] -> Vamos a hacer saltos de forma inversa y el resultado sera nuestra lista pero invertida. 


--------------------------------------------------

# 5) Clase 5- Modificar listas. 

 Vamos a aprender a modificar las listas, ya sea anadiendo o quitando elementos de ellas. Apoyandonos en un par de metodos. 


lista_cursos = ["Python", "Django", "Flask", "Ruby", "Java", "Rust"]

-> Vamos a anadir un par de nuevos cursos a traves del elemento app-end, este metodo nos permite anadir nuevos elementos al final de nuestra lista. Ejecucion:

lista_cursos.append("")

-> Por medio de este metodo podemos anadir cualquier tipo de objeto, podemos anadir enteros, flotantes, booleanos, strings, listas, tuplas, diccionarios, etc. Pero lo recomendable es siempre almacenar el mismo tipo de objeto.

lista_cursos = ["Python", "Django", "Flask", "Ruby", "Java", "Rust"]

lista_cursos.append("")

print(lista_cursos)

-> Se anade el elemento nuevo al final de la lista:
['Python', 'Django', 'Flask', 'Ruby', 'Java', 'Rust', 'MongoDB']

.append() -> Nos permite anadir nuevos elementos a nuestra lista, estos elementos se van a posicionar al final de ella. 




COMO PODEMOS CONOCER LA LONGITUD DE UNA LISTA???
-> Podemos conocer LA LONGITUD DE UNA LISTA por medio de la funcion len. Ejm:

lista_cursos = ["Python", "Django", "Flask", "Ruby", "Java", "Rust"]

print(len(lista_cursos))




COMO PODEMOS ANADIR UN ELEMENTO EN UN INDICE EN PARTICULAR???
-> Haremos uso del metodo insert. Este metodo nos permite anadir un elemento a la lista a partir de un  indice en concreto. Este metodo recibe dos argumentos separados por una coma, el primer valor hace referencia al indice donde nosotros deseamos anadir el nuevo elemento y el segundo valor hace referencia al elemento que nosotros queramos almacenar-anadir. Ejm: 

lista_cursos = ["Python", "Django", "Flask", "Ruby", "Java", "Rust"]

lista_cursos.insert(1, "Rails") -> Quiero anadir Rails a la lista en el indice numero 1. 

Cuando ejecuto, en consola: 

lista_cursos = ["Python", "Rails", "Django", "Flask", "Ruby", "Java", "Rust"]




AHORA VAMOS A EXTENDER NUESTRA LISTA, Nosotros podemos hacer mas grande nuestra lista a partir de otra. 

lista_cursos = ["Python", "Django", "Flask", "Ruby", "Java", "Rust" ]
Lista_cursos_2 = ["C", "C++", "Docker"]

-> Mi segunda lista posee solo tres elementos, si yo quisiera que estos tres elementos se encontraran en la primera lista podemos hacer uso de la funcion extend. Colocamos la lista a la cual queremos anadir los nuevos elementos seguido de .extend() y dentro de los parentesis colocamos la segunda lista. 
Ejm: 

lista_cursos.extend(lista_cursos_2) -> Vamos a anadir todos los elementos de la segunda lista a la primera SIN AFECTAR a la segunda lista. La segunda lista seguira existiendo de manera normal. 

lista_cursos = ["Python", "Django", "Flask", "Ruby", "Java", "Rust" ]
Lista_cursos_2 = ["C", "C++", "Docker"]

lista_cursos.extend(lista_cursos_2)

print(lista_cursos)
print(lista_cursos_2)

En consola: 

['Python', 'Django', 'Flask', 'Ruby', 'Java', 'Rust', 'C', 'C++', 'Docker']
['C', 'C++', 'Docker']

--> Las dos listas, la primera con los nuevos valores y la segunda intacta. 





AHORA VAMOS A ELIMINAR ELEMENTOS DENTRO DE LA LISTA. Existen dos formas para eliminar elementos, LA PRIMERA: 

La primera forma para eliminar elementos de la lista, nos apoyamos del metodo remove. Este metodo recibe como argumento el elemento que nosotros queramos eliminar. Ejm: lista_cursos.remove("Java").

lista_cursos = ["Python", "Django", "Flask", "Ruby", "Java", "Rust" ]

print(lista_cursos) -> Aqui visualizamos el elementos "Java"

lista_cursos.remove("Java")

print(lista_cursos) -> Aqui ya removimos el elemento "Java"


LA SEGUNDA FORMA con la que tambien podemos ELIMINAR ELEMENTOS por medio de la palabra reservada del y usando su indice, ejm: 

del lista_cursos[0] -> Estamos eliminando el elemento que se encuentra en el indice 0 de la lista_cursos. 

lista_cursos = ["Python", "Django", "Flask", "Ruby", "Java", "Rust" ]

print(lista_cursos)

del lista_cursos[0]

print(lista_cursos)




UNA FORMA EN LA QUE PODEMOS ELIMINAR TODOS LOS ELEMENTOS DE UNA LISTA. Es por medio del metodo clear.
Este elemento se va a encargar de eliminar todos los elementos almacenados dentro de la lista, seria como reiniciar nuestra lista. 

lista_cursos = ["Python", "Django", "Flask", "Ruby", "Java", "Rust" ]

print(lista_cursos)

lista_cursos.clear()

print(lista_cursos)




--------------------------------------------------

# 6) Clase 6- Metodos de listas. 

 Vamos a trabajar con algunas operaciones comunes que podemos hacer utilizando listas. 
 
 Cuando estamos trabajando con listas que posean un solo tipo de valor, ya sean: strings, enteros, flotantes, etc. Es posible que necesitemos ordenarlas, y en esos casos tenemos dos opciones: 

 LA PRIMERA opcion es implementar algun tipo de algoritmo de ordenamiento,por ejemplo burbuja, quitsort, etc. 

 LA SEGUNDA opcion, las mas sencilla es haciendo uso de la funcion sort. 

-> LA FUNCION SORT en Python nos permite ordenar nuestras listas de forma ascendente (de menor a mayor) Ejm: 

lista = [8, 90, 1, 5, 44, 132, 600, 3, 4]

lista.sort()

print(lista)

-> No muestra la lista de forma ordenada. 
[1, 3, 4, 5, 8, 44, 90, 132, 600]




 ORDENANDO DE FORMA DESCENDENTE. Para nosotros hacer el ordenamiento a la inversa, hacemos uso del parametro reverse dentro de los parentesis.
 Ejm: lista.sort(reverse=True) -> Con esto le indicamos a Python que deseamos que el ordenamiento se haga a la inversa, es decir de forma descendente (de mayor a menor) 

lista = [8, 90, 1, 5, 44, 132, 600, 3, 4]

lista.sort(reverse=True)

print(lista)




CONOCIENDO EL NUMERO MAYOR Y EL NUMERO MENOR DENTRO DE UNA LISTA. 

Queremos conocer el numero menor y el numero mayor que se encuentren dentro de esta lista:

lista = [8, 90, 1, 5, 44, 132, 600, 3, 4]

Podemos hacer lo siguiente: Podemos ordenar de forma ascendente y posteriormente vamos a acceder a los elementos mendiante sus indices. 

lista.sort() -> Estamos ordenando de forma ascendente mediante sus indices. 

print(lista[0]) -> Para obtener el menor numero
print(lista[-1]) -> Para obtener el mayor numero. Podemos tomarlo con su indice negativo o con el indice [8]
 

EXPLICACION: Estamos necesitando tomar de la lista el numero con menor valor y el numero con mayor valor. Para eso lo mas logico es ordenar la lista de manera ascendente y una vez que ya la tengamos ordenada tomamos el primer y el ultimo valor por medio de los indices que ocupan. 

lista = [8, 90, 1, 5, 44, 132, 600, 3, 4]

lista.sort()

print(lista[0])
print(lista[-1])

 En consola nos muestra el numero menor y el numero mayor. 

 Con este metodo podemos conocer el numero menor y el numero mayor de una lista, pero existen dos funciones que nos ayudan de manera mas corta a conocer el  numero menor y el numero mayor de una lista. 




FUNCIONES PARA CONOCER EL NUMERO MENOR Y EL NUMERO MAYOR DE UNA LISTA. 

-> Serian las funciones min - max. Dentro de los parentesis de la funcion ponemos la lista de la cual queremos conocer el numero menor o el numero mayor. 

lista = [8, 90, 1, 5, 44, 132, 600, 3, 4]

print(min(lista))
print(max(lista))

-> Este metodo nos permite conocer el menor y el mayor sin necesidad de trabajar con los indices ni ordernar.


------------------------------

PODEMOS SABER SI UN ELEMENTO SE ENCUENTRA O NO DENTRO DE NUESTRA LISTA. Haciendo uso de la palabra reservada in y del nombre de la lista, y el resultado de esa expresion dara un valor booleano, True o False. 

Ejm: Si deseo saber si 10 se encuentra dentro del listado.

10 in lista

lista = [8, 90, 1, 5, 44, 132, 600, 3, 4]

print(10 in lista)


SI QUEREMOS NEGAR LA SENTENCIA, por ejemplo si nosotros queremos confirmar que un elemento no esta dentro de la lista, hacemos uso del operador aritmetico not in. 


lista = [8, 90, 1, 5, 44, 132, 600, 3, 4]

print(11 not in lista)



--------------------------------------------------

# 7) Clase 7- Index.

 Una vez que nosotros confirmamos que un valor si se encuentra dentro de la lista, muy probablemente lo siguiente que nosotros querramos conocer sera su indice. Para ellos nos podremos apoyar del metodo Index. Este metodo recibe como argumento, el valor del cual queremos conocer su indice. 
Ejm: lista.index(5)-> Queremos conocer el indice de 5. El metodo index va a retornar el indice en el cual se encuentra el elemento.  


lista = [8, 90, 1, 5, 44, 132, 600, 3, 4]

print(5 in lista) ->Compruebo que se encuentra en lista.

index = lista.index(5) -> Guardo en una variable el indice de 5
print(index) 


IMPORTANTE, el metodo index va a retornar el primer indice encontrado. O sea, si en la lista tenemos varios elementos del mismo valor y ese elemento es el que necesitamos conocer nos va a dar el indice del primer elemento de ese tipo que consiga. Si intentamos conocer el indice de un elemento que no existe vamos a obtener un error, por esta razon es importante que siempre antes de obtener el indice de un elemento confirmemos que dicho elemento en efecto exista dentro del listado. 



-------------------------------------------------- 

# 8) Clase 8- Matrices. 


 En Python utilizando listas seremos capaces de trabajar con matrices de una forma muy facil, ya que utilizando listas seremos capaces de almacenar diferentes tipos de datos incluidas otras listas, con lo cual seremos capaces de generar matrices de n dimensiones. 

 Vamos a crear una matriz de 2 por 2, para ello voy a crear una lista la cual a su vez almacenara dos listas mas. Para ejemplificar esto voy a crear dos nuevas variables. 

columna_a = [10, 20]
columna_b = [30, 40]

-> Estas serian las columnas que conformarian mi matriz. Mediante estas dos columnas que almacenan dos elementos voy a crear una matriz de 2 por 2 (una matriz bidimensional). 

matriz = [columna_a, columna_b] -> La matriz sera una matriz 2 * 2 la cual posee 2 columnas que a su vez posee dos filas. 


print(matriz)

En consola: [[10, 20], [30, 40]] ->Visualizamos nuestra lista que a su vez almacena dos listas. 

 Si por lo menos nosotros quisieramos obtener el primer elemento, colocamo 0 en la posicion X, y 0 en la posicion Y. Ejm: 

print(matriz[0][0])

En consola: 10 -> Ya que seria el elemento que se encuentra en la esquina superior izquierda de la matriz. En el indice 0,0. 

print(matriz[1][0])
En consola:30


print(matriz[0][1])
En consola:20


print(matriz[1][1])
En consola:40

REPASA UN POCO MAS LAS MATRICES, LAS POSICIONES QUE OCUPAN CADA ELEMENTO. 



# ----------->MODULO_3->TUPLAS

# 1) Clase 1- Que son las tuplas?

 Las tuplas son muy parecidas a las listas, las tuplas nos permiten almacenar diferentes tipos de datos, como: strings, enteros, flotantes, booleanos, listas, tuplas, etc.

 La principal diferencia entre las listas y las tuplas es que las tuplas son inmutables, es decir una vez que nosotros definamos una tupla, asi se quedara por el resto del programa. Nosotros no seremos capaces de modificar los elementos almacenados dentro de una tupla ni tampoco la longitud de una tupla (no podremos anadir ni quitar elementos). Una vez que creamos una tupla no podremos cambiarla, siempre podemos consultarla pero no modificarla. 

 Como crear una tupla???

-> Colocamos el nombre de nuestra variable, luego para indicarle a Python que esta variable sera de tipo tupla haremos uso de parentesis. Ejm:

tupla = () 

print(tupla)
En consola: ()

print(type(tupla))
En consola: <class 'tuple'>


 Lo comun es que siempre que creemos una tupla, al definir dicha variable, coloquemos los elementos que queremos almacenar dentro de los parentesis, separados por una coma (,).  Al igual que con las listas, las tuplas nos permiten almacenar diferentes tipos de datos en una misma tupla, puede ser una string, un entero, un flotante, un booleano y hasta una misma lista, etc. Ejm: 

tupla = ("String", 10, 15.4, True, [1, 2, 3])

-> En este caso mi tupla almacena 5 elementos. 

print(tupla)
En consola: ('String', 10, 15.4, True, [1, 2, 3])


 Y las tuplas tambien nos permiten almacenar otras tuplas, ejm: 

tupla = ("String", 10, 15.4, True, [1, 2, 3], (4, 5, 6))

-> El ultimo elemento dentro de esta tupla es otra tupla. 


 Cada uno de los elementos de la tupla le corresponde un indice, una posicion dentro de la tupla. Y los indices comienzan en cero (0). 

 LA PRINCIPAL VENTAJA de utilizar las tuplas sobre listas, es que las tuplas son mucho mas rapidas en cuanto a obtener elementos se refiere. Ya que al ser estas objetos inmutables, Python las almacena en un espacio de memoria especial para objetos de lectura. En cambio a las listas por ser cambiantes las almacena en un espacio de lectura y escritura. 


----------------------------------------------------------------------------------------------
# 2) CLASE 2- INDICES DE TUPLAS.

 Al igual que con las listas, con las tuplas trabajaremos mediante indices, esto para obtener los valores almacenados. 


             0         1        2         3             
cursos = ("Python", "Flask", "Django", "Rails", 
    4
"MongoDB")


 Si nosotros queremos obtener algun elemento de la tupla, lo haremos a traves de indices. Ejm:


primer_curso = cursos[0]

print(primer_curso)
En consola: Python.


 Tambien podemos utilizar valores negativos, por ejemplo el -1 para MongoDB. 


 Con las tuplas seremos capaces de generar subtuplas. Por ejemplo si nosotros queremos crear una subtupla a partir de los primeros tres elementos de la tupla, podemos hacer lo siguiente. 

sub_tupla = cursos[0:3]

print(sub_tupla)
En consola: ('Python', 'Flask', 'Django')

 En la creacion de subtuplas aplican las mismas condiciones que en la creacion de las sublistas. 


---------------------------------------------------------------------------------------------- 
# 3) CLASE 3- LISTAS Y TUPLAS. 


 Sabemos que una variable es de tipo lista si al momento de definirla utilizamos corchetes []. Por otro lado sabemos que una variables es de tipo tupla si al momento de definirla utilizamos parentesis ().

 El uso de estas estructuras tienen sus pros y contras. Habran ocasiones en las que tengamos que utilizar listas o tuplas, todo va a depender de nuestras necesidades.  

 Cuando nosotros no sepamos la cantidad de elementos que tenemos que almacenar y/o sepamos que estos elementos pueden variar, ya sea que modifiquen su valor, incrementen o decrezcan en cantidad, haremos usos de listas. 

 Si por el contrario sabremos que los elementos a almacenar no cambiaran y queremos que se mantengan asi durante el resto del programa, haremos uso de tuplas. 


AHORA, que pasa si en dado caso en tiempo de ejecucion debemos generar LISTAS A PARTIR DE TUPLAS O VICERVERSA????

R: Para esos casos haremos uso de las funciones lista o tupla. 

Ejm:  

cursos = ["Python", "Django", "Flask"]

niveles = ("Basico", "Intermedio", "Avanzado")


cursos = ["Python", "Django", "Flask"]

1- Vamos a generar una tupla a partir de nuestra lista:
-> Usamos la funcion tuple() y como parametro colocamos la lista a partir de la cual queremos generar nuestra tupla. Ejm: 

tuple(cursos) -> La funcion tupla va a generar una tupla a partir de la lista. 

-> La tupla generada la podemos almacenar en una variable, ejm: 

cursos_tupla = tuple(cursos)

cursos_tupla = (type(cursos_tupla))

print(cursos_tupla)
En consola: ('Python', 'Django', 'Flask')
<class 'tuple'> -> Visualizamos en consola un objeto de tipo tupla. 



niveles = ("Basico", "Intermedio", "Avanzado")

2- Ahora si queremos generar una lista a partir de una tupla:
-> Hacemos uso de la funcion list() y como argumento dentro de los parentesis vamos a colocar la tupla a partir de la cual vamos a generar la lista. 

niveles_lista = list(niveles)

print(niveles_lista)

print(type(niveles_lista))
En consola: ['Basico', 'Intermedio', 'Avanzado']
<class 'list'>



---------------------------------------------------------------------------------------------- 
# 4) CLASE 4- DESEMPAQUETADO - DESCOMPRIMIR.

 Nosotros podemos definir multiples variables y asignarles sus correspondientes valores en una sola linea de codigo. Ejm: 

uno, dos, tres, cuatro = 1, 2, 3, 4

print(uno)
print(dos) 
print(tres)
print(cuatro)

En consola: 
1
2
3
4

 Nosotros podemos hacer exactamente lo mismo pero utilizando tuplas. Ejm: 

numeros = (1, 2, 3, 4)

uno, dos, tres, cuatro = numeros => Asigno a esta variable la tupla. 

print(uno)
print(dos) 
print(tres)
print(cuatro)

En consola: 
1
2
3
4

Al nosotros hacer esto, Python va a asignar cada uno de los valores de la tupla a cada una de las variables. El primer valor a la primer variable, el segundo valor a la segunda variable y asi sucesivamente. 


 Que pasa si no conocemos de antemano la cantidad de elementos que posee nuestra tupla??? Ejm, que posea 6 elementos y unicamente estamos asignando 5 variables.  
-> Al ejecutar obtendriamos un error, donde se nos indica que existen demasiados valores para desempaquetar. 

 Para solucinarlo podemos hacer lo siguiente: 
Colocamos un asterisco como prefijo a la ultima variable y en este caso le cambiamos el nombre a la misma, ejemplo: 

numeros = (1, 2, 3, 4, 5, 6)

uno, dos, tres, cuatro, *resto_valores = numeros 

 -> Al nosotros hacer esto le estamos indicando a python que a partir del cuarto valor el resto se va a almacenar en la variable resto valores. 

print(uno)
print(dos)
print(tres)
print(cuatro)
print(resto_valores)

En consola: 
1
2
3
4
[5, 6]

--> Visualizamos que la variable resto valores no es mas que una lista, donde son almacenados los valores que no fueron desempaquetados. Si existieran mas valores, seran almacenados en esta nueva lista y mostrados en consola.

 El asterisco es muy importante al nosotros trabajar con listas, ya que el mismo denota listas. Siempre que veamos un * como prefijo eso quiere decir que la variable es una lista. 

 
 SI NO QUEREMOS ALMACENAR EL RESTO EN UNA VARIABLE, lo que debemos hacer es colocar *_ . Ejm: 

numeros = (1, 2, 3, 4, 5, 6, 7)

uno, dos, tres, cuatro, *_ = numeros

print(uno)
print(dos)
print(tres)
print(cuatro)

En consola: 
1
2
3
4

-> De esta forma la estamos diciendo a Python que no quiero trabajar con el resto de valores, asi que no hay necesidad de crear una nueva variable.  

CONSEJO: Si nosotros no queremos trabajar con algun valor simplemente la omitamos, y no creemos variables las cuales posteriormente no vayamos a utilizar. 


 QUE PASA SI NOSOTROS QUEREMOS OMITIR LOS ELEMENTOS QUE SE ENCUENTREN DESPUES DEL INDICE 4 PERO QUEREMOS OBTENER LOS ULTIMOS 2 ELEMENTOS???
Queremos omitir: 5, 6, 7 y 8. Nos interesan del 1 al 4 y el 9 y el 10.

numeros = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

uno, dos, tres, cuatro, *_, nueve, diez = numeros

-> Al hacer esto Python sabra que los ultimos dos elementos de la tupla si nos interesan, asi que los va a excluir de la lista que estamos omitiendo.

print(uno)
print(dos)
print(tres)
print(cuatro)
print(nueve)
print(diez)

En consola: 
1
2
3
4
9
10


 AHORA OBTENGAMOS UNICAMENTE EL 1, 3, 4, 9, 10.
ESTAMOS OMITIENDO EL 2. 

numeros = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

uno, _, tres, cuatro, *_, nueve, diez = numeros

-> Colocamos un guion bajo en el numero dos, con esto le estamos indicando a Python que el segundo elemento que se encuentra en el indice uno, no nos interesa. 

print(uno)
print(tres)
print(cuatro)
print(nueve)
print(diez)

En consola:
1
3
4
9
10

* -> Lista
_ -> Omitir valor


 El tema del desempaquetado es muy importante ya que a partir de la combinacion que nosotros utilicemos (variable, _, *_, *) sera como Python va a obtener los elementos y los va a asignar a nuevas variables. 



--------------------------------------------------------------------------------------------------------------
# 5) CLASE 5- ZIP - COMPRIMIR

 Vamos a aprender a como comprimir elementos para generar tuplas. Utilizando la funcion zip. 

Con la funcion zip combinaremos los valores de la tupla y de la lista a continuacion, y ese valor lo guardaremos en una variable. Pasamos como argumento (parametro) los valores que nosotros queremos comprimir. 

lista = [1, 2, 3, 4, 5]

tupla = (10, 20, 30, 40, 50)

resultado = zip(tupla, lista)

print(resultado)
En consola: <zip object at 0x000001EBA0D62940>

-> Esta funcion zip nos va a retornar un objeto, un tipo de dato de tipo zip. 
 Si nosotros quisieramos finalmente generar una tupla, entonces podemos convertir este objeto, este tipo a una tupla utilizando la funcion tuple(). Ejm: 

lista = [1, 2, 3, 4, 5]

tupla = (10, 20, 30, 40, 50)

resultado = zip(tupla, lista)
resultado = tuple(resultado)

print(resultado)
En consola: ((10, 1), (20, 2), (30, 3), (40, 4), (50, 5))
--> Visualizamos una tupla que a su vez almacena subtuplas. Cada una de estas subtuplas es la combinacion de nuestra lista y nuestra tupla. 

 El orden afecta, si yo colocara en vez de zip(tupla, lista) , colocara zip(lista, tupla) el resultado seria: ((1, 10), (2, 20), (3, 30), (4, 40), (5, 50))

-> Entonces, a partir del objeto zip generamos una tupla. Con la funcion zip seremos capaces de comprimir elementos para nosotros generar una nueva tupla. 


 TAMBIEN, podriamos utilizar solo listas o solo tuplas. Ejm: 

lista = [1, 2, 3, 4, 5]

tupla = (10, 20, 30, 40, 50)

lista_2 = [100, 200, 300, 400, 500]

resultado = zip(lista, tupla, lista_2)
resultado = tuple(resultado)

print(resultado)
En consola: ((10, 1, 100), (20, 2, 200), (30, 3, 300), (40, 4, 400), (50, 5, 500))

-> Esto nos indica que las tuplas ahora van a poseer tres valores. Podemos colocar la N cantidad de listas o tuplas para la funcion zip. Dependiendo de la cantidad de listas o tuplas, dependiendo de la cantidad de argumentos, sera la cantidad de valores que encontraremos en nuestras tuplas. 

Tambien podria en vez de usar la funcion tuple() usar la funcion list(), pero lo aconsejable es SIEMPRE trabajar con tuplas utilizando ZIP. 


 QUE PASA SI ALGUNA DE ESTAS ESTRUCTURAS NO POSEE LA MISMA CANTIDAD DE ELEMENTOS QUE OTRAS???
Ejm:

lista = [1, 2, 3, 4, 5, 6, 7]

tupla = (10, 20, 30, 40, 50)

lista_2 = [100, 200, 300, 400, 500]

tupla_2 = (1000, 2000, 3000, 4000, 5000)

resultado = zip(lista, tupla, lista_2)
resultado = tuple(resultado)

print(resultado)
En consola: ((10, 1, 100, 1000), (20, 2, 200, 2000), (30, 3, 300, 3000), (40, 4, 400, 4000), (50, 5, 500, 5000))

--> Lo que pasa es que los elementos restante simplemente no son tomados en cuenta para generar las tuplas, ya que la combinacion debe ser exacta. Entonces si alguna estructura posee elementos de mas, estos son omitidos. Las tuplas siempre va a tener la misma longitud.  




# ----------->MODULO_4->STRINGS

# 1) CLASE 1- STRINGS CON LISTADOS. 

 Vamos a trabajar con los metodos mas utilizados al momento de utilizar strings, no son lo unicos metodos pero si los "mas usados". 

 Metodo split y metodo join. 

 Metodo split -> Nos permite generar una lista a partir de un string. 
 
 Metodo join -> Nos permite generar un string a partir de una lista. 


METODO SPLIT:


 EJEMPLO METODO SPLIT: Tenemos una variable que contiene un string con varios lenguajes de programacion separados por espacios. 

lenguaje = "Python Ruby Java Rust C++ C" 
 
Vamos a crear una lista a partir de este string con el metodo split, que me va a generar y retornar un nuevo listado, que estaremos almacenando en una nueva variable: 

listado_lenguajes = lenguajes.split()

print(listado_lenguajes)
En consola: ['Python', 'Ruby', 'Java', 'Rust', 'C++', 'C']

IMPORTANTE: El metodo split va a dividir el texto del string utilizando espacios, cada espacio denota un nuevo elemento dentro del listado. Pero si nosotros necesitamos dividir el string ya no por espacios sino por otros caracteres, lo que debo hacer es pasar el caracter o los caracteres a partir de los cuales deseo dividir el string, ejm:

lenguaje = "Python-Ruby-Java-Rust-C++-C" 

listado_lenguajes = lenguajes.split("-")

print(listado_lenguajes)
En consola: ['Python', 'Ruby', 'Java', 'Rust', 'C++', 'C']

o

lenguaje = "Python//Ruby//Java//Rust//C++//C" 

listado_lenguajes = lenguajes.split("//")

print(listado_lenguajes)
En consola: ['Python', 'Ruby', 'Java', 'Rust', 'C++', 'C']

-> Podrimos utilizar cualquier caracter o grupo de caracteres. 

 El metodo split por default va a dividir utilizando espacios, sin embargo si nosotros quisieramos dividir utilizando otros caracteres entonces basta con colocar como argumento dichos caracteres. 
 El metodo split va a dividir el string a partir de todas las coincidencias que se encuentren dentro del string, por ejemplo es este caso: 

lenguaje = "Python/-/*Ruby/-/*Java/-/*Rust/-/*C++/-/*C"

listado_lenguajes = lenguajes.split("/-/*")

=> En este caso se encuentran 5 coindicencias, las coincidencias son los valores que usamos para separar. 

 Si por ejemplo nosotros no quisieramos dividir por todas las coincidencias, quizas por un par, entonces debemos saber que el metodo split puede recibir un segundo valor. Ejm:

lenguaje = "Python/-/*Ruby/-/*Java/-/*Rust/-/*C++/-/*C"

listado_lenguajes = lenguaje.split("/-/*", 2)

print(listado_lenguajes)
En consola: ['Python', 'Ruby', 'Java/-/*Rust/-/*C++/-/*C']

--> Al nosotros hacer esto le estamos indicando a Python que ahora queremos crear una lista a partir del string pero unicamente dividiendo 2 veces. O sea, me divide el string en una lista de dos elementos. 



METODO JOIN -> Nos permite generar un string a partir de una lista. 

Tenemos el siguiente listado y a partir de el quiero tener un string. 

lenguajes = ["Python", "Ruby", "Java", "Rust"]

Colocamos un string a partir del cual nosotros queremos unir cada uno de los elementos dentro del listado, colocamos .join() y dentro de los parentesis vamos a colocar el listado a partir del cual queremos generar el string:

" " -> Estaria unido mediando un espacio. Dentro de este string podemos colocar un caracter o un grupo de caracteres.


string_lenguajes = " ".join(lenguajes) 

print(string_lenguajes)
En consola: Python Ruby Java Rust

-> Cada uno de los elementos dentro del listado ha sido unido para generar un nuevo string separado por un espacio. 

 Utilizando el metodo join seremos capaces de unir cada uno de los elementos dentro del listado mediante un caracter o grupo de caracteres. 

----------------------------------------------------------------------------------------------

# 2) CLASE 2- CONCATENAR PT1.

 Los string en Python son inmutables, una vez que nosotros definamos un string no podremos modificarlo en tiempo de ejecucion y asi se quedara por el resto del programa. Sin embargo habran ocasiones en donde voy a necesitar modificarlos pero no lo podre hacer, lo que si puedo hacer es generar nuevos strings a partir de otros, veamos: 

FORMA 1: MEDIANTE EL OPERADOR +.

nombre = "Eduardo Ismael"
apellido = "Garcia"

nombre_completo = nombre + " " + apellido

print(nombre_completo) 
En consola: Eduardo Ismael Garcia

 Podemos sumar lo N cantidad de string que nosotros deseemos. 
 La forma mas sensilla que nosotros podemos utilizar para concatenar strings (genearar un nuevo string a partir de otros) es simplemente utilizando el operador +.  

FORMA 2: UTILIZANDO %S

nombre = "Eduardo Ismael"
apellido = "Garcia"

Creo la nueva variable en donde ira el nuevo string, dentro de esta comienzo por crear un string base en donde debo poner los %s que van a corresponder a los valores que voy a concatenar. Despues de este string pongo %() y dentro de los parentesis los string que deseo concatenar.    

"Mr. %s %s." -> Debo colocar un string base y en este ejemplo seria este, este seria string base a partir del cual yo voy a crear un nuevo string. 


nombre_completo = "Mr. %s %s." %(nombre, apellido)

print(nombre_completo) 
En consola: Mr. Eduardo Ismael Garcia

 Los %s seran reemplazados dentro de los valores que coloquemos dentro de los parentesis. 
 Pudiesemos utilizar la N cantidad de valores y la N cantidad de %s, ejm: 

nombre_completo = "Mr. %s %s %s." %(nombre, apellido, "Perez") 

print(nombre_completo) 
En consola: Mr. Eduardo Ismael Garcia Perez.

----------------------------------------------------------------------------------------------

# 3) CLASE 3- CONCATENAR PT2.


nombre = "Eduardo Ismael"
apellido = "Garcia"


FORMA 3: METODO FORMAT.


nombre_completo = "Mr. {} {} {}.".format(nombre, apellido, "Perez")

-> Creo un string base y dentro de este pongo tantos placeholders (llaves) como strings que vaya a necesitar concatenar, luego ejecutamos el metodo format y como argumento los valores que vamos a utilizar para generar el nuevo string. 

print(nombre_completo) 
En consola: Mr. Eduardo Ismael Garcia Perez.

 Los placeholders seran reemplazados por los valores que se encuentren dentro de los parentesis, esto con respecto a su posicion.  


 Tambien pudiesemos nombrar a nuestros placeholders, ponerles nombres. Pero al momento de llamarlos necesitariamos utilizar parametros. Ejm:

nombre_completo = "Mr. {nombre} {primer_apellido} {segundo_apellido}.".format(
   nombre=nombre,
   primer_apellido=apellido,
   segundo_apellido="Perez"
)

print(nombre_completo) 
En consola: Mr. Eduardo Ismael Garcia Perez.

 Lo interesante de trabajar con nombres es que nosotros pudiesemos facilmente modificar el orden. Ejm:

nombre_completo = "Mr. {primer_apellido} {segundo_apellido} {nombre}.".format(
   nombre=nombre,
   primer_apellido=apellido,
   segundo_apellido="Perez"
)

print(nombre_completo) 
En consola: Mr. Garcia Perez Eduardo Ismael.

 
 Lo interesante de nombrar a los placeholders es que ahora los valores no se van a asignar con respecto a la posicion sino que lo haran con respecto a los nombres. 


--------------------------------------------------------------------------------------------------------------

# 4) CLASE 4- FString

 Los Fstring nos permiten generar nuevos string a partir de otros utilizando interpolacion. 

nombre = "Eduardo Ismael"
apellido = "Garcia"

nombre_completo = f'Mr. {nombre} {apellido} {"Perez"}'
 
 --> Hacemos uso de un string base pero debemos anteponer como prefijo el caracter f (Con el caracter f le indicamos a Python que ese string sera un fstring y dentro de el seremos capaces de utilizar interpolacion) dentro del string base van los juegos de llaves dentro de los cuales iran los valores que queremos utilizar dentro del string, pueden ser variables o directamente el valor, como en el caso de "Perez". En ejecucion me di cuenta que no puedo usar dos veces comillas dobles.   

print(nombre_completo)
En consola: Mr. Eduardo Ismael Garcia Perez

 Dentro del juego de llaves puedo colocar cualquier valor. Pueden ser numeros enteros, flotantes, booleanos, etc. Incluso operaciones matematicas. 


NOTA: DESDE EL PUNTO DE VISTA DEL PROFESOR LOS FSTRING SON LA FORMA MAS SENCILLAS CON LA QUE NOSOTROS PODEMOS GENERAR NUEVOS STRINGS, YA QUE LA LEGIBILIDAD JUEGA UN PAPEL MUY IMPORTANTE AL MOMENTO DE CODIFICAR NUESTRO PROGRAMA. EN LOS FSTRINGS PODEMOS COMPRENDER FACILMENTE QUE TIPO DE VALORES ESTAMOS UTILIZANDO PARA GENERAR NUESTRO STRING. 


--------------------------------------------------------------------------------------------------------------

# 5) CLASE 5- FUNCION PRINT.

 En los casos en donde yo creo una nueva variable unicamente para imprimir en consola su valor, se aconseja no crear esta nueva variable sino imprimir los valores directamente en consola con la funcion print. 

 LA FUNCION PRINT nos permite imprimir en consola diferentes valores. Lo interesante de esta funcion es que no esta limitada a imprimir un solo valor, sino que podemos imprimir la N cantidad de valores que deseemos. 
Ejm: 

nombre = "Eduardo Ismael"
apellido = "Garcia"

print(nombre, apellido, "Perez")
En consola: Eduardo Ismael Garcia Perez

-> Van a imprimir los valores pero los va a separar utilizando un espacio. 
 La funcion print se va a encargar de imprimir en consola TODOS los valores que nosotros coloquemos como argumentos, ya sean string, booleanos, listas, tuplas, etc. 


 POR DEFAULT la funcion print va a separar los valores mediante un espacio, sin embargo podemos separar los valores utilizando otros caracteres, utilizando el parametro sep seguido del caracter o caracteres que deseamos utilizar para separar los valores. Ejm: 


print(nombre, apellido, "Perez", sep=" ")-> por espacio
print(nombre, apellido, "Perez", sep="-")-> por guion
print(nombre, apellido, "Perez", sep="/")-> por slash


 Intentemos colocar el parametro sep al final de la funcion print. 

 Entonces siempre que nosotros queramos generar un string para que unicamente lo imprimamos en consola, entonces lo que podriamos hacer para no generar variables de forma innecesarias es simplemente imprimir en consola la union de los diferentes valores que queremos utilizar apoyandonos de la funcion print.
 OJO, la funcion print unicamente va a imprimir en consola, NO va a generar un nuevo string. Si por el contrario queremos generar un nuevo string para que se imprima en consola y posteriormente utilizarlo para otras operaciones, recuerda que podemos apoyarnos de la interpolacion, el metodo format, %s, +.  


--------------------------------------------------------------------------------------------------------------

# 6) CLASE 6- VALIDAR SUB STRINGS.


 Aprenderemos a buscar strings dentro de otros strings. 
Para ello existen diferentes formas de hacerlo, en este video estaremos trabajando con la siguiente variable: 

titulo_curso = "curso profesional de Python"


USANDO EL METODO COUNT: 

 Ahora, si nosotros deseamos conocer si el string Python existe o no dentro de string curso profesional de Python, pudiesemos hacer lo siguiente, nos podemos apoyar del metodo count, este metodo recibe como argumento un string, el string que nosotros queremos si existe o no dentro del string base. Ejm: 

titulo_curso = "curso profesional de Python"

titulo_curso.count("Python") -> El metodo count va a retornar la cantidad de coincidencias que se encuentren dentro del string, cuantas veces Python existe en titulo curso. 

titulo_curso = "curso profesional de Python"

contador = titulo_curso.count("Python")

print(contador)
En consola: 1

--> Con esto visualizamos que Python si existe dentro del string y se visualiza una sola vez. 

 Podemos usarlo para buscar palabras, letras o frases.  


USANDO EL METODO IN:

titulo_curso = "curso profesional de Python"

print("Python" in titulo_curso) -> Coloco el string a buscar seguido de palabra reservada in y despues el string base (el string a partir del cual podemos buscar). La palabra reservada in nos va a retornar un valor booleano. 


titulo_curso = "curso profesional de Python"

print("Python" in titulo_curso)
En consola: True

Recordar que para Python las minusculas y las mayusculas si importan, es case sensitive. Por lo tanto si busco segun el ejemplo la palabra Python en minuscula me va a retornar el valor False, por lo tanto para evitar este "error" lo que debo hacer es estandarizar el string ya sea convirtiendo todos sus caracteres a mayusculas o a minusculas con los metodos .lower o .upper segun la necesidad que tenga en su momento. Ejm:

print("python" in titulo_curso.lower()) 

-> Me muestra que Python en minusculas si existe dentro del string.

 Al agregar el metodo lower a titulo_curso, lo convierto todo a minusculas y busco en minusculas. 


 Tambien nosotros podemos negar, por ejem:

print("codigofacilito" not in titulo_curso.lower())
En consola: True, porque es verdad que no existe. 



 UTILIZANDO LOS METODOS STARTSWITH O ENDSWITH, podemos saber si un string comienza o no con otro string. Ejm:

print(titulo_curso.startswith("Curso")) ->Recibe como argumento el string del cual queremos conocer si se encuentra al inicio del string base y va a retornar un valor booleano. 


print(titulo_curso.endswith("Python")) -> Para saber si se encuentra al final. 



--------------------------------------------------------------------------------------------------------------

# 7) CLASE 7- JUSTIFICAR TEXTO 

 Algo interesante de los strings en Python es que nosotros podemos alinearlos-justificarlos utilizando metodos. 


mensaje = "Hola mundo!"

print(mensaje)

ljust -> Justificar a la izquierda
rjust -> Justificar a la derecha
center -> Centrar

 Los tres metodos no justifican al string original sino que a partir de el se genera uno nuevo. Ya que recordemos que los strings en Python son objetos inmutables. 


mensaje = "Hola mundo!"

mensaje = mensaje.ljust(20) -> Como argumento paso un numero entero que hace referencia a la cantidad de espacios que se van a anadir a la derecha del string. 

print(mensaje, ".")
En consola: Hola mundo!         .


mensaje = mensaje.rjust(20) -> Ahora los veinte caracteres son a la izquierda porque estoy alineando a la derecha.

print(mensaje)
En consola:          Hola mundo!



mensaje = mensaje.center(20) -> La cantidad de espacios que queremos utilizar para centrar el string. En este ejemplo, por poner 20, se anaden 10 espacios a la derecha y 10 espacios a la izquierda.  


# ---------------------->MODULO_5->DICCIONARIOS


# 1) CLASE 1- QUE SON LOS DICCIONARIOS????

 LOS DICCIONARIOS en Python al igual que las listas y las tuplas, nos permiten almacenar diferentes tipos de datos como: Strings, enteros, booleanos, flotantes, tuplas, listas e inclusive otros diccionarios. 			
 Los diccionarios son mutables, podemos modificar su longitud bien sean agregando o quitando elementos de el. De igual forma todos los valores almacenados en los diccionarios pueden ser modificados. 

 A diferencia de las listas y de las tuplas, los diccionarios no se rigen por la regla de los indices. Los valores que se almacenen dentro de un diccionario no corresponden a un indice sino a una llave. Todos los valores necesitan tener una llave y cada llave necesita tener un valor. 

 Algo interesante a tener en cuenta es que una llave puede ser cualquier tipo, cualquier objeto inmutable en Python, ya sea un string, un entero, un flotante, una tupla, etc. 

 Para definir un diccionario haremos uso de un juego de llaves o de la funcion dict(), ejm: 

diccionario = {}
diccionario = dict()

 Para poder almacenar un valor seguiremos la siguiente estructura: 
 { llave : el valor el cual queremos asociar. }

 diccionario = {"total": 55} -> Almacena el string total:55. Con esto le indico a Python que la llave total almacena 55.

 Si necesitamos almacenar nuevos valores, basta con separarlos mediante una coma. Ejm:

 diccionario = {"total": 55, "descuento": True, "subtotal": 15}

 Otro ejemplo: 

 diccionario = {"total":55, 10: "Curso de Python", (1,2,3): True}

-> En este ejemplo estamos almacenando 3 valores con sus correspondientes llaves, estas tres llaves son valores inmutables. Tenemos:

Un string ("total")
Un numero entero (10)
Una tupla que almacena numero enteros (1,2,3)

 Y estos a su vez almacena: 

55
"Curso de Python"
True

Correspondientemente. 



 Regularmente haremos uso de las llaves de un mismo tipo, comunmente string. Sin embargo si por algun motivo necesitas almacenar otro tipo de llave, puedes hacerlo. 

DATO INTERESANTE, podemos utilizar clases como llaves. 

*Si has trabajado con objetos JASON los diccionarios te seran muy familiare, ya que de hecho el equivalente a un JASON en Python es un diccionario. Podemos ver que este tipo de dato puede ser tan complejo como lo deseemos:

usuario = {
    "nombre": "Nombre del usuario",
    "edad": 23,
    "curso": "Curso de Python",
    "skills":{
        "programacion": True,
        "base_de_datos: False" 
    },
    "medallas": ["basico", "intermedio"]
}



 Para poder agregar, obtener o modificar algun valor dentro del diccionario haremos uso de corchetes. 

Creacion del diccionario:
diccionario = dict()

Agregar nueva llave valor:
diccionario["usuario"] = "eduardo"

Actualizar valor mediante una llave:
diccionario["usuario"] = "eduardo_gpg"

Obtener valor mediante una llave
print(diccionario["usuario"])


 Podemos obtener todas las llaves de nuestro diccionario utilizando el metodo keys(). 

 Podemos obtener todos los valores del diccionario usando el metodo values().
 
 Si queremos recorrer tanto las llaves como sus correspondientes valores haremos uso del metodo items().

>>> diccionario = {"Eduardo": 1, "Fernando": 2, "Uriel": 3, "Rafael": 4}

>>> diccionario.keys()
dict_keys(["Eduardo", "Fernando", "Uriel", "Rafael"])

>>> diccionario.values()
dict_values([1, 2, 3, 4])

>>> for key, value in diccionario.items():
        print(key, value)

Eduardo 1
Fernando 2
Uriel 3
Rafael 4


 Un metodo al que le podemos sacar mucho provecho es el metodo get. Este metodo nos permite obtener el valor de un diccionario con respecto a una llave, lo interesante de este metodo ocurre en caso de que la llave no exista, porque si por ejemplo intentamos acceder a una llave que no existe utilizando corchetes obtendremos un error, el error de key error. Pero con el metodo get seremos capaces de establecer un valor por default en dado caso la llave no exista y de esta forma podremos evitar el error. EJM:


usuario = {
    "name": "Eduardo Ismael",
    "age": 26,
    "job": "CodigoFacilito"
}

calificaciones = usuario.get("calificaciones", [])
if calificaciones:

    for calificacion in calificaciones:
        print(calificacion)
  

--> En este caso intentamos acceder a las calificaciones de un usuario, en particular este usuario no posee la llave calificaciones. Asi que mandamos una lista vacia para evitar el error, si esta lista esta vacia simplemente no recorremos e imprimimos los valores. 


 Al igual que con las listas es posible implementar el comprenhension utilizando diccionarios, en este caso seria dict comprenhension. Ejm:

usuarios = ["Eduardo", "Fernando", "Uriel", "Rafael"]
diccionario = { usuario:position + 1
                        for position, usuario in enumerate(usuarios) }

print(diccionario)  

--------------------------------------------------------------------------------------------------------------

# 2) CLASE 2- DICCIONARIOS

 Aprenderemos a anadir y a obtener elementos de un diccionario. 


 Vamos a crear un diccionario. Creamos una variable que tenga por nombre: elementos y seguido del igual abrimos llaves. Ejm:

elementos = {}

-> El diccionario esta vacio, para agregarle nuevos elementos debo seguir la siguiente estructura: Colocamos nuestro diccionario seguido de corchetes y dentro de los corchetes la llave la cual queremos anadir, seguido de los corchetes colocamos el igual y despues el valor el cual nosotros queremos almacenar(Recordemos que las llaves en los diccionarios son objetos inmutables, objetos los cuales NO pueden modificar su valor en tiempo de ejecucion, como strings, tuplas, enteros, flotantes,etc). En este caso vamos a utilizar un string, el tipo mas comun para crear llaves, Ejm:

elementos["nombre"] = "Cody"

-> Esta es la forma en la que podremos anadir mas elementos a los diccionarios. 



elementos = {}

elementos["nombre"] = "Cody"

print(elementos)
En consola: {'nombre': 'Cody'}

 Visualizamos que el diccionario posee un elemento con su correpondiente llave y con su correspondiente valor. 

 Si nosotros quisiesemos conocer la longitud de un diccionario utilizamos la funcion len().

print(len(elementos))
En consola: 1
-> Eso quiere decir que el diccionario posee un solo elemento. 


 Nosotros podemos anadir la N cantidad de elementos que deseemos, por ejemplo vamos a anadir una tupla al ejemplo anterior. 

elementos = {}

elementos["nombre"] = "Cody"
elementos[(1, 2, 3)] = "La llave es una tupla"

print(elementos)
print(len(elementos))

En consola: 
{'nombre': 'Cody', (1, 2, 3): 'La llave es una tupla'}
2

-> El diccionario ahora posee dos elementos con sus correspondientes llaves y valores, posee una llave de tipo string y una llave de tipo tupla. 


AHORA VAMOS A MODIFICAR EL VALOR DE UNA LLAVE: Practicamente vamos a trabajar con la misma estructura. 
 
 Modifiquemos el valor para la llave nombre. 

elementos = {}

elementos["nombre"] = "Cody" <-Crea la llave con su valor.
elementos[(1, 2, 3)] = "La llave es una tupla"

elementos["nombre"] = "CodigoFacilito" <-Actualiza el valor de la llave.

print(elementos)
print(len(elementos))
En consola: 
{'nombre': 'CodigoFacilito', (1, 2, 3): 'La llave es una tupla'}
2

-> Lo unico que debemos hacer es poner nuevamente nuestro diccionario, corchetes y dentro de estos la llave que queremos actualizar, signo igual y su nuevo valor. 
 Es exactamente la misma estructura ya que Python hace lo siguiente: Si la llave no existe dentro de diccionario la crea, en caso de que la llave si exista entonces la actualiza. 


AHORA, QUE PASA SI AL MOMENTO DE CREAR EL DICCIONARIO NOSOTROS COLOCAMOS DOS LLAVE CON EL MISMO VALOR???

EJEMPLO:

elementos = {"a": 1, "b": 2, "c": 3, "a": 4}

-> En este ejemplo la llave "a" se encuentra duplicada. 

print(elementos)
print(len(elementos))

En consola: 
{'a': 4, 'b': 2, 'c': 3}
3

-> En el resultado vemos que "a" unicamente se encuentra una sola vez y con el valor que se le asigno de ultimo. Ya que en Python NO se permiten las llaves duplicadas y el valor de la llave sera el ultimo valor asignado. 


A PARTIR DE LA VERSION 3.7 DE PYTHON, LOS DICCIONARIOS CONSERVAN EL ORDEN CON RESPECTO A SUS LLAVES EN EL CUAL FUERON DEFINIDOS. 



----------------------------------------------------------------------------------------------

# 3) CLASE 3- OBTENER ELEMENTOS

Tenemos el siguiente diccionario:

diccionario = {"a": 1, "b": 2, "c": 3, "d": 4}

Vamos a obtener el valor de la llave d. Creo una nueva variable para almacenar el valor tomado, seguido del igual coloco la variable del diccionario en donde esta contenida la llave, abro corchetes y dentro de ellos pongo  la llave de la cual necesito su valor. 

valor = diccionario["d"]

print(valor)
En consola: 4

--> De esta manera obtengo los VALORES de una llave en un diccionario, siempre y cuando la llave exista.  

 Si nosotros tratamos de obtener el valor de una llave que no existe vamos a obtener un error. 

 Para que nosotros podamos evitar este posible error, podemos hacer uso de la palabra reservada in, la cual me va a retornar un valor booleano. "a" in diccionario.

diccionario = {"a": 1, "b": 2, "c": 3, "d": 4}
 
print("a" in diccionario)

valor = diccionario["d"]

print(valor)
En consola:
True
1


 UTILIZANDO EL METODO GET PARA OBTENER VALORES DE FORMA SEGURA. 

 El metodo get recibe como argumento la llave de la cual queremos conocer su valor. Ejm:

valor = diccionario.get("d")

print(valor)


 Pero si en este caso tratamos de obtener el valor de una llave que no existe no vamos a obtener un error. Ejm:

valor = diccionario.get("z")

print(valor)
En consola: None

 None -> Hace referencia a la ausencia de algun valor. 

 El metodo get de forma opcional puede recibir un segundo argumento, este segundo argumento se va a retornar siempre y cuando la llave que queramos conocer su valor no exista, y este segundo argumento seria el valor por default a retornar. Ejm: 

valor = diccionario.get("z", "La llave no existe en el dict.")

print(valor)
En consola: La llave no existe en el dict.

Si coloco una llave que si existe y uso este segundo argumento, me va retornar el valor de dicha llave. Y el valor que le podemos pasar a este segundo argumento puede ser de cualquier tipo (booleano, entero, flotante, lista, tupla, etc.)

 
 EL METODO SETDEFAULT:

 Este metodo nos permite obtener el valor de una llave. Y si la llave no existe, entonces se procedera a anadir con su respectivo valor al diccionario. Este metodo recibe dos parametros, el primero es la llave que estamos buscando y el segundo es el valor que queremos anadir en caso la llave no exista. Ejm: Intentemos obtener el valor para la llave "e", en caso la llave no exista entonces procedamos a anadirla con su correspondiente valor que es 5. 

valor = diccionario.setdefault("e", 5)

print(valor)
En consola: 5

print(diccionario)
En consola: {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

--> Se anadio la nueva llave con su valor. 



----------------------------------------------------------------------------------------------

# 4) CLASE 4- LLAVES, ITEMS Y VALORES. 

 En ocasiones tenemos la necesidad de conocer que llaves, que valores o que llaves-valores, almacenamos en los diccionarios. 

 Para eso tenemos 3 metodos que nos ayudaran en esta problematica. Estos son:

- Metodo keys
- Metodo values
- Metodo Items

-> Estos metodos nos ayudaran a obtener las llaves, los valores y los elementos dentro de un diccionario. 



METODO KEYS: Este metodo va a retornar un objeto en donde se encuentran almacenadas todas las llaves del diccionario. 


diccionario = {"a": 1, "b": 2, "c": 3, "d": 4}

llaves = diccionario.keys()

print(llaves)
En consola: dict_keys(['a', 'b', 'c', 'd'])

-> Visualizamos un objeto de tipo dict_keys, este objeto facilmente podemos convertirlo en una tupla. Ejm: 

llaves = tuple(diccionario.keys())

print(llaves)
En consola: ('a', 'b', 'c', 'd')

-> Desde el punto de vista del profesor es mucho mas seguro trabajar con una tupla de llaves. 



METODO VALUES:  

valores = diccionario.values()

valores = tuple(diccionario.values())

print(valores)
En consola: dict_values([1, 2, 3, 4])
(1, 2, 3, 4)


-> IMPORTANTE, tanto los valores como las llaves se van a obtener con respecto a su orden. 



METODO ITEMS: 


elementos = diccionario.items()

elementos = tuple(diccionario.items())

print(elementos)
En consola:
dict_items([('a', 1), ('b', 2), ('c', 3), ('d', 4)])
Como tupla:
(('a', 1), ('b', 2), ('c', 3), ('d', 4))

COMO CONSEJO, se cambiaron a tupla para que posteriormente nuestro programa no pueda modificarlos. 


----------------------------------------------------------------------------------------------

# 5) CLASE 5- ELIMINAR ELEMENTOS. 
 Existen dos formas de eliminar elementos en los diccionarios.

FORMA 1: UTILIZANDO EL METODO DEL

diccionario = {"a": 1, "b": 2, "c": 3, "d": 4}

-> Vamos a eliminar el elementos cuya llave sea "a".
Para ello podemos hacer uso de la palabra reservada del. 

del diccionario["a"]

print(diccionario)
En consola: {'b': 2, 'c': 3, 'd': 4}
-> Podemos confirmar que fue eliminado el elemento. 

 Tambien podemos confirmar imprimiendo en consola la longitud del elemento con el metodo len. Lo podemos hacer antes y despues de ejecutar el metodo del. Ejm:

diccionario = {"a": 1, "b": 2, "c": 3, "d": 4}

print(len(diccionario))

del diccionario["a"]

print(diccionario)

print(len(diccionario))

En consola: 
4
{'b': 2, 'c': 3, 'd': 4}
3



FORMA 2: UTILIZANDO EL METODO POP.

 El metodo pop recibe como argumento la llave del elemento que queremos extraer del diccionario y retorna el valor de la llave que queremos eliminar. Vamos a almacenar ese valor. Ejm, vamos a eliminar "b".

diccionario = {"a": 1, "b": 2, "c": 3, "d": 4}

valor = diccionario.pop("b")

print(valor)

print(diccionario)

En consola: 
2
{'a': 1, 'c': 3, 'd': 4}


 QUE PASA SI COLOCAMOS LLAVES A ELIMINAR QUE NO EXISTEN?????

R: Nos va a dar un error de llave, en ambas formas de eliminar. 
 Por lo tanto antes de tratar de eliminar cualquier elemento del diccionario lo primero que debemos hacer sera cerciorarnos que dicho elemento exista dentro del diccionario. Esto para evitar posibles errores en la ejecucion del programa. 


ELIMINANDO TODOS LOS ELEMENTOS DEL DICCIONARIO: 

 Para eliminar todos los elementos de un diccionario haremos uso del metodo clear. El metodo clear va a eliminar todos los metodos del diccionario, dando como resultado que nuestro diccionario sea un diccionario vacio. 

diccionario = {"a": 1, "b": 2, "c": 3, "d": 4}

diccionario.clear()

print(diccionario)
En consola: 
{}



# ------------------>MODULO-6/CICLOS Y CONDICIONES

# 1) CLASE 1 - TIPO NONE.

 None es usado para definir un valor vacio. 

 Frecuentemente usaremos none para representar la ausencia de algun valor. 
 
  Utilizando none seremos capaces de almacenar variables que simplemente no almacenen valor alguno, algo que es muy util cuando aun no sabemos que tipo de valor usaremos mas adelante. 

 Ejemplo, imagina el siguiente escenario: Nos encontramos consumiendo una API que sabemos nos va a retornar algun valor, pero desconocemos que tipo (Puede ser un string, un diccionario, una tupla, etc.). En estos casos, en los casos en donde nosotros no sabemos que tipo de valor usaremos mas adelante, lo aconsejable es simplemente no crear variables de diferentes tipos, evitando asi reservar espacio en memoria que muy probablemente no vayamos a utilizar, y lo aconsejable es simplemente crear variables las cuales no almacenen valor alguno. 
 Por ejemplo si yo se que voy a trabajar con algun valor mas adelante en mi programa pero justo ahora no se el tipo, entonces puedo crear una variable que no almacene ningun valor, una variable vacia. 

 -> Para indicar que la variable no almacena ningun valor, haremos uso de la palabra reservada None. Ejm:

resultado = None

print(resultado)
En consola: None

print(type(resultado))
En consola: <class 'NoneType'> => No posee tipo. 

 
 Si recordamos, Python al ser un lenguaje de tipado dinamico facilmente podemos asignarle un valor a una variable vacia. Por ejemplo definimos la variable que no almacena ningun valor y mas adelante asignamos un nuevo valor, que obviamente puede ser de cualquier tipo. 


--------------------------------------------------------------------------------------------------------------

# 2) CLASE 2 - VALORES FALSOS. 

 Algo interesante de None es que Python lo toma como un valor falso. 

 Recordando, si utilizamos las constantes True y False seremos capaces de representar valores booleanos. De igual forma estas constantes representan numeros  enteros, True hace referencia a 1 y False hace referencia a 0.
 True (1) / False (0)

 Sin embargo utilizando la constante False no es la unica forma en la que nosotros podemos representar un valor falso. En Python existen estas 8 formas en las que podemos representar un valor falso:

False:
None
0
0.0
''/"" -> Un string vacio
[] -> Un listado vacio
() -> Una tupla vacia
{} -> Un diccionario vacio

--> Estos 8 valores para Python, representan-equivalen a falso, y viceversa, o sea todos aquellos valores que no se encuentren dentro de este listado seran tomados como verdaderos. 

 Mediante estos valores directamente seremos capaces de condicionar. 

--------------------------------------------------------------------------------------------------------------

# 3) CLASE 3 - CONDICIONES.

 AHORA VAMOS A TRABAJAR CON ESTRUCTURAS DE CODIGO. 

 En ciertas ocasiones tendremos la necesidad de ejecutar ciertos bloques de codigo dependiendo de ciertos criterios a evaluar o lo que es lo mismo, vamos a condicionar nuestro programa. 

 Y para que nosotros podamos condicionar utilizando Python, haremos uso de la palara reservada "if". 

Ejm: 

* 1- Vamos a crear una nueva variable:

resultado = 10

* 2- Ahora condicionemos un mensaje, y que este mensaje pueda ser impreso en consola si y solo si la variable es mayor que 10. 
 -> Para ello vamos a condicionar nuestro codigo, colocamos if y posteriormente un valor booleano ya sea verdadero o falso (Recordemos que existen diferentes formas en las cuales representar ya sea verdadero o falso y no unicamente utilizando las constantes True o False), una vez nosotros hayamos colocado el valor booleano hacemos uso de dos puntos. De esta forma vamos a condicionar => if <Bool>:  

* 3- Ahora para que nosotros podamos crear un nuevo bloque vamos a indentar, para indentar haremos uso de 4 espacios. Indentando mediante 4 espacios, por convencion de la comunidad Python seremos capaces de ejecutar un nuevo bloque. Para la condicion el nuevo bloque es de suma importancia, ya que este bloque se va a ejecutar siempre y cuando el valor booleano sea verdadero.
Ejm: 

if <Bool>:
    print("La variable cumple con la condicion.")

 -> Este sera el mensaje que se va a imprimir en consola siempre y cuando la variable cumpla con la condicion, que en este caso seria si la variable es mayor que 10. 


* 4- Para que nosotros podamos obtener como resultado un valor booleano, vamos a utilizar el operador relacional ">".

 Colocamos antes de la condicion if: 
resultado = resultado > 10 (Recordar que el operador > me da un valor booleano), este es el valor booleano que vamos a poner en la condicion.

Y vamos a colocar el resultado de esta expresion, ya sea verdadero o falso, en la condicion: 

if resultado:
    print("La variable cumple con la condicion") 

-> Si resultado es verdadero entonces se ejecuta este bloque, en este caso unicamente seria imprimir en consola. 
  
EJEMPLO COMPLETO:  

resultado = 10

resultado = resultado > 10

if resultado:
    print("La variable cumple con la condicion")

En consola: No tenemos ningun tipo de error y tampoco tenemos ningun tipo de mensaje, esto quiere decir que la condicion no se cumple, ya que resultado no es mayor que 10. La expresion resultado > 10 da como resultado falso, y falso como no es verdadero entonces la condicion no se cumple, por lo tanto no se ejecuta el bloque. 

 En este ejemplo explicativo estamos utilizando una linea de codigo extra para poder obtener resultado, estamos utilizando: resultado = resultado > 10

 Sin embargo nosotros podemos colocar una expresion directamente en la condicion y quedaria de la siguiente forma: 

resultado = 10

if resultado > 10:
    print("La variable cumple con la condicion.")

--> Si resultado es mayor que 10, ejecuta este bloque. 


 Utilizarlo de esta forma es mucho mas comun que simplemente utilizar un valor booleano. 


 Tambien podemos hacer uso de operadores logicos, por ejemplo: 

if resultado > 10 and resultado < 20:
    print("La variable cumple con la condicion.")

-> O sea, si el resultado es mayor que 10 y menor que 20, imprime el mensaje. 


 Tambien podemos ejecutar un bloque de codigo cuando la condicion o las condiciones no se cumplan, podemos hacerlo mediante la palabra reservada else, colocamos else: y creamos un nuevo bloque. Ejm: 

resultado = 50

if resultado > 10 and resultado < 20:
    print("La varible cumple con la condicion")
else:
    print("La condicion no se cumplio")

 La palabra reservada else: nos permite ejecutar un codigo siempre y cuando la condicion no se cumpla, y el else es completamente opcional. 


--------------------------------------------------------------------------------------------------------------

# 4) CLASE 4 - ELIF.

 Algo muy comun al condicionar nuestro programa, es querer evaluar multiples condiciones para asi poder ejecutar diferentes bloques, y para lograr esto haremos uso de la palabra reservada "elif". 

Ejm:
- Vamos a estar trabajando con la variable calificacion, que representa la calificacion de un alumno. 

calificacion = 8

-> Lo que vamos a hacer es imprimir en consola diferentes mensajes con respecto a la calificacion de un alumno. 
Recordando que si utilizamos el operador relacional == seremos capaces de obtener un valor booleano. 
 

if calificacion == 10:
    print("Felicidades, aprobaste la materia con una calificacion perfecta.")
else:
    print("Reprobaste la materia.") 

 Sin embargo sabemos que obtener de calificacion 8, no amerita el mensaje de reprobado, por lo tanto para que el usuario no visualice ese mensaje debemos evaluar otras condiciones. 

 Para ello haremos uso de la palabra reservada elif seguida de nuestra segunda condicion. La colocamos despues de la primera condicion y antes del else. Ejm:
elif calificacion == 9 or calificacion == 8:
   print() -> Si calificacion es igual a nueve o calificacion es igual a 8, vamos a imprimir el siguiente mensaje.


if calificacion == 10:
    print("Felicidades, aprobaste la materia con una calificacion perfecta.")
elif calificacion == 9 or calificacion == 8:
    print("Felicidades, aprobaste la materia.")
else:
    print("Reprobaste la materia.") 


 Podemos evaluar otras condiciones para dar mas resultados:

if calificacion == 10:
    print("Felicidades, aprobaste la materia con una calificacion perfecta.")
elif calificacion == 9 or calificacion == 8:
    print("Felicidades, aprobaste la materia.")
elif calificacion == 7 or calificacion == 6:
    print("Aprobaste la materia.")
else:
    print("Reprobaste la materia.") 


-> En caso de que calificacion sea un numero completamente diferente a 10, 9, 8, 7, 6; el usuario va a visualizar en consola: Reprobaste la materia. 

 Las condiciones se van a evaluar de forma descendente, comenzando siempre con el if. Si las condiciones para el if no se cumplen, entonces se comienzan a evaluar las condiciones elif, de forma descendente y si a su vez estas no se cumple, pasa al else. 



----------------------------------------------------------------------------------------------------------------
# 5) CLASE 5 - TERNARIO.

PRACTICA:
 Necesito colocar sobre una pagina web la calificacion de un alumno. La calificacion la estare colocando de color verde si y solo si el alumno tiene una calificacion aprobatoria (Mayor o igual a 7), en caso contrario la calificacion se pintara de color rojo. 

PASOS: 

1- Primero vamos a declarar dos variable: calificacion (haciendo referencia a la calificacion del alumno) y color (que seria al color que vamos a utilizar para pintar la calificacion). Como a estas alturas del programa no sabemos que color sera el que utilizaremos, ya sea verde o rojo porque va a depender de la calificacion que tenga el alumno, lo que podemos hacer es crear una variable la cual no almacene ningun tipo de valor, para esto podemos hacer uso de la palabra reservada None.

calificacion = 10

color = None


2- Lo siguiente que vamos a hacer es condicionar. 

if calificacion >= 7:
    color = "Verde"
else:
    color = "Rojo"

-> Si la calificacion es aprobatoria el color sera verde, en caso contrario sera rojo. Mediante esta condicion seremos capaces de solventar nuestro problema, si el alumno posee una calificacion aprobatoria entonces su calificacion se pintara de color verde y en caso contrario se pintara de color rojo. 


3- Vamos a imprimir en consola la calificacion y el color:

print(calificacion, color)



EJEMPLO COMPLETO:

calificacion = 10

color = None

if calificacion >= 7:
    color = "Verde"
else:
    color = "Rojo"

print(calificacion, color)
En consola: 10 Verde


 Esta metodologia funciona y podemos solventar la problematica pero el problema no es lo suficientemente grande para que amerite tantas lineas de codigo. Asi que lo que vamos a hacer es implementar un refactor. Vamos a convertir estas lineas de codigo a una sola y para ello vamos a utilizar el equivalente del OPERADOR TERNARIO en Python:

color = "Verde" if calificacion >= 7 else "Rojo" 

 => Color es igual a verde si y solo si calificacion es mayor igual a 7, en caso contrario el color sera rojo.
 De esta forma es como nosotros podemos asignar un valor a una variable utilizando una condicion en una sola linea de codigo. 
 Entonces utilizando el valor ternario en Python vamos a colocar: el valor + if + nuestra condicion + else + segundo valor.


EJEMPLO:

calificacion = 5

color = "Verde" if calificacion >= 7 else "Rojo"

print(calificacion, color)



IMPORTANTE - OJO:

Cuando estamos condicionando en una sola linea de codigo el else se convierte en obligatorio, deja de ser opcional.


----------------------------------------------------------------------------------------------------------------
# 6) CLASE 6 - ASIGNAR VALORES MEDIANTE OPERADORES LOGICOS. 

 Utilizando el operador logico "or" seremos capaces de asignar valores a nuestras variables. 

 Python lo que va a hacer es simplemente evaluar cada una de las opciones al utilizar el valor logico or y va a asignar a la variable el primer valor verdadero con el cual se tope. Ejm:

 variable = "Cody" or "CodigoFacilito"

-> En este caso Python va a asignar a la variable el primer valor verdadero con el cual se tope, recordando que la lectura es de izquierda a derecha, por lo tanto la variable va a almacenar Cody, ya que recordamos todos aquellos strings que no sean string vacios, Python los considera como valores verdaderos. Por lo tanto si en consola imprimo variable el resultado sera Cody. 

variable = "Cody" or "CodigoFacilito"

print(variable)
En consola: Cody


 Por supuesto nosotros no estamos limitados unicamente a trabajar con strings, podemos trabajar con listas, tuplas, diccionarios, strings, enteros, flotantes, booleanos, etc. Ejm:

variable = "" or 0 or [] or True

print(variable)
En consola: True

-> La variable almacena verdadero, ya que los tres primeros son considerados por Python como valores falsos. 

 El que nosotros podamos asignar valores a nuestras variables utilizando el operador logico or, es de mucha utilidad principalmente cuando nosotros queremos asignar valores los cuales pertenezcan a otras variables, de esta forma simplemente vamos a omitir una condicion. 
Por ejemplo:

- Vamos a crear dos nuevas variables:

listado = []
nombre = "Cody"  

- Ahora vamos a asignarle a la variable, "variable" ya sea el listado o Cody. Dependiendo cual de estas variables almacene un valor verdadero.:

if listado:
    variable = listado
else:
    variable = nombre

Se lee: Si listado, es decir si el listado posee por lo menos un elemento entonces variable es igual a listado. En caso contrario, variable es igual a nombre. 


Ejemplo completo: 

listado = []
nombre = "Cody"  

if listado:
    variable = listado
else:
    variable = nombre

print(variable) 
En consola: Cody -> Ya que listado es un valor falso que no posee ningun elemento dentro de el.  


 Sin embargo nosotros pudiesemos reducir estas lineas de codigo a una sola. Ejm: 

listado = []
nombre = "Cody" 

variable = listado or nombre

print(variable) 

-> El primer valor verdadero que se encuentre en esta comparacion sera asignado a nuestra variable. 



-------------------------------------------------------------------------------CICLOS---------------------------

# 7) CLASE 7 - CICLO WHILE.


 El ciclo while nos permite ejecutar una N cantidad de veces un bloque de codigo hasta que una condicion se cumpla "mientras que". 

Ejm: Creemos un programa el cual nos permita visualizar en consola del 1 al 10. 

* 1- Creamos una variable que tendra por nombre contador y que comenzara en 1.

contador = 1


* 2- Comenzamos a iterar, usamos la palabra reservada while seguida de nuestra condicion. 

while contador <= 10: 
-> Mientras que contador sea menor o igual que 10. 


* 3- Luego creamos un nuevo bloque que se va a ejecutar siempre y cuando la condicion se cumpla. En ese nuevo bloque primero vamos a imprimir en consola contador y posteriormente vamos a modificar su valor incrementando por 1 a contador, de tal forma que podamos imprimir en consola del 1 al 10.  

print(contador)

contador = contador + 1


EJEMPLO COMPLETO:

contador = 1

while contador <= 10: 

    print(contador)

    contador = contador + 1

En consola:
1
2
3
4
5
6
7
8
9
10

--> En este caso este bloque de codigo se va a ejecutar siempre y cuando contador sea menor o igual a 10, sin embargo dentro del bloque nosotros incrementamos en 1 el valor de contador, asi que cuando el contador valga 11 la condicion deja de cumplirse. 


 El ciclo while lo utilizaremos siempre y cuando NO SEPAMOS la cantidad de iteraciones que vamos a realizar. 

 En el caso del ejemplo si sabemos la cantidad de iteraciones que vamos a realizar, sabemos que son 10, por lo tanto no es un ejemplo correcto, vamos con otro. 



EJEMPLO #2- Imprimamos la cantidad de digitos que posee un numero entero. 


numero = 1234

contador_digitos = 0


while numero >= 1:
    contador_digitos = contador_digitos + 1

    numero = numero / 10 


print(contador_digitos) 

En consola: 4


MI EXPLICACION: 

- La variable numero es a la que le vamos a calcular el numero de digitos. 

- La variable contador_digitos es la variable que nos va a retornar el numero de digitos que posee numero. 

- while numero >= 1: --> Mientras que el numero sea mayor o igual a uno se ejecuta el bloque de codigo a continuacion. 

- contador_digitos = contador_digitos + 1 --> Incremento el valor de contador en 1 , para que cada vez que se haga la division entre 10, nos contara un digito mas. O sea, cada vez que se haga el proceso de la division entre si, ya haya contado 1 y estos 1 se van sumando en cada vuelta y sera el resultado final que vamos a recibir en el print. Esta es la variable que va a dar el resultado final, la que va a mostrar todo.

- numero = numero / 10 --> Voy a decrecer el valor de numero, cuando lo divido entre 10 le elimino un digito hasta que lo dejo en 0 digitos y es cuando se rompre el ciclo por la condicion del while. 

- print(contador_digitos) --> Me va a imprimir la cantidad de digitos que posee el numero. 


--> Es decir lo que yo voy a hacer con el bucle es que cada vez que se ejecute el cuerpo del bucle voy a contar +1 y voy a dividir al numero entre 10. Esto hace que voy reduciendo el numero en cantidad de digitos de uno en uno y cada una de estas divisiones en contador voy sumando uno, es como si contador cuenta las veces que numero se va reduciendo y nos dice cuantas veces se redujo.
Cuando numero no es mayor que cero el bucle terminara y nos devolvera el return, nos va a devolver el contador, porque es una variable que hemos creado nosotros para ir contando los digitos del numero. 

Explicacion YT: https://www.youtube.com/watch?v=Ikl_DiSoaZ0&t=217s

YA LO ENTENDI. 


 Reiteramos, el ciclo while lo vamos a utilizar siempre y cuando no sepamos la cantidad de iteraciones que vamos a realizar ya que el ciclo while se apoya de una condicion y cuando se va a cumplir la condicion a ciencia cierta no lo sabemos. 
 

 ## IMPORTANTE, Python tiene una "abreviatura" en la cual nosotros podemos incrementar el valor de una variable en 1 o en cualquier numero que deseemos. Ejemplo del caso de la variable contador_digitos:

contador_digitos = contador_digitos + 1 es igual a poner: contador += 1

-> De esta forma Python entiende que vamos a incrementar en 1 el valor de contador. 


contador_digitos = contador_digitos + 1 igual a: contador_digitos += 1


 Al igual que con las condiciones en el ciclo while podemos utilizar el else, y tambien es opcional. Ejm:


numero = 1234

contador_digitos = 0


while numero >= 1:
    contador_digitos = contador_digitos + 1

    numero = numero / 10 
else: 
    print(contador_digitos)


--> SE LEE ASI: Cuando el ciclo finalice entonces imprime en consola la cantidad de digitos. Cuando la condicion deje de cumplirse, cuando numero deje de no ser mayor o igual a 1, entonces (else), imprime en consola. 


POR QUE PODEMOS UTILIZAR EL ELSE JUNTO CON EL CICLO WHILE???

-> Al igual que con el if, el ciclo while se apoya de una condicion. Si la condicion se cumple entonces se ejecuta un bloque, tanto para el if como para el while. Sin embargo si la condicion no se cumple, entonces tenemos la opcion de definir un nuevo bloque. 

# COMO FUNCIONA UN CICLO WHILE:

----------------------------------------------------------------------------------------------

# 8) CLASE 8 - FOREACH.

 El ciclo for en Python no es mas que un ciclo for each, es decir utilizando el ciclo for seremos capaces de iterar sobre cada uno de los elementos dentro de una coleccion, dentro de un objeto iterable, que facilmente puede ser un string, una tupla, una lista, un diccionario, etc. 

 Por ejemplo, tengo la siguiente variable que no es mas que una lista de strings y vamos a mostrar en consola cada uno de los elementos dentro de este listado utilizando el ciclo foreach y no sus indices. 

usuarios = ["usuario1", "usuario2", "usuario3", "usuario4"]

Para utilizar el ciclo for:

1- Utilizamos la palabra reservada for mas una nueva variable que creamos, aconsejamos nombrarla en singular ya que la variable va a tomar el valor de cada uno de los elementos dentro de la coleccion en cada iteracion; en la primera iteracion la variable tomara el valor de usuario1, en la segunda de usuario2 y asi sucesivamente.
(Nota: regularmente las listas, tuplas y diccionarios tendran su nombre en plural.) 
 Posteriormente colocamos in seguido de nuestro objeto el cual queremos iterar mas dos puntos. Luego indentamos  y creamos un nuevo bloque. En este caso en cada interacion vamos a imprimir en consola el valor de la variable usuario, esta variable unicamente va a existir para este bloque.

for usuario in usuarios:
    print(usuario)
     
Ejemplo completo:

usuarios = ["usuario1", "usuario2", "usuario3", "usuario4"]

for usuario in usuarios:
    print(usuario)

En consola: 
usuario1
usuario2
usuario3
usuario4

--> Visualizamos en consola los diferentes strings que almacena mi listado. 


El ciclo foreach se comprende de 4 partes:
- for
- Una variable que tomara el valor de cada uno de los elementos dentro de la coleccion por cada iteracion
- in
- Y el objeto el cual queremos iterar

+: y creamos un nuevo bloque. 

Una vez que nosotros terminamos de iterar cada uno de los objetos de la coleccion el ciclo finaliza. Y como en este caso no estamos utilizando ningun tipo de condicion, entonces no es posible utilizar el else. 

----------------------------------------------------------------------------------------------------------------

# 9) CLASE 9 - FUNCION ENUMERATE - FUNCION RANGE.


 Las dos siguientes funciones las usaremos mucho en conjunto con el ciclo for each. 

 Son la funcion range y enumerate. 

## FUNCION RANGE: Utilizando esta funcion seremos capaces de crear una secuencia de numeros enteros los cuales facilmente podemos iterar.

 Por ejemplo, creemos un rango del 0 al 10. 
-> Creamos una variable que sera igual a la funcion range y dentro de los parentesis, como argumento, vamos a colocar el numero final de nuestro rango (en este caso como queremos crear un rango del 0 al 10 vamos a colocar 11), range por default comenzara en 0 y el valor final no es tomado en cuenta dentro del rango, seria ese valor -1, o sea el ultimo valor no es tomado en cuenta sino el anterior a ese.  

rango = range(11)  

print(rango)
En consola: range(0, 11)

print(type(rango))
En consola: <class 'range'>

 Este objeto facilmente podemos interarlo y en cada iteracion imprimimos valor. Por ejemplo:

for valor in rango:
    print(valor) 

En consola: 
0
1
2
3
4
5
6
7
8
9
10


 Podemos colocar la funcion range dentro del ciclo for, ejm:

for valor in range(21):
    print(valor)


 AHORA, CUANDO NO QUEREMOS COMENZAR DE CERO SINO DESDE UN NUMERO DIFERENTE. 
-> En ese caso debemos colocar dos argumentos a la funcion range, que serian el punto inicial y el punto final. Por ejemplo:

for valor in range(5, 21):
    print(valor)
En consola: 
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20


 USANDO UN TERCER ARGUMENTO, podemos usar un tercer argumento que hace referencia a los saltos. Ejm, creemos un rango de numero enteros del 5 al 20 con saltos de 2 en 2.

for valor in range(5, 21, 2):
    print(valor)
En consola: 
5
7
9
11
13
15
17
19

--------------------------------------

## FUNCION ENUMERATE: La funcion enumerate nos permite enumerar cada uno de los elementos dentro de una coleccion. 

Para el ejemplo vamos a crear una nueva lista en la que vamos a iterar utilizando indices y para ello vamos a utilizar enumerate.

numero = [10, 20, 30, 40, 50]

for indice, numero in enumerate(numero):

--> La funcion enumerate va a retornar una tupla con 2 valores. El primer valor hace referencia al indice del elemento dentro de la coleccion, y el segundo valor hace referencia al elemento dentro de la coleccion que seria indice y numero. 

Ejemplo completo:

numero = [10, 20, 30, 40, 50]

for indice, numero in enumerate(numero):
    print(indice, numero)

En consola:
0 10
1 20
2 30
3 40
4 50
-> Aqui vemos el indice y el numero de enumerate.


 Si queremos modificar el valor del indice podemos hacerlo. Lo que hacemos para esto es pasar un segundo valor a nuestra funcion y que seria el numero a partir del cual queremos comenzar, por default comienza en 0 pero con este segundo argumento pero con este segundo argumento comienzo en otro. Ejm: 

numero = [10, 20, 30, 40, 50]

for indice, numero in enumerate(numeros, 10):
    print(indice, numero)

En consola:
10 10
11 20
12 30
13 40
14 50
-> Vemos que el indice "comienza" en 10. 

 El uso de este segundo argumento no es muy comun. 
----------------------------------------------------------------------------------------------------------------

# 9) CLASE 10 - BREAK AND CONTINUE.


 Existen dos palabras que nos permitiran modificar el comportamiento de nuestros ciclos, ya sea el ciclo while y el ciclo foreach. Estas palabras son:

BREAK AND CONTINUE.

BREAK:

Ejemplo: Vamos a crear una variable y posterior vamos a crear un ciclo for, para recorrer cada uno de los caracteres de esta variable. 

titulo_curso = "Curso profesional de Python"

for caracter in titulo_curso:
    print(caracter)

En consola:
C
u
r
s
o

p
r
o
f
e
s
i
o
n
a
l

d
e

P
y
t
h
o
n

--> Visualizamos cada uno de los caracteres que comprende un string, ya que recordemos que un string es un objeto iterable. 

Ahora, QUE PASA SI NOSOTROS CONDICIONAMOS. EJM:


titulo_curso = "Curso profesional de Python"

for caracter in titulo_curso:

    if caracter == "P":
        break

    print(caracter)

En consola:
C
u
r
s
o

p
r
o
f
e
s
i
o
n
a
l

d
e

En este caso:

- Estamos colocando doble indentacion. La primera nos permite crear un bloque para el ciclo for y la segunda para la condicion if. 

- Y en consola visualizamos hasta la p mayuscula. Esto gracias a que la palabra break nos permite finalizar de forma inmediata nuestro for, tambien lo haria con el ciclo while. Break finaliza de forma inmediata cualquier tipo de ciclo. 

 
CONTINUE:

titulo_curso = "Curso profesional de Python"

for caracter in titulo_curso:

    if caracter == " ":
        continue

    print(caracter)

En consola:
C
u
r
s
o
p
r
o
f
e
s
i
o
n
a
l
d
e
P
y
t
h
o
n

--> Se visualizan cada uno de los caracteres exceptuando los espacios. 

Esto se debe a que el uso de la palabra continue hara que el ciclo salte a la siguiente iteracion. Por lo cual el codigo que se encuentre despues de esta palabra simplemente no es ejecutado con el flujo normal del programa, es por ello que en consola no visualizamos los espacios. Por ejemplo si yo coloco la palabra o, entonces se lee: cuando caracter sea igual a o se va a saltar la ejecucion y va a pasar a la siguiente iteracion, evitando asi que el caracter se imprima en consola. Ejm:


titulo_curso = "Curso profesional de Python"

for caracter in titulo_curso:

    if caracter == "o":
        continue

    print(caracter)


En consola:
C
u
r
s

p
r
f
e
s
i
n
a
l

d
e

P
y
t
h
n


----------- MODULO_7->FUNCIONES-------------------------
-----------------------------------------------------

#1) CLASE 1- FUNCIONES.

 Para que nosotros podamos definir una funcion, debemos hacer uso de la palabra reservada "def" seguido del nombre de la funcion mas parentesis. Dentro de los parentesis vamos a definir la "n" cantidad de variables necesarias para que la funcion funcione, a estas variables las conoceremos como parametros.  

 Vamos a crear una funcion que sume dos numero enteros:
(Al igual que las variables, los nombres de las funciones deben seguir la nomenclatura snake case)

def suma():
    numero_uno = int(input("Ingresa el primer numero entero"))
    numero_dos = int(input("Ingresa el segundo numero entero"))


    resultado = numero_uno + numero_dos
    print(resultado)
     
suma()

Explicacion del codigo:

- En este caso la funcion suma no va a recibir ningun tipo de valor, asi que no es necesario trabajar con parametros, colocamos los parentesis sin nada dentro de ellos. 

- Despues de definir la funcion, creamos dos puntos seguidos de la indentacion para crear un nuevo bloque de codigo. Dentro de este nuevo bloque vamos a colocar todas aquellas lineas de codigo que queramos ejecutar cuando la funcion sea llamada. 

- En este caso vamos a pedir al usuario que ingrese dos numero enteros, por medio de la funcion input. Como la funcion input nos va a retornar un objeto del tipo string debemos pasarlo a entero por medio de la funcion int. 

- Luego creamos la variable que me va a mostrar el resultado de la suma y su impresion. 

- Una vez que nosotros hayamos definido, hayamos creado nuestra funcion, seremos capaces de utilizarla, de llamarla la "n" cantidad de veces que deseemos. Para llamarla debemos colocar el nombre de la funcion con sus parentesis y dentro de estos como parametros colocamos los argumentos que la funcion necesite. En este caso la funcion suma no posee ningun parametro. Tambien recordar que al llamarla debo eliminar la indentacion, ya que sale de ese bloque de codigo. 

IMPORTANTE: Dentro de una funcion podemos llamar a otras funciones, en este caso la funcion suma manda a llamar tres funciones mas, estos son: la funcion input, la funcion int y la funcion print. 

 Tambien tener en cuenta que yo puedo llamar una funcion la "n" cantidad de veces que deseeo. Por ejemplo si llamo 3 veces la funcion suma, entonces debo ingresar 6 valores. 
----------------------------------------------------------------------------------------------------------------

#2) CLASE 2- ARGUMENTOS.

 En la mayoria de los casos las funciones van a necesitar valores de entrada para su correcto funcionamiento, y para que nosotros podamos leer dichos valores de entrada lo haremos mediante variables. Variables que debemos definir entre los parentesis, a estas variables las conoceremos como PARAMETROS. 
 
 Vamos a trabajar con el ejemplo anterior pero aplicando un refactor. 

FUNCION ANTERIOR:

def suma():
    numero_uno = int(input("Ingresa el primer numero entero"))
    numero_dos = int(input("Ingresa el segundo numero entero"))


    resultado = numero_uno + numero_dos
    print(resultado)
     
suma()


REFACTOR FUNCION:
- Vamos a pedir los dos numeros enteros fuera de la funcion, ya que quiza mas adelante en el programa necesitemos dichos valores. Para sacarlos de la funcion debo ponerlos debajo sin la indentacion. 

- Sin embargo es necesario tener dentro de la funcion a numero_uno y a numero_dos, para ello vamos a crear parametros. Nos situamos dentro de los parentesis y definimos la "n" cantidad de variables que vayamos a necesitar y las vamos a separar mediante una coma (,).

- Debo agregar LOS ARGUMENTOS en el llamado de la funcion. Debo agregar los argumentos para los parametros de la funcion. Los argumentos se asignan con respecto a su posicion, el primer argumento es almacenado en la primera variable, el segundo argumento es asignado a la segunda variable y asi sucesivamente. 


def suma(numero_uno, numero_dos):

    resultado = numero_uno + numero_dos
    print(resultado)

numero_uno = int(input("Ingresa el primer numero entero"))
numero_dos = int(input("Ingresa el segundo numero entero"))
     
suma(numero_uno, numero_dos)

--> De esta forma queda mi funcion, la cual es mucho mas abstracta ya que nos permite sumar dos numeros enteros que dichos valores pueden provenir de diferentes lugares, NO necesariamente de lo que el usuario haya ingresado via teclado, esta funcion nos permite sumar dos numeros enteros que pueden provenir de cualquier lugar, quiza de una base de datos, de un archivo excel, de una archivo .txt, de una API, de lo que el usuario ingreso via teclado, etc. O sea, esos valores no estan amarrados a la funcion, son valores (variables) que estan por fuera de la funcion y los utilizo para mi funcion.  

IMPORTANTE, las variables NO necesariamente deben tener el mismo nombre. Ya que las variables que nosotros hemos definido dentro de la funcion, entre los parentesis van a existir unica y exclusivamente para este bloque:

def suma(numero_uno, numero_dos):
    resultado = numero_uno + numero_dos
    print(resultado)

 Y nosotros podemos nombrar a los parametros como deseemos. Ejm:

def suma(n1, n2):
    resultado = n1 + n2
    print(resultado)

numero_uno = int(input("Ingresa el primer numero entero"))
numero_dos = int(input("Ingresa el segundo numero entero"))
     
suma(numero_uno, numero_dos)

--> Obtenemos el mismo resultado, ya que las variables que defino al crear la funcion son completamente independientes a las variables que se encuentren fuera de la funcion, estas variables van a existir unica y exclusivamente para el bloque de la funcion. 


----------------------------------------------------------------------------------------------------------------

#3) CLASE 3- RETORNAR VALORES.

 Habran ocasiones en las cuales nuestras funciones deban retornar valores, para ello haremos uso de la palabra reservada return. 

 Vamos a trabajar con el ejemplo anterior pero aplicando un refactor.

FUNCION ANTERIOR:

def suma(n1, n2):
    resultado = n1 + n2
    print(resultado)

numero_uno = int(input("Ingresa el primer numero entero"))
numero_dos = int(input("Ingresa el segundo numero entero"))
     
suma(numero_uno, numero_dos)



REFACTOR FUNCION:

- La funcion anterior imprime en consola el resultado de la suma pero ahora nosotros no queremos imprimir en consola el resultado, quiza queremos hacer otras cosas con el, quiza almacenarlo en una base de datos, quiza enviarlo via correo electronico, etc. No queremos imprimirlo en consola pero si nos interesa dicho valor. 
Asi que lo que debo es indicarle a dicha funcion que va a retornar un valor, para ellos sustituimos print(resultado) por return resultado. 

- Ahora como la funcion retorna un valor, nosotros podemos almacenar ese valor en una nueva variable.
Ejm: resultado = suma(numero_uno, numero_dos)

- Despues ese valor que almacene en la variable lo puedo imprimir en consola. 

Queda asi:

def suma(n1, n2):
    resultado = n1 + n2
    return resultado

numero_uno = int(input("Ingresa el primer numero entero"))
numero_dos = int(input("Ingresa el segundo numero entero"))
     
resultado = suma(numero_uno, numero_dos)
print(resultado)

--> En este caso la funcion se vuelve mucho mas abstracta, lo cual es lo ideal. Lo unico que hace es sumar dos numero enteros que pueden provenir de cualquier lugar y posteriormente retorna el resultado.
 

 Podemos reducir mas las lineas de codigo de esta funcion:

def suma(n1, n2):
    return n1 + n2

numero_uno = int(input("Ingresa el primer numero entero: "))
numero_dos = int(input("Ingresa el segundo numero entero: "))
     
resultado = suma(numero_uno, numero_dos)
print("El resultado es:", resultado)


Entonces nuestra funcion:

def suma(n1, n2):
    return n1 + n2

En este caso unicamente se encarga de realizar una sola tarea, que es la de sumar dos numeros. NO se encarga de obtener los valores ni de imprimir en consola. Lo unico que hace es simplemente sumar.  



 Las funciones en Python nos permiten RETORNAR multiples valores. Por ejemplo: Vamos a retornar la suma de n1 + n2 mas un string. Colocamos coma (,) seguido de el segundo o tercer o cuarto... valor. Podemos retornar la "n" cantidad de valores, pero se recomienda no retornar una gran cantidad, se recomienda retornar un maximo de tres valores. 

def suma(n1, n2):
    return n1 + n2, "La funcion retorna 2 valores"


-> Python al percatarse que estamos retornando dos valores, un entero y un string; lo que va a hacer sera generar una tupla y va a retornar la tupla. 

def suma(n1, n2):
    return n1 + n2, "La funcion retorna 2 valores"

numero_uno = int(input("Ingresa el primer numero entero: "))
numero_dos = int(input("Ingresa el segundo numero entero: "))
     
resultado = suma(numero_uno, numero_dos)
print("El resultado es:", resultado)

En consola: El resultado es: (24, 'La funcion retorna 2 valores')

-> Visualizamos una tupla. Y en este caso lo que podemos hacer es implementar el tema de DESEMPAQUETADO DE TUPLAS.



 En este caso como la funcion suma esta retornando una tupla de dos valores, entonces puedo facilmente crear dos variables:

def suma(n1, n2):
    return n1 + n2, "La funcion retorna 2 valores"

numero_uno = int(input("Ingresa el primer numero entero: "))
numero_dos = int(input("Ingresa el segundo numero entero: "))

resultado, mensaje = suma(numero_uno, numero_dos)

print("El resultado es:", resultado)
print(mensaje)
 
En consola:
El resultado es: 2
La funcion retorna 2 valores

- OJO AQUI CON LA CREACION DE LAS DOS VARIABLES. 
- Y CON EL DESEMPAQUETADO DE TUPLAS.


RECORDAR, que lo ideal es retornar un maximo de 3 valores y si la funcion va a retornar mas de una valor lo que podemos hacer es implementar el desempaquetado de tuplas y generar nuevas variables para almacenar los valores retornados. 
----------------------------------------------------------------------------------------------------------------

#4) CLASE 4- PARAMETROS OPCIONALES.

 En las funciones creadas con Python los parametros pueden ser completamente opcionales, para ello al momento de definir de crear nuestra funcion, vamos a asignar valores por default a dichos parametros.    

 Vamos a crear una funcion la cual me permita calcular el area de un circulo:

1- Definimos la funcion con sus parametros. En este caso para que podamos definir el area de un circulo necesitamos dos valores, el radio y pi.: 

def area_circulo(radio, pi):

2- En el return, la funcion va a retornar el area del circulo, escribimos directamente la formula. Nota: Para elevar al cuadrado en Python usamos dobles asterisco. 

return pi * (radio ** 2)

3- Obtenemos el resultado. En los argumentos colocamos los valores corresponientes. 


FUNCION COMPLETA:

def area_circulo(radio, pi):
    return pi * (radio ** 2)

resultado = area_circulo(10, 3.14)
print(resultado)

En consola: 314.0


--> En este caso ambos parametros son abligatorios, asi que debemos colocar valores para los argumentos. 

 Pero como ya sabemos nosotros podemos definir parametros los cuales sean opcionales, y para ello vamos a definir, vamos a establecer los valores por default. 

 En este caso como sabemos, pi es una constante asi que podemos agregarle un valor por default. Lo colocamos asi: 

def area_circulo(radio, pi=3.14) -> No ponemos espacios entre los iguales, no porque de error sino por convencion. Se acuerda no colocar espacios al definir valores por default de un parametros. 

 Cuando ya indicamos un valor por default de un parametros no es necesario utilizar un argumentos para este parametro. Ejm:

def area_circulo(radio, pi=3.14):
    return pi * (radio ** 2)

resultado = area_circulo(10)
print(resultado)

En consola: 314.0


IMPORTANTE MENCIONAR, que nosotros unicamente vamos a establecer valores por default leyendo de derecha a izquierda. Si por ejemplo ponemos el valor por default de pi de esta manera:

def area_circulo(pi=3.14, radio): -> Vamos a obtener un error de argumento. 


 Tambien pudiesemos poner un nuevo valor como argumento a ese parametro que ya tiene un valor asignado, por ejemplo podemos agregar un valor de pi mas preciso que el que ya tiene asignado en el parametro. Ejm:

def area_circulo(radio, pi=3.14):
    return pi * (radio ** 2)

resultado = area_circulo(10, 3.141592)
print(resultado)

En consola: 314.1592

--> Sin importar que la funcion ya tenga en el parametro un valor asignado, si ponemos un nuevo valor como argumento este sera utilizado. 



 Nosotros podemos asignar valores a los parametros utilizando el nombre de los parametros. Ejm:

def area_circulo(radio, pi=3.14):  --> Tengo 2 parametros con sus nombres. 

 Sabemos que los argumentos se asignan con respecto a su posicion, el 1er argumento con el 1er parametro, y el 2do con el 2do, etc... Sin embargo en Python puedo asignar valores a los parametros en los argumentos por su nombre. Ejm: 

def area_circulo(radio, pi=3.14):
    return pi * (radio ** 2)

resultado = area_circulo(radio=10, pi=3.141592)
print(resultado)

-> Al utilizar los nombres de los parametros en los argumentos puedo moverlos de posicion, ya no importa que el primero vaya con el primero y el segundo con el segundo, etc. Puedo mover su posicion en los argumentos. 
Ejm:

def area_circulo(radio, pi=3.14):
    return pi * (radio ** 2)

resultado = area_circulo(pi=3.141592, radio=10)
print(resultado)


RECUERDA EL METODO FORMAT. 

--> En el primer ejemplo que vimos de funciones no tenia parametros porque era un ejemplo muy basico de una funcion que dependia directamente de los valores que asignaba el usuario, era un funcion muy poco abstracta. 


----------------------------------------------------------------------------------------------------------------

#5) CLASE 5 - ARGS.

 Con Python podemos crear funciones las cuales pueden recibir una "n" cantidad de argumentos.    

 Por ejemplo utilizando la funcion print, seremos capaces de imprimir en consola una "n" cantidad de valores, basta con colocar dentro de los parentesis separados por comas todos aquellos valores los cuales queramos imprimir en consola. Ejm:

print("string", 10, 14.5, True)

 Este tipo de funciones son muy utiles sobre todo para aquellos casos en donde no sepamos de antemano la cantidad exacta de valores que vayamos a utilizar. 


 
 A continuacion vamos a aprender a crear funciones las cuales puedan recibir una "n" cantidad de argumentos. 

 Vamos a crear una funcion la cual nos permita calcular el promedio de un listado de numero enteros. Mi funcion tendra por nombre: promedio. Y poseera un parametro que seria el listado de numeros enteros. Y posteriormente vamos a retornar el promedio de dicho listado, para ello podemos hacer uso de dos funciones que serian la funcion sum dividida entre la funcion len.

-> La funcion sum() nos permite obtener como resultado la suma total de todos los elementos dentro de una coleccion, ya sea dentro de un listado o dentro de una tupla. Como necesitamos conocer la suma de todos los elementos dentro del listado, paso como argumento listado. 

-> La funcion len() nos permite obtener la cantidad de elementos dentro de listado. 

def promedio(listado):
    return sum(listado) / len(listado)  -> Con esta sencilla linea de codigo nosotros podemos conocer el promedio de un listado de numeros enteros. 

 Hacemos el llamado de la funcion y pasamos como argumento un listado de numero enteros. Almacenamos el promedio en una variable llamada: resultado. Que posteriormente vamos a imprimir.

Ejm completo:

def promedio(listado):
    return sum(listado) / len(listado)

resultado = promedio([10, 10, 5, 7, 10])
print(resultado)

En consola: 8.4

--> Definimos una funcion la cual lo unico que hace es calcular el promedio de nuestros listado. 



 Que pasa si nosotros ya no colocamos como ARGUMENTO de la funcion un listado, si no que colocamos directamente todos aquellos valores de los cuales queremos obtener el promedio???? 
Ejm: 

def promedio(listado):
    return sum(listado) / len(listado)

resultado = promedio(10, 10, 5, 7, 10) -> sin las llaves
print(resultado)

En consola: Nos da error que indica que la funcion promedio unicamente toma un argumento porque hay un solo parametro. 


 Entonces si deseeamos que esta funcion pueda recibir una "n" cantidad de argumentos debemos apoyarnos de un * delante de nuestro parametro (sin espacios, por convencion). 

def promedio(*listado):
    return sum(listado) / len(listado)

resultado = promedio(10, 10, 5, 7, 10)
print(resultado)

--> Al hacer esto le estamos diciendo a Python que todos los argumentos utilizados a la hora de llamar a una funcion van a servir para generar un tupla, tupla que se va a asignar al parametro que tenga asterisco. 
 Podemos confirmar esto imprimiendo en consola el objeto per se y su tipo. 

def promedio(*listado):
    print(listado)
    print(type(listado))

    return sum(listado) / len(listado)

resultado = promedio(10, 10, 5, 7, 10)
print(resultado)

En consola:
(10, 10, 5, 7, 10)
<class 'tuple'>
8.4


 Entonces, de esta forma es que nosotros podemos crear funciones que puedan recibir una "n" cantidad de argumentos. 


 OJO, por convencion de la comunidad Python TODOS aquellos parametros los cuales posean * , deben llamarse: args. 

def promedio(*args):
    print(args)
    print(type(args))

    return sum(args) / len(args)

resultado = promedio(10, 10, 5, 7, 10)
print(resultado)


----------------------------------------------------------------------------------------------------------------

#6) CLASE 6 - ARGS PT2.

 Debemos tener presente que el uso del asterisco no nos limita para usar otros parametros. 

 Vamos a crear otra funcion que tendra por nombre: combinacion con tres parametros y vamos a imprimir en consola esos parametros, finalmente hacemos el llamado de la funcion pasando sus respectivos valores. 

def combinacion(p1, p2, p3):
    print(p1)
    print(p2)
    print(p3)

combinacion(10, 20, 1)

En consola: 
10
20
1

--> Los argumentos se han asignado con respecto a su posicion. El primer argumento (10), para el primer parametro (p1)... Y asi sucesivamente.


 Si nosotros colocamos * delante de alguno de los parametros, le vamos a indicar a Python que todos los argumentos que fueron utilizados al momento de llamar a la funcion serviran para generar una tupla, tupla la cual se va a asignar al parametro que tenga asterisco, y por convencion ese parametro debe llamarse: args. Ejm:

def combinacion(p1, p2, *args):
    print(p1)
    print(p2)
    print(args)

combinacion(10, 20, 1)

En consola:
10
20
(1,)

--> La tupla posee un solo elemento que seria el tercer argumento. 


 Aniadiendo mas valores a ese argumento:

def combinacion(p1, p2, *args):
    print(p1)
    print(p2)
    print(args)

combinacion(10, 20, 1, 2, 4, 5, 6, 7, 8)

En consola:
10
20
(1, 2, 4, 5, 6, 7, 8)

--> Visualizamos que ahora el parametro args es una tupla de 7 elementos. 


 Tambien puedo anadir un 4to parametro el cual sea completamente opcional, recordando que todos los parametros opcionales con un valor por default van a la derecha y deben ir sin espacios despues del igual. Ejm:

def combinacion(p1, p2, *args, p4=500):


 Pero si deseo agregarle un valor para p4, un valor utilizando los argumentos debo apoyarme de los nombres de los parametros, ejm:

def combinacion(p1, p2, *args, p4=500):
    print(p1)
    print(p2)
    print(args)
    print(p4)

combinacion(10, 20, 1, 2, 4, 5, 6, 7, 8, p4=1000)

En consola:
10
20
(1, 2, 4, 5, 6, 7, 8)
1000

--> Si lo hacia sin el nombre, se agregaba el valor de 1000 a la tupla.


IMPORTANTE. Por covencion y por buenas practicas, cuando nuestro programa posea dos o mas funciones, vamos a separar las funciones con dos saltos. Ejm: 

def promedio(*args):
    return sum(args) / len(args)


def combinacion(p1, p2, *args, p4=500):
    print(p1)
    print(p2)
    print(args)
    print(p4)

combinacion(10, 20, 1, 2, 4, 5, 6, 7, 8, p4=1000)

----------------------------------------------------------------------------------------------------------------

#7) CLASE 7 - KWARGS.

 Otra forma de pasar diferentes valores al momento de llamar a una funcion es utilizando doble asterisco **. 
 Solo que al pasar doble asterisco estamos dejando de lado trabajar con tuplas y nos concentraremos en trabajar con diccionarios. Por convencion de la comunidad Python el parametro que reciba doble asterisco tendra por nombre: kwargs.

 Vamos a crear una funcion que tendra por nombre usuarios, esta funcion va a recibir diferentes calificaciones de diferentes usuarios y a continuacion vamos a imprimir en consola el objeto (el parametro) y su tipo.  

def usuarios(**kwargs): 
    print(kwargs)
    print(type(kwargs))

 -> Ahora vamos a llamar a la funcion pero no vamos a colocar directamente los argumentos, sino que nos apoyaremos de parametros. Ejm:

usuarios(eduardo=[10, 10, 8], fernando=[10, 9, 9]) 

-> En este caso estoy llamando a la funcion, pasando dos listas para dos parametros. Los parametros son: eduardo y fernando. 


Ejemplo completo:

def usuarios(**kwargs): 
    print(kwargs)
    print(type(kwargs))

usuarios(eduardo=[10, 10, 8], fernando=[10, 9, 9]) 

En consola:
{'eduardo': [10, 10, 8], 'fernando': [10, 9, 9]}
<class 'dict'>

--> Encontramos nuestro diccionario, diccionario que posee dos elementos con sus correspondientes dos llaves. Los parametros son utilizados como llaves y los valores son los valores que hemos asignado. 

 Recordar que por convencion siempre que asignemos un valor a un parametro lo haremos todo junto, sin ningun tipo de espacio. 

 Nosotros podemos pasar una "n" cantidad de parametros y a partir de ellos se va a generar un diccionario el cual se va a asignar al parametro que tenga doble asterisco, parametro que por convencion se llamara: kwargs.



 Entonces, de estas formas es como nosotros podemos pasar diferentes valores al momento de llamar a una funcion. 

*args --> Tupla
**kwargs --> Dict


 Tambien podemos crear funciones que posean asterisco y doble asterisco. Ejm:

def combinacion(*args, **kwargs):
    print(args)
    print(kwargs)

--> Al momento de hacer el llamado lo que debemos hacer es combinar los argumentos con los parametros. O sea, le asignamos argumentos a el primero parametro y al momento de trabajar con los kwargs lo hacemos por medio de los parametros. Ejm:

combinacion(1, 2, 3, 4, 5, cody=True, curso="python")

-> Los numeros: 1, 2, 3, 4, 5 corresponden a args y despues de los numeros (los parametros) corresponden a kwargs.

Ejemplo completo:

def combinacion(*args, **kwargs):
    print(args)
    print(kwargs)

combinacion(1, 2, 3, 4, 5, cody=True, curso="python")

En consola:
(1, 2, 3, 4, 5)
{'cody': True, 'curso': 'Python'}

--> Visualizamos la tupla del 1 al 5, y visualizamos el diccionarion con dos elementos. 


----------------------------------------------------------------------------------------------------------------

#8) CLASE 8 - SCOPES. = ALCANCES

 Ahora veremos como se comportan las variables tanto dentro como fuera de las funciones.
 Vamos a trabajar con el siguiente programa:

animal = "Leon"

def imprimir_animal():
    print(animal)

imprimir_animal()

En consola: Leon

-> El programa lo unico que hace es imprimir en consola el valor de una variable a traves de una funcion. 


 MODIFICAREMOS LIGERAMENTE LA FUNCION:

animal = "Leon"

def imprimir_animal():
    animal = "Ballena"

    print(animal)

imprimir_animal()

En consola: Ballena

--> Al ver este resultado pensamos que la funcion ha modificado el valor de la variable animal, pero NO es asi, podemos confirmar ello si imprimimos en consola despues de ejecutar la funcion, la variable animal.
Ejm: 


animal = "Leon"

def imprimir_animal():
    animal = "Ballena"

    print(animal)

imprimir_animal()

print(animal)

En consola:
Ballena
Leon

--> Visualizamos en consola tanto a Ballena como a Leon. Esto se debe al tema de scope. 

 Para Python la variable animal con el valor de Leon y la variable animal con el valor de Ballena, son objetos completamente diferentes, ya que estas variables fueron creadas en scopes diferentes, por lo tanto tienen alcances diferentes.  

 La variable animal con el valor Leon, al no ser creada dentro de un bloque sera considerada como una variable global. 
 LAS VARIABLES GLOBALES pueden ser consideradas dentro de cualquier bloque, ya sea un bloque de una funcion, un bloque de una condicion o un bloque de un ciclo. Si por ejemplo yo elimino la variable que contiene ballena, la funcion estara utilizando la variable global.  


 La variable con el valor Ballena, al ser creada dentro de un bloque la conoceremos como una variable local. Una VARIABLE LOCAL unicamente puede ser creada dentro del bloque donde fue creada. 

 
 En el caso del ejemplo, para Python animal que contiene Leon y animal que contiene Ballena son objetos diferentes. Objetos los cuales fueron creados en scopes diferentes, por lo tanto poseen alcances diferentes.


 Pudiesemos confirmar que son objetos distintos si imprimimos en consola el id de los objetos. 

 En Python para nosotros poder distinguir un objeto de otro podemos hacer uso de su identificador unico y esto lo hacemos por medio de su id y utilizando la funcion id. Ejm, vamos a imprimir mediante la funcion id el id del objeto animal.:

animal = "Leon"

def imprimir_animal():
    animal = "Ballena"

    print(animal)
    print(id(animal))

imprimir_animal()

print(animal)
print(id(animal))

En consola: 
Ballena
1252642597168
Leon
1252642597104

--> Verificamos que son objetos diferentes. 


 Si por ejemplo creo otra variable dentro de la funcion, que sera: tipo = "Mamifero" , y intento imprimir en consola el valor de esa variable pero fuera de la funcion me va a dar error ya que una vez el bloque finzaliza entonces todas las variables que fueron creadas alrededor de ese bloque se procederan a destruir, debo hacer la impresion dentro de la funcion, de la siguiente manera: 

animal = "Leon"

def imprimir_animal():
    animal = "Ballena"

    tipo = "Mamifero"

    print(animal)
    print(id(animal))

    print(tipo)

imprimir_animal()

print(animal)
print(id(animal))



 Si deseamos modificar el valor de una variable global dentro de un bloque, haremos uso de la palabra global. Ejm, vamos a modificar dentro de la funcion el valor de la variable global.

Para ello debemos:  
1- Primero debemos indicarle a Python que no deseamos crear una variable con el mismo nombre sino que vamos a utilizar la variable glogal, para ello colocamos la palabra global seguido de la variable global la cual querramos modificar. -> De esta forma le indicamos a Python que no vamos a crear una variable local sino que vamos a trabajar con la variable global. 

2- Luego ya podemos modificar la variable animal dentro de la funcion, escribimos la variable con su nuevo valor.

Resumen de pasos: Indico que voy a modificar la variable global y posteriormente modifico su valor.  

animal = "Leon"

def imprimir_animal():
    global animal
    animal = "Ballena"

    print(animal)
    print(id(animal))


imprimir_animal()

print(animal)
print(id(animal))

En consola:
Ballena
1927997827312
Ballena
1927997827312

--> Visualizamos ballena dos veces y confirmamos por medio de su id que ahora estamos trabajando con el mismo objeto. 


Entonces, finalmente ya sabemos que el alcance que tiene una variable depende completamente de su scope, de donde fue creada. Si fue creada fuera de un bloque la conoceremos como una variable global y esta variable global puede ser utilizada en cualquier parte del programa, ya sea dentro de bloques o fuera de. Y por otra parte las variables que fueron creadas dentro de un bloque, unicamente pueden ser utilizadas dentro de dicho bloque. 


----------------------------------------------------------------------------------------------------------------

#9) CLASE 9 - FUNCIONES ANIDADAS.


 Al igual que con las condiciones y con los ciclos, las funciones tambien pueden ser anidadas, o sea las funciones pueden poseer a su vez otras funciones.

 Ejm: Vamos a crear una funcion la cual nos permita simular una transaccion bancaria. 

PASOS:
 
- La funcion va a tener por nombre: operacion.

def operacion():


- Dentro de la funcion voy a definir dos funciones mas. Una funcion me permitira simular el deposito a una cuenta y otra funcion me permitira simular el retiro a una cuenta. Creo estas dos nuevas funciones como nuevos bloques dentro de la funcion operacion.

 La funcion deposito poseera dos parametros, que seran: cantidad y balance. Esta funcion lo unico que hara es suma cantidad mas balance. 

 La funcion retiro ira posteriormente fuera de la funcion deposito pero obviamente dentro de la funcion operacion. Esta funcion tendra exactamente los mismos parametros que la funcion deposito pero la diferencia esta en que nos va a restar. Por supuesto vamos a condicionar la funcion retiro, que la cantidad que deseemos retirar sea menor o igual a la cantidad total de la cuenta, o sea al balance total. Si cantidad es menor o igual a balance, entonces podremos retirar, en caso contrario vamos a retornar none.


def operacion():
    def deposito(cantidad, balance):
        return cantidad + balance


    def retiro(cantidad, balance):
        if cantidad <= balance:
            return balance - cantidad
        else:
            return None


- Finalmente puedo hacer el llamado a la funcion operacion. 


def operacion():

    def deposito(cantidad, balance):
        return cantidad + balance


    def retiro(cantidad, balance):
        if cantidad <= balance:
            return balance - cantidad
        else:
            return None

operacion()

En consola: No ocurre ningun tipo de error pero tampoco tengo ningun tipo de resultado, esto se debe principalmente a que dentro de la funcion no se realiza ningun tipo de operacion, unicamente se definen las funciones y listo, en ningun momento se mandan a llamar.
 
 Lo que podemos hacer dentro de la funcion es simplemente imprimir en consola el llamado, el resultado del llamado a las funciones, agregandoles obviamente los argumentos. 

    
def operacion():

    def deposito(cantidad, balance):
        return cantidad + balance


    def retiro(cantidad, balance):
        if cantidad <= balance:
            return balance - cantidad
        else:
            return None

    print(deposito(10, 20))
    print(retiro(50, 30))


operacion()

En consola: 
30 
None

--> Ahora nuestra funcion esta llamando a las funciones que se encuentran dentro de ella.  



 Entonces como podemos observar, definir funciones dentro de otras funciones es sencillo, solo debemos definir la "n" cantidad de funciones que vamos a utilizar y recordar separarlas entre si con dos espacios. Y estas funciones a su vez pudiesen tener otras funciones anidadas de una "n" cantidad de niveles. 


-------------------REFACTOR:
 Ahora vamos a implementar un pequeno refactor a la funcion operacion. 

- Vamos a definirle a la funcion tres parametros, que seran: cantidad, balance y tipo que este ultimo tendra el valor por default de deposito. 

- Luego vamos a ejecutar una de estas dos funciones dependiendo de el tercer parametro. Entonces debajo de las funciones y dentro de la funcion operacion vamos a colocar la condicion if.

- La condicion if dice: si tipo es igual a deposito entonces ejecutamos y retornamos lo que la funcion deposito nos retorne, pasando como argumento cantidad y balance. En caso contrario (elif), si tipo es igual a retiro entonces vamos a retornar lo que la funcion retiro nos retorne, pasando como argumento cantidad y balance.

-> Entonces dentro de la funcion operacion yo defino dos funciones que posteriormente utilizando un parametro condiciono su ejecucion y en ambos casos voy a retornar lo que las funciones me retornen.

- Finalmente hago el llamado a la funcion con los argumentos que le asigne y listo, ya con estos valores obviamente la funcion a saber si es deposito o retiro. Y almacenamos el llamado de esa funcion en una variable e imprimimos en consola.


def operacion(cantidad, balance, tipo="deposito"):

    def deposito(cantidad, balance):
        return cantidad + balance


    def retiro(cantidad, balance):
        if cantidad <= balance:
            return balance - cantidad
        else:
            return None

    if tipo == "deposito":
        return deposito(cantidad, balance)
    elif tipo == "retiro":
        return retiro(cantidad, balance)

resultado = operacion(10, 30)
print(resultado)

En consola: 
40

--> Que seria 10 + 30. 


Pero si yo coloco en los argumentos: 10, 30, "retiro" 
visualizamos 20, que seria su contraparte, la resta. Ejm:


def operacion(cantidad, balance, tipo="deposito"):

    def deposito(cantidad, balance):
        return cantidad + balance


    def retiro(cantidad, balance):
        if cantidad <= balance:
            return balance - cantidad
        else:
            return None

    if tipo == "deposito":
        return deposito(cantidad, balance)
    elif tipo == "retiro":
        return retiro(cantidad, balance)

resultado = operacion(10, 30, "retiro")
print(resultado)

En consola: 
20

--> Es la resta porque al poner retiro elimino el valor por default que es deposito. 


FINALMENTE, podemos tener funciones dentro de funciones y lo comun es tener funciones anidadas de dos niveles, como en el ejemplo. Podemos tener funciones anidadas de "n" niveles pero no es recomendado porque puede complicar nuestro codigo. 


----------------------------------------------------------------------------------------------------------------

#10) CLASE 10 - CIUDADANOS DE PRIMERA CLASE 

 En Python las funciones son ciudadanos de primera clase o tambien conocidas como ciudadanos de primer orden. 
Esto quiere decir que las funciones pueden ser asignadas a variables, pueden ser utilizadas como argumentos para otras funciones e inclusive funciones pueden retornar funciones. 

Ejemplo:

- En este caso vamos a definir una funcion que tiene por nombre centigrados_a_farhenheit, una funcion que a partir de ciertos grados centigrados va a retornar su equivalente a grados farhenheit, para ello aplicamos la formula que me hace la conversion de la misma. 

- Finalmente ya definida la funcion, hacemos uso de la funcion. Recordando que podemos hacer uso de la misma la "n" cantidad de veces que nosotros deseemos, en este caso vamos a imprimirla en consola 3 veces, con argumentos distintos.   

def centigrados_a_farhenheit(grados):
    return grados * 1.8 + 32  

print(centigrados_a_farhenheit(10))
print(centigrados_a_farhenheit(-1))
print(centigrados_a_farhenheit(8))

En consola:
50.0
30.2
46.4

--> Visualizo sus correspondientes resultados. 

 Nosotros vamos a llamar a la funcion siempre y cuando sepamos cuando utilizarla. SIN EMBARGO habra ocasiones en las que nosotros sepamos que vamos a utilizar una funcion pero nos sepamos exactamente cuando.

CASO CUANDO NO SEPAMOS QUE VAMOS A UTILIZAR UNA FUNCION PERO EXACTAMENTE NO SABEMOS CUANDO LA VAMOS A UTILIZAR: 
En estos casos lo recomendable es que almacenemos la funcion en una variable y a partir de la variable hagamos el llamados bajo demanda. 

ALMACENANDO UNA FUNCION EN UNA VARIABLE:

- Creamos el nombre de la variable y despues del igual colocamos el nombre de la funcion la cual querramos almacenar.  Ejm:

mi_funcion = centigrados_a_farhenheit


Ejm total:

def centigrados_a_farhenheit(grados):
    return grados * 1.8 + 32 
 

mi_funcion = centigrados_a_farhenheit

--> De esta forma queda almacenada la funcion en la variable mi_funcion. 


Si de hecho imprimimos en consola el tipo de la varible, queda asi: 

def centigrados_a_farhenheit(grados):
    return grados * 1.8 + 32 
 

mi_funcion = centigrados_a_farhenheit

print(type(mi_funcion))

En consola: 
<class 'function'>

--> Es de tipo funcion.


 Una vez que la funcion se encuentre almacenada dentro de una variable, para nosotros poder llamar a la funcion ahora nosotros lo haremos a traves de la variable. 

 Colocamos la variable seguida de parentesis y dentro de los parentesis todos aquellos argumentos necesarios para ejecutar la funcion. Ejm para imprimir en consola: print(mi_funcion(10))


def centigrados_a_farhenheit(grados):
    return grados * 1.8 + 32 
 

mi_funcion = centigrados_a_farhenheit

print(type(mi_funcion))

print(mi_funcion(10))

En cosola:
<class 'function'>
50.0

--> Ahora estamos llamando a la funcion a traves de una variable. 


OJO: Al momento de crear la variable con la funcion, colocar despues de el igual unicamente el nombre de la funcion, NO DEBEMOS COLOCAR LOS PARENTESIS, ya que si colocamos parentesis Python va a tomar como que estamos llamando a la funcion. 


----------------------------------------------------------------------------------------------------------------

#11) CLASE 11 - FUNCIONES LAMBDA

 Una funcion lambda tambien conocida como una funcion anonima, no es mas que una funcion la cual es expresada en una sola linea de codigo ademas de no poseer un nombre, ya que comunmente este tipo de funciones realizan tareas muy pequenas. Ejm:

Aca tenemos la funcion centigrados_a_farhenheit, la cual realiza una tarea muy sencilla que de grados centigrados retorna el equivalente a farhenheit:

def centigrados_a_farhenheit(grados):
    return grados * 1.8 + 32


mi_funcion = centigrados_a_farhenheit

print(type(mi_funcion))

print(mi_funcion(10))  


--> Podemos convertir esta funcion a una funcion lambda, a una funcion la cual no posea un nombre. Pasos:

- Asignamos directamente la funcion a una variable.
- Despues del igual hacemos uso de la palabra reservada lambda. 
- Posteriormente despues de la palabra lambda, colocamos los parametros que la funcion necesite y los separamos con una coma. 
- Despues de los parametros haremos uso de dos puntos :.
- Posteriormente en la misma linea vamos a colocar el cuerpo de la funcion, la operacion en la cual nosotros queremos realizar y por default la operacion lambda va a retornar el resultado de dicha operacion, asi que no es necesario utilizar la palabra reservada return. La funcion lamnda siempre va a retornar la linea de codigo que sea ejecutada. 

funcion_grados = lambda grados : grados * 1.8 + 32

- Como la funcion ya se encuentra almacenada dentro de una variable, para que nosotros podamos llamar a esta funcion colocamos nuestra variable seguida de parentesis y dentro de los parentesis todos aquellos argumentos obligatorios para que la funcion pueda ejecutarse.  

Ejm completo:
  
funcion_grados = lambda grados : grados * 1.8 + 32

print(funcion_grados(10))

En consola:
50.0


 En este caso la funcion lambda es mas o menos sencilla pero nosotros podriamos complicarla usando mas o menos parametros, ejemplos:

- Funcion lambda sin parametros: 
sin_parametros = lambda : True

- Funcion lambda con parametros por default:
parametros_default = lambda p1=10, p2=20, p3=30 : p1 + p2 + p3

- Tambien podemos trabajar con asterisco o doble asterisco:
asterisco = lambda *args, **kwargs: len(args) + len(kwargs)


Importante, siempre que nosotros creemos una funcion lambda obligatoriamente la funcion debe poseer un cuerpo, por lo menos debe haber una expresion la cual se deba ejecutar, no importa que sea una expresion muy sencilla como imprimir en consola, lo importante es que si o si debe haber una expresion que se deba ejecutar, de igual forma no importa si dicha expresion retorna o no un valor. 


----------------------------------------------------------------------------------------------------------------

#12) CLASE 12 - CALLBACKS 


 Los callbacks son funciones las cuales son utilizadas como argumentos para otras funciones, y seran las funciones que reciban estos argumentos las cuales las llamen. 

Por ejemplo vamos a crear una funcion que nos permita obtener el promedio de cualquier listado PERO considerando que calcular el promedio de un listado no es lo suficientemente complejo para que nosotros debamos definir una funcion. Entonces, lo ideal en estos casos es crear una funcion lambda. 

Creando la funcion lambda:
- Colocamos la variable, igual a lambda. 
- Como queremos que la funcion al momento de ser llamada pueda colocar una "n" cantidad de argumentos utilizo *args.
- En el cuerpo de la funcion (despues de los :), vamos a retornar el promedio de esta tupla ya que si recordamos al nosotros anteponer *, el parametro es una tupla. Entonces vamos a sumar todos los elementos dentro de la tupla y posteriormente vamos a dividir sobre la cantidad de elementos. 

promedio = lambda *args : sum(args) / len(args)

print(promedio(10, 10, 9, 8, 7))

En cosola: 8.8

-> Funciona de manera correcta, esta calculando el promedio de una tupla. Y al momento de llamar a la funcion, estamos pasando una "n" cantidad de argumentos. 


Ahora creemos una funcion la cual nos permita conocer si un alumno a aprobado o no la materia, para ello su calificacion debe ser mayor o igual a 7. Ya que es una operacion relativamente sencilla de igual forma estaremos utilizando una funcion lambda. 

PASOS:

- Escribo el nombre de la variable.
- = lambda
- En este caso tendra un parametro obligatorio que seria la calificacion, seguido de los dos puntos. 
- En el cuerpo vamos a retornar verdadedor o falso dependiendo si la calificacion es aprobatoria o no. Para ello utilizamos un operador relacional el cual recordando no dara un valor booleano. Y de igual forma recordar que una funcion lambda va a retornar lo que el cuerpo de la funcion retorne al ejecutarse. 
 
aprobatorio = lambda calificacion : calificacion >= 7

print(aprobatorio(7))

En consola -> Perfecto. 



 Ahora para ver los callbacks en accion, vamos a crear una funcion la cual nos permita ver un mensaje en consola diferente dependiendo de la calificacion de un alumno, para ello esta funcion obligatoriamente va a recibir como argumento las dos funciones anteriores, promedio y aprobatorio. 

 *Como podemos observar en este caso hemos aplicado el refran divide y venceras, hemos creado funciones las cuales realicen tareas muy atomicas, por ejemplo calcular el promedio y saber si un alumno aprueba o no una materia, ahora vamos a crear una funcion la cual combine estas dos funciones anteriores.* 

PASOS:

- Es una funcion compleja por lo tanto la trabajo como una funcion normal. La llamo mostrar_mensaje. 

def mostrar_mensaje():

- Deseo que la funcion reciba como argumento las dos funciones creadas, asi que voy a crear dos parametros. Nota: Utilizo el prefijo func_ unicamente para entender de mejor manera el tipo de dato que es cada parametro. Y finalmente vamos a colocar nuestra tupla de valores como tercer parametro.

def mostrar_mensaje(func_promedio, func_aprobatorio, *args)

- Lo primero que vamos a hacer sera "calcular" el promedio del alumno para eso llamamos a la funcion func_promedio (funcion en donde ya se hizo el calculo) y pasando la "n" cantidad de argumentos utilizados al momento de llamar a esta funcion (los argumentos que utilizamos en la funcion promedio para calcular el promedio), o sea args, pero si coloco solo args estaremos pasando no diferentes argumentos sino una tupla, para nosotros poder desempaquetar esta tupla y pasar una "n" cantidad de argumentos basta con sobreponer *.  

def mostrar_mensaje(func_promedio, func_aprobatorio, *args):
    promedio = func_promedio(*args)

- Posteiormente vamos a condicionar, se lee: Si la funcion aprobatorio pasando como argumento el promedio es verdadero entonces vamos a imprimir en consola... 
Nota: Estamos haciendo uso de algo llamado f string. Que es?? ->  le permiten incluir el valor de las expresiones de Python dentro de una cadena prefijando la cadena con f o F y escribiendo expresiones como {expresion}.

def mostrar_mensaje(func_promedio, func_aprobatorio, *args):
    promedio = func_promedio(*args)

    if func_aprobatorio(promedio):
        print(f"Felicidades, aprobaste la materia con         {promedio}.")
    else:
        print("No aprobaste la materia.")


- Finalmente llamamos a nuestra funcion mostrar_mensaje y pasamos como argumentos nuestras dos funciones y posteriormente la "n" cantidad de argumentos.

def mostrar_mensaje(func_promedio, func_aprobatorio, *args):
    promedio = func_promedio(*args)

    if func_aprobatorio(promedio):
        print(f"Felicidades, aprobaste la materia con         {promedio}.")
    else:
        print("No aprobaste la materia.")

mostrar_mensaje(promedio, aprobatorio, 10, 10, 8, 7, 7)

En consola: Felicidades, aprobaste la materia con 8.4.

Listo, con esto hemos dividido el problema en pequenas operaciones. Una funcion calcula el promedio y la otra funcion nos permite conocer si el alumno o no ha aprobado la materia. 


Los callbacks son de mucha utilidad principalmente en programas los cuales son modularizables, donde facilmente podamos reemplazar una pieza de software por otra. Por ejemplo si yo creo una tercera funcion llamada es_aprobatorio con otras condiciones diferentes a las de la funcion aprobatorio y si cuando voy a hacer el llamado de la funcion al final del codigo coloco esta nueva funcion en el lugar de la funcion aprobatorio, el codigo me funciona igual pero el resultado cambiara. Ejm completo: 

promedio = lambda *args : sum(args) / len(args)

aprobatorio = lambda calificacion : calificacion >= 7

def es_aprobatorio(calificacion):
    return calificacion >= 90

def mostrar_mensaje(func_promedio, func_aprobatorio, *args):
    promedio = func_promedio(*args)

    if func_aprobatorio(promedio):
        print(f"Felicidades, aprobaste la materia con         {promedio}.")
    else:
        print("No aprobaste la materia.")

mostrar_mensaje(promedio, es_aprobatorio, 10, 10, 8, 7, 7)

En consola: 
No aprobaste la materia.

--> Seguimos calculado el promedio pero utilizando un metodo diferente y con la misma funcion principal. 

----------------------------------------------------------------------------------------------------------------

#13) CLASE 13 - VARIABLES NO LOCALES.

 Este tema se encuentra estrechamente relacionado con el tema de funciones anidadas y alcances de las variables, por lo tanto vamos a hacer un repaso rapido de esos temas con la siguiente funcion:

def funcion_principal():
    a = "a"
    b = "b"

    def funcion_anidada():
        c = "c"

        print(a)
        print(b)

    funcion_anidada()
    print(c)

funcion_principal()

En consola: Me muestra a y b pero con c me da un error, me indica que c no se encuentra definida. 

--> El error de c se debe a que es una variable local y esta unicamente puede ser utilizada dentro del bloque donde fueron creadas, tiene una alzance local. Por otro lado las variables a y c son tambien variables locales ya que tambien fueron creadas dentro de un bloque sin embargo estas variables locales se encuentran con un scope superior, tienen un alcance mucho mayor ya que se encuentran creadas en un bloque superior por lo tanto pueden ser utilizadas en bloques inferiores. 

 Recordemos que existen variables globales, y que estas no son creadas dentro de una funcion y pueden ser utilizadas en cualquier parte del programa. Ejm:

e = "e"  # -> Variable global

def funcion_principal():
    a = "a"  # -> Variables locales
    b = "b"

    def funcion_anidada():
        c = "c"  # -> Variable local

        print(a)
        print(b)

        print(e)

    funcion_anidada()
    #print(c)

funcion_principal()

En consola: 
a
b
e

--> Al ser e una variable global, puedo hacer uso de esta en cualquier parte del programa.


 Ahora, que pasa si nosotros quisieramos modificar el valor de una variable local dentro de un bloque anidado???

 Por ejemplo que pasa si yo deseo modificar el valor de la variable b creada en la funcion principal dentro de la funcion anidada???
--> Al hacerlo y volver a imprimir b en consola me muestra el nuevo valor anadido pero esto no quiere decir que logre modificar el valor de b, para Python ahora van a existir dos variables b ya que estas dos variables fueron creadas en scopes diferentes. Para demostrarlo podemos imprimir el id de cada una de ellas. 

e = "e"

def funcion_principal():
    a = "a"
    b = "b"

    def funcion_anidada():
        c = "c"
        b = "Cambio de valor"

        print(a)
        print(b)
        print(id(b))

        print(e)

    funcion_anidada()
    print(b)
    print(id(b))
    #print(c)

funcion_principal()

En consola:
a
Cambio de valor
1736451565808
e
b
140722617308960

--> Podemos verificar que ambas variables b tienen son objetos diferentes. 


 Si nosotros quisieramos modificar el valor de una variable local que se encuentra en un scope superior vamos a hacer uso de la palabra reservada nonlocal. 

Debemos hacer escribir nonlocal seguido de la variable local que se encuentra en un nivel superior la cual queramos modificar, esto lo coloco en una linea anterior al nuevo valor que le voy a agregar a la variable. Ejm:

nonlocal b
b = "Cambio de valor"

--> Con esto le estamos indicando a Python que no vamos a crear una nueva variable, sino que vamos a utilizar la variable local que se encuentra en un nivel superior. 


Ejm completo:


e = "e"

def funcion_principal():
    a = "a"
    b = "b"

    def funcion_anidada():
        c = "c"

        nonlocal b
        b = "Cambio de valor"

        print(a)
        print(b)
        print(id(b))

        print(e)

    funcion_anidada()
    print(b)
    print(id(b))
    #print(c)

funcion_principal()

En consola:
a
Cambio de valor
2069425170672
e
Cambio de valor
2069425170672

--> Ambos objetos son lo mismo. 


----------------------------------------------------------------------------------------------------------------

#14) CLASE 14 - RETORNAR FUNCIONES. 

 En Python las funciones son ciudadanos de primera clase, esto quiere decir que funciones pueden retornar funciones. 

Ejemplo, vamos a definir una funcion la cual tendra por nombre saludar, esta funcion a su vez poseera una funcion anidada la cual tendra por nombre mostrar_mensaje y esta funcion unicamente va a imprimir en consola un pequeno mensaje. 

def saludar():

    def mostrar_mensaje():
        print("Hola, nos encontramos en el curso de               Python.")


Ahora, hagamos que la funcion saludar retorne a la funcion mostrar_mensaje. Para ello, colocamos return seguido del nombre de la funcion que nosotros queremos retornar, en este caso es mostrar_mensaje.


def saludar():

    def mostrar_mensaje():
        print("Hola, nos encontramos en el curso de               Python.")

    return mostrar_mensaje

-> Listo, de esta forma es que nosotros podemos crear funciones que retornen a otras funciones. En este caso estamos retornando nuestra funcion anidada. 

- Ahora hagamos el llamado a la funcion. En este caso vamos a guardar ese llamado en la variable respuesta. 



def saludar():

    def mostrar_mensaje():
        print("Hola, nos encontramos en el curso de               Python.")

    return mostrar_mensaje

respuesta = saludar()
print(respuesta)

En consola:
<function saludar.<locals>.mostrar_mensaje at 0x000001DF7DF88C20>

--> Visualizamos que el objeto es un objeto de tipo funcion, muy puntualmente la funcion mostrar_mensaje y que es una funcion que le pertenece a saludar. Con esto confirmamos que la funcion saludar esta retornando a la funcion anidada. 

- Como sabemos, si nosotros quisieramos llamar a una funcion a traves de una variable, debemos colocar la variable seguida de parentesis y dentro de los parentesis todos aquellos argumentos para que la funcion se ejecute de forma correcta. En este caso como la funcion mostrar_mensaje no posee parametro alguno no sera necesario colocar ningun tipo de argumento. Solo llamamos a la funcion saludar con su variable respuesta.


def saludar():

    def mostrar_mensaje():
        print("Hola, nos encontramos en el curso de               Python.")

    return mostrar_mensaje

respuesta = saludar()

respuesta()

En consola:
Hola, nos encontramos en el curso de Python.

--> Podemos observar como nuestra funcion saludar esta retornando una funcion la cual facilmente podemos almacenar en una variable y para que nosotros podamos llamar a esta funcion a traves de la variable, colocamos nuestra variable y parentesis, dentro de los parentesis los argumentos. 


 Entonces recordemos que en Python las funciones son ciudadanos de primera clase, esto quiere decir que funciones son asignadas a variables, funciones pueden ser utilizadas como argumentos y funciones pueden retornar otras funciones. 



----------------------------------------------------------------------------------------------------------------

#15) CLASE 15 - CLOSURES. 

 Un closure no es mas que una funcion la cual puede generar de forma dinamica a otra funcion y esta nueva funcion puede acceder a las variables locales aun cuando la primera haya finalizado. Ejemplo:

- Tenemos la siguiente funcion que se llama saludar, funcion que posee unicamente un parametro llamado username, mediante este parametro he creado una nueva variable llamada mensaje, variable que es local. 

def saludar(username):
    mensaje = f"Hola {username}"


- Posteriormente he definido la funcion mostrar_mensaje, una funcion anidada. Esta funcion lo unico que hace es imprimir en consola el valor de la variable. Y finalmente la funcion saludar retorna la funcion anidada.

    def mostrar_mensaje():
        print(mensaje)

        return mostrar_mensaje


- Fuera de la funcion he creado la variable username y la utilizo al momento de llamar a la funcion saludar, almaceno la respuesta por parte de la funcion en respuesta, que seria la funcion mostrar_mensaje y posteriormente una vez que la funcion saludar finaliza hago el llamado a dicha funcion. 

username = "Cody"
respuesta = saludar(username)

respuesta()

----------------------------------------

EJEMPLO COMPLETO:

def saludar(username):
    mensaje = f"Hola {username}"


    def mostrar_mensaje():
        print(mensaje)

    return mostrar_mensaje     

username = "Cody"
respuesta = saludar(username)

respuesta()


En consola:
Hola Cody

--> Podemos observar que en toda esta ejecucion sucede algo muy interesante. Lo interesante de todo esto es que la funcion mostrar_mensaje al momento de su llamado con respuesta(), aun pueda acceder a las variables locales de la funcion saludar. En este caso la funcion mostrar_mensaje imprime en consola la variable local mensaje.
 Pero si recordamos las variables locales son todas aquellas variables que se crean dentro de un bloque y unicamente pueden ser utilizadas dentro de ese bloque, ya que una vez ese bloque finalice las variables seran destruidas. En este caso "visualizamos" la excepcion a la regla, ya que la funcion saludar al momento de su llamado crea el bloque, se crea la variable y posteriormente se utiliza cuando la funcion ya ha finalizado. A esto se le conoce como un closure, la funcion saludar es un closure ya que retorna una funcion la cual puede acceder a las variables locales aun cuando la primera ya haya finalizado. 


Que pasa si nosotros creamos una variable username global con un nuevo valor????????? por ejemplo:

def saludar(username):
    mensaje = f"Hola {username}"


    def mostrar_mensaje():
        print(mensaje)

    return mostrar_mensaje     

username = "Cody"
respuesta = saludar(username)

username = "Eduardo"  <--* Nueva variable global.

respuesta()

En consola: 
Hola Cody

--> En consola seguimos visualizando Hola Cody, ya que de cierta manera la funcion mostrar mensaje "tiene memoria", puede acceder a las variables locales aun cuando estas hayan sido creadas en una funcion que ya haya finalizado. 



----------------------------------------------------------------------------------------------------------------

#16) CLASE 16 - DECORADORES  


 A traves de los decoradores seremos capaces de reducir lineas de codigo duplicadas, haremos que nuestro codigo sea aun mas legible, facil de testear, facil de mantener y sobre todo tendremos un codigo mucho mas Pythonico.  

 UN DECORADOR no es mas que una funcion la cual toma como input (como valor de entrada) una funcion y a su vez retorna otra funcion. Al momento de implementar un decorador estaremos trabajando con por lo menos tres funciones, el input, el output y la funcion principal. 

Para que nos quede mas claro vamos a nombrar estas funciones como a, b y c.

a -> La funcion principal (Decorador)
b -> La funcion a decorar
c -> La funcion decorada


 Regularmente vamos a hacer uso de los decoradores siempre que nosotros queramos extender funcionalidades a una funcion, ya sea porque nosotros no podemos modificar la funcion o siplemente no queremos hacerlo. 

En este caso la funcion_a va a recibir como argumento la funcion_b y dara como resultado la funcion_c. 

a(b) -> c

--> De esta forma vamos a extender funcionalidades. Veamos un ejemplo.

Ejemplo - guia:

- Vamos a definir la funcion_a la cual sera mi decorador.

- La funcion_a recibe como argumento la funcion_b la cual es la funcion a decorar.

- Dentro de la funcion_a vamos a crear una segunda funcion, una funcion anidada. Que seria la funcion_c la cual es la funcion decorada. 

- Y la funcion_a va a retornar la funcion decorada

def funcion_a(funcion_b):

    def funcion_c():
        pass

    return funcion_c

--> Esta seria la estructura base para cualquier decorador. Una funcion que recibe como argumento una funcion que a su vez retorna otra funcion. Los decoradores nos permitiran extender funcionalidades a funciones las cuales no podamos modificarlas o simplemente no queramos hacerlo, por ejemplo:

- Vamos a crear la funcion saludar la cual tendra como objetivo imprimir en consola un mensaje.

def saludar():
    print("Hola, nos encontramos en una funcion.")

- Para que nosotros podamos decorar la funcion, para que nosotros podamos extender funcionalidades vamos a hacer lo siguiente: En la parte superior de la funcion escribimo @ seguido del nombre del decorador que queramos utilizar. 

@funcion_a
def saludar():
    print("Hola, nos encontramos en una funcion.")

-> De esta forma le indicamos a Python que funcion_a va a recibir como ARGUMENTO la funcion que estamos decorando, que en este caso seria saludar. 


Ejemplo completo:

def funcion_a(funcion_b):

    def funcion_c():
        pass

    return funcion_c

@funcion_a
def saludar():
    print("Hola, nos encontramos en una funcion.")

saludar()


--> En consola: Si yo ejecuto no pasa absolutamente nada. 

 Esto pasa porque al momento de nosotros llamar a una funcion decorada nosotros no estaremos ejecutando directamente la funcion decorada sino que estaremos ejecutando la funcion que se nos retorne, que seria la funcion_c y en este caso la funcion_c no hace absolutamente nada, es por ello que no visualizamos nada en consola. 

Si por ejemplo hacemos un cambio en la funcion decorada, agregando un print a la funcion_c: 


def funcion_a(funcion_b):

    def funcion_c():
        print("Nos encontramos en la funcion c.")

    return funcion_c

@funcion_a
def saludar():
    print("Hola, nos encontramos en una funcion.")

saludar()


En consola: Nos encontramos en la funcion c

Efectivamente ahora si aparece el mensaje, con esto confirmamos que NO ESTAMOS EJECUTANDO DIRECTAMENTE LA FUNCION A DECORAR SINO QUE ESTAMOS EJECUTANDO LA NUEVA FUNCION, LA FUNCION DECORADA que seria la funcion_c.


 AHORA, para que nosotros podamos ejecutar la funcion a decorar, o sea la funcio_b, basta con que dentro de la funcion_c llamar a la funcion_b (Esto se debe a que la funcion_b es el argumento de la funcion_a, y cuando puse el @funcion_a encima de la funcion saludar le dije a Python que: funcion_a va a recibir como ARGUMENTO la funcion que estamos decorando, que en este caso seria saludar. O sea la funcion_b es el argumento y al mismo tiempo es la funcion saludar). De la siguiente manera:

def funcion_a(funcion_b):

    def funcion_c():
        funcion_b()

    return funcion_c

@funcion_a
def saludar():
    print("Hola, nos encontramos en una funcion.")

saludar()


En consola: Hola, nos encontramos en una funcion. 

--> Ya podemos ver el mensaje de la funcion saludar. Ahora nuestro decorador esta decorando de forma correcta a nuestra funcion. 


 Pero, como mencionamos anteriormente lo interesante de los decoradores es que nosotros podemos extender funcionalidades a funciones las cuales o no podamos modificarlas o simplemente no queramos hacerlo, para ello podemos ejecutar codigo ya sea antes o despues del llamado a la funcion.
 
 Por ejemplo, trabajando con la funcion_a vamos a realizar nuevas tareas antes y despues de llamar a la funcion_b, en este caso son tareas bastante sencillas donde unicamente vamos a imprimir en consola un pequeno mensaje, sin embargo nosotros pudiesemos realizar tareas sumamente complejas, tareas repetitivas como por ejemplo conectarse a una base de datos, enviar un correo electronico, leer de una archivo de excel, etc. Cualquier tipo de tarea que nosotros necesitemos ejecutar ya sea antes o despues del llamado a la funcion. 

Demostracion: 

def funcion_a(funcion_b):

    def funcion_c():
        print(">>> Antes del llamado.")

        funcion_b()

        print(">>> Despues del llamado.")

    return funcion_c

@funcion_a
def saludar():
    print("Hola, nos encontramos en una funcion.")

saludar()

En consola: 
>>> Antes del llamado.
Hola, nos encontramos en una funcion
>>> Despues del llamado.

--> Confirmamos que en efecto podemos realizar tareas ya sea antes o despues del llamado. 

 Con esto podemos entender mejor que estamos extendiendo funcionalidades, ya que en ningun momento estamos modificando a nuestra funcion saludar sin embargo con el decorador podemos ejecutar codigo ya sea antes o despues de su llamado. Entoces ya sabemos que ...

def funcion_a(funcion_b):

    def funcion_c():
        print(">>> Antes del llamado.")

        funcion_b()

        print(">>> Despues del llamado.")

    return funcion_c

... a esto lo conoceremos como un decorador y esta es la estructura base de cualquier decorador. Una funcion que recibe como argumento una funcion y a su vez retorna otra funcion, esta nueva funcion no sera mas que la funcion decorada donde colocamos el codigo que queremos ejecutar.

 OJO: EN LA FUNCION DECORADA COLOCAMOS EL CODIGO QUE QUEREMOS EJECUTAR. 

 Tambien saber que un decorador puede ser utilizado una "n" cantidad de veces dentro de una "n" cantidad de funciones. 



 Otro ejemplo, trabajando con la misma funcion saludar pero agregando una funcion nueva llamada suma que va a realizar una pequena operacion, y si yo quiero decorar a esta funcion lo que hago es volver a colocar en la parte superior el @ seguido de la funcion a decorar: 

def funcion_a(funcion_b):

    def funcion_c():
        print(">>> Antes del llamado.")

        funcion_b()

        print(">>> Despues del llamado.")

    return funcion_c

@funcion_a
def saludar():
    print("Hola, nos encontramos en una funcion.")


@funcion_a
def suma():
    print(10 + 30)
    
suma()

En consola:
>>> Antes del llamado.
40
>>> Despues del llamado.

--> Estamos nuevamente reutilizando mi decorador.



 Los decoradores pueden ser aun mas complejos, hay decoradores para decoradores, decoradores para metodos, decoradores para clases, etc. Sin embargo la estructura base de un decorador es unicamente trabajar con por lo menos con tres funciones , la funcion_a que recibe como argumento a la Funcion_b y da como resultado la funcion_c.  


----------------------------------------------------------------------------------------------------------------

#17) CLASE 17 - DECORADORES PT2.

def funcion_a(funcion_b):

    def funcion_c():
        print(">>> Antes del llamado.")

        funcion_b()

        print(">>> Despues del llamado.")

    return funcion_c


@funcion_a
def suma():
    print(10 + 30)
    
suma()


 Que pasa si la funcion a decorar recibe argumentos y parametros y retorna algun tipo de valor???

R: En esos casos debemos adaptar nuestro decorador para que pueda trabajar con argumentos, parametros y retornar valores. Para ellos vamos hacer lo siguiente, nos apoyaremos de los parametros con * y **. 

 Por ejemplo, creemos una funcion que nos permita sumar dos numeros enteros y esta funcion va a retornar la suma de esos numeros.  

def suma(numero_1, numero_2):
    return numero_1 + numero_2

suma()

-> Ahora queremos decorar esta funcion. 

Ejemplo completo con el decorador y colocando los argumentos que son necesarios en la funcion suma:

def funcion_a(funcion_b):

    def funcion_c():
        print(">>> Antes del llamado.")

        funcion_b()

        print(">>> Despues del llamado.")

    return funcion_c


@funcion_a
def suma(numero_1, numero_2):
    return numero_1 + numero_2
    
suma(10, 20)


En consola: 
Traceback (most recent call last):
  File "C:\Users\Usuario\Desktop\python\python.programas\modulo_7\decoradores.py", line 202, in <module>
    suma(10, 20)
TypeError: funcion_a.<locals>.funcion_c() takes 0 positional arguments but 2 were given


--> Nos indica un error, que la funcion_c toma cero argumentos a pesar de que nosotros estamos pasando 2. 

 Para solucionar este problema vamos a hacer lo siguiente:

 Como ya sabemos cuando decoramos a una funcion, estaremos ejecutando no la funcion perse sino la funcion_c, asi que dentro de esta funcion_c vamos a colocar los parametros con asteriscos y doble asterisco. Ejemplo:


def funcion_a(funcion_b):

    def funcion_c(*args, **kwargs):
        print(">>> Antes del llamado.")

        funcion_b()

        print(">>> Despues del llamado.")

    return funcion_c


@funcion_a
def suma(numero_1, numero_2):
    return numero_1 + numero_2
    
suma(10, 20)

En consola: 
Traceback (most recent call last):
  File "C:\Users\Usuario\Desktop\python\python.programas\modulo_7\decoradores.py", line 202, in <module>
    suma(10, 20)
TypeError: funcion_a.<locals>.funcion_c() takes 0 positional arguments but 2 were given

C:\Users\Usuario\Desktop\python\python.programas\modulo_7>python decoradores.py
>>> Antes del llamado.
Traceback (most recent call last):
  File "C:\Users\Usuario\Desktop\python\python.programas\modulo_7\decoradores.py", line 202, in <module>
    suma(10, 20)
  File "C:\Users\Usuario\Desktop\python\python.programas\modulo_7\decoradores.py", line 192, in funcion_c
    funcion_b()
TypeError: suma() missing 2 required positional arguments: 'numero_1' and 'numero_2'

--> Nos da el mismo error, ya que a pesar de que la funcion_c si puede obtener-capturar los argumentos y los parametros al momento de llamar a suma no estamos pasando ningun tipo de valor. Asi que para ello debemos colocar los argumentos y los parametros tal cual. (En la funcion_b). 


def funcion_a(funcion_b):

    def funcion_c(*args, **kwargs):
        print(">>> Antes del llamado.")

        funcion_b(*args, **kwargs)

        print(">>> Despues del llamado.")

    return funcion_c


@funcion_a
def suma(numero_1, numero_2):
    return numero_1 + numero_2
    
suma(10, 20)

En consola:
>>> Antes del llamado.
>>> Despues del llamado.


--> Ya no me da ningun tipo de error. 

 Ahora vamos a imprimir en consola el resultado, despues de obviamente almacenarlo en una variable. 

def funcion_a(funcion_b):

    def funcion_c(*args, **kwargs):
        print(">>> Antes del llamado.")

        funcion_b(*args, **kwargs)

        print(">>> Despues del llamado.")

    return funcion_c


@funcion_a
def suma(numero_1, numero_2):
    return numero_1 + numero_2
    
resultado = suma(10, 20)
print(resultado)

En consola: 
>>> Antes del llamado.
>>> Despues del llamado.
None

--> Visualizamos None, esto se debe a que si recordamos cuando nosotros decoramos una funcion y llamamos a esa funcion no estaremos ejecutando la funcion perse sino estaremos ejecutando la funcion_c entonces debemos hacer que la funcion_c retorne el valor. Entonces si deseamos vizualizar el resultado de la suma, entonces debemos almacenar en una variable la funcion_c y vamos a retornar en la funcion_c dicha variable. 

 De esta forma para el usuario final al momento de utilizar la funcion se le sera completamente indiferente si la funcion se encuentra decorada o no, simplemente hace el llamado, pasa los argumentos y los parametros, espera un resultado y listo.
 Internamente la funcion ejecuta tareas antes y despues (los print que pusimos), obtiene un resultado (la variable resultado) no sin antes pasar los argumentos y los parametros y para finalizar la funcion_c retorna dicho resultado.   
 La funcion_c es la funcion la cual posee mas acciones a realizar, ya que esta es la funcion decorada, la funcion que extiende funcionalidades por lo tanto necesita mas tareas que realizar. 

def funcion_a(funcion_b):

    def funcion_c(*args, **kwargs):
        print(">>> Antes del llamado.")

        resultado = funcion_b(*args, **kwargs)

        print(">>> Despues del llamado.")

        return resultado

    return funcion_c


@funcion_a
def suma(numero_1, numero_2):
    return numero_1 + numero_2
    
resultado = suma(10, 20)
print(resultado)

En consola: 
>>> Antes del llamado.
>>> Despues del llamado.
30

--> Ahora si visualizamos el resultado de la suma. 


Para el usuario final debe ser transparente el uso de la funcion suma, realmente a el no le interesa si la funcion se encuentra decorada o no. El decorador debe ser lo suficientemente flexible para que pueda recibir una "n" cantidad de argumentos y una "n" cantidad de parametros y en caso la funcion retorne algun tipo de valor, bueno la funcion decorada pueda retornar dicho valor. 


Finalmente, esta seria la estructura base que nosotros vamos a utilizar para cualquier decorador que nosotros creemos:

def funcion_a(funcion_b):

    def funcion_c():
        pass

    return funcion_c

Tenemos: La funcion_a que recibe la funcion_b y retorna la funcion_c. La funcion_c es la funcion decorada por lo tanto esta funcion debe realizar muchas mas tareas, ya sean tareas antes o despues de que la funcion a decorar sea llamada y en dado caso la funcion a decorar reciba argumento o parametros haremos uso de * y **.   

Recordemos, cuando nosotros llamamos a una funcion decorada no estaremos ejecutando directamente la funcion perse sino que estaremos ejecutando la funcion_c, la funcion_c se encargara de realizar las tareas antes o despues del llamado a la funcion principal - la funcion a decorar, y la funcion a decorar posteriormente va a realizar las tareas que le correspondan.  


----------------------------------------------------------------------------------------------------------------

#18) CLASE 18 - GENERADORES.

 Un generador no es mas que un tipo especial de funcion la cual retorna objetos que facilmente podemos iterar, esto sin que la funcion finalice.
 
 Ejemplo: Vamos a crear un generador el cual nos permita iterar sobre todo los numeros pares que comprendan del 0 al 100. 

- Primero definimos la funcion que tendra por nombre pares, y por dentro de la funcion vamos a iterar utilizando la funcion range y posteriormente vamos a imprimir. Y para finalizar llamamos a la funcion.

def pares():
    for numero in range(0, 10, 2): 
        print(numero)

pares()


*(0, 10, 22) -> En este caso como queremos todos los numeros pares del 0 al 100, ponemos el 0, el 100 y el 2 por los saltos de 2 en 2. 

En consola: Visualizamos todos los numero pares del 0 al 100.


 Sin embargo la funcion pares se encuentra lejos de poderse considerar un generador, ya que como mencionamos un generador no es mas que un tipo especial de funcion la cual RETORNA objetos sin que esta finalice. 

 Entonces si recordamos, para que nosotros podamos retornar valores debemos hacer uso de la palabra reservada return. Por ejemplo, hagamos uso de return en la funcion pares y luego imprimamos en consola lo que la funcion pares me retorne:

def pares():
    for numero in range(0, 10, 2): 
        return numero

print(pares())

En consola: 
0 

--> Visualizamos 0, que seria el primer numero generado por la funcion range. Si bien es cierto la palabra reservada return nos permite retornar valores para nuestras funciones tambien es importante mencionar que al nosotros ejecutar return estaremos finalizando de forma inmediata la ejecucion de la funcion, es por ello que en este caso visualizamos 0, ya que en la primera iteracion retornamos el valor y finalizamos la funcion, por lo tanto las iteraciones que continuan no pueden comenzar porque la funcion a finalizado en la primera iteracion.    
 Por lo tanto, para que nosotros podamos crear nuestros propios generadores la palabra reservada return no nos es de utilidad. Lo que podemos hacer es utilizar la palabra reservada yield. 
 A diferenca de return donde retornamos un objeto y finalizamos la funcion, con el uso de la palabra reservada yield suspenderemos de forma momentanea la ejecucion de la funcion, esto para retornar un objeto, una vez el objeto haya sido retornado la funcion podra reanudarse en el punto donde se detuvo.  


def pares():
    for numero in range(0, 10, 2): 
        yield numero

print(pares())

En consola:
<generator object pares at 0x0000020ABFD8D0E0>

--> Ahora visualizamos un objeto de tipo generador.  

 Una vez que nosotros hayamos comenzado el generador, facilmente podemos ir obteniendo cada uno de sus valores conforme a demanda, conforme a nosotros lo vayamos necesitando.
 Veamos, en el ejemplo anterior, debajo de la funcion pares vamos a ir iterando: for par in (llamamos a la funcion pares) pares y en cada iteracion simplemente vamos a imprimir par. Ejm:

def pares():
    for numero in range(0, 10, 2): 
        yield numero

for par in pares():
    print(par)
      

En consola: Visualizamos en consola todos los numeros pares del 0 al 100, solo que en esta ocasion nos apoyamos de un generador. 

 Entonces, la palabra reservada yield nos permite retornar valores sin que la funcion finalice, unicamente pausando su ejecucion para que posteriormente pueda reanudarse desde el punto donde se quedo.   

 En este ejemplo la funcion pares ya se convierte en un generador.  

 Lo interesante de todo esto es que al nosotros poder retornar valores y pausar la ejecucion de nuestra funcion 
estaremos trabajando con un: Lazy iterator. Es decir, trabajaremos con una iteracion perezosa. Pudiendo asi obtener cada uno de los objetos que el generador genera y retorna bajo de demanda, siempre que lo necesitemos. 

 En este caso (en el ejemplo), la funcion retorna y pausa su ejecucion. Podemos confirmar esto si nosotros imprimimos en consola un mensaje. Veamos: 

def pares():
    for numero in range(0, 10, 2): 
        yield numero

        print("Se reanuda la ejecucion")

for par in pares():
    print(par)  


En consola:
0
Se reanuda la ejecucion.
2
Se reanuda la ejecucion.
4
...


--> Visualizamos en consola, primero la impresion del numero y despues la impresion de nuestro mensaje. Numero-mensaje, numero-mensaje, ...
 Esto se debe ya que al retornarse el valor de numero este se almacena en la variable par, y en este caso despues de retornarse, la funcion suspende su ejecucion. Entonces, el valor de numero se almacena en par y posteriormente se ejecuta este bloque: print(par), donde simplemente se imprime la variable. En la siguiente iteracion la funcion par reanuda su ejecucion en el punto donde se detuvo (en yield) ejecutando todas aquellas lineas de codigo que se encuentren despues de yield. Es por ello que visualizamos la impresion del numero y despues la impresion del mensaje.  

def pares(): # Generador -> Lazy iterator
    for numero in range(0, 10, 2): 
        yield numero # La funcion suspende su ejecucion

        print("Se reanuda la ejecucion")

for par in pares():
    print(par)  

  
----------------------------------------------------------------------------------------------------------------

#19) CLASE 19 - DISTRIBUCION PEREZOSA.

- Cual es la principal ventaja de que nosotros implementemos generadores???
- No es mas facil que nuestra funcion retorne ya sea una lista o una tupla???

--> La principal ventaja de que nosotros utilicemos generadores recae en la forma en la que nosotros vamos a iterar cada uno de los objetos que el generador genera y retorna, ya que como mencionamos anteriormente, al nosotros implementar la palabra reservada yield seremos capaces de suspender la ejecucion de la funcion de forma momentanea, esto a su vez nos permite trabajar con un lazy iterator, pudiendo asi obtener cada uno de los objetos que el generador retorna bajo demanda. 
 La principal ventaja de todo esto recae en el uso de memoria, ya que al nosotros solo obtener los valores que necesitemos cuando los necesitemos no estaremos reservando espacio en memoria que muy probablemente no usaremos y esto nos viene perfecto al trabajar con colecciones de miles, cientos de miles o inclusive millones de registros. Pudiendo asi tener programas con un mucho mayor performance (mucho mas rapidos), reservando espacio en memoria que si usaremos.     

En este caso: 

def pares(): #Generador -> Lazy iterator
    for numero in range(0, 10, 2): 
        yield numero #La funcion suspende su ejecucion

        print("Se reanuda la ejecucion")

for par in pares():
    print(par)  
 

...Nosotros comenzamos nuestro generador y en cada iteracion lo volvemos a llamar, pudiendo asi pausar y reanudar su ejecucion --> Esto lo hacemos con for par in pares():
    print(par)  


 Sin embargo para que nos quede mas claro este concepto de los lazy iterator, vamos a ir obteniendo cada uno de los objetos que el generador genere y retorne bajo demanda, conforme nosotros lo vayamos necesitando. Para ello nos apoyaremos de la funcion next. 

- Primero y debajo obviamente de la funcion pares, voy a almacenar el generador en una variable:

generador = pares()

- Posteriormente vamos a obtener el siguiente elemento que el generador nos retorne, y para ello vamos a hacer uso de la funcion next y pasamos como argumento el generador perse, que seria mi variable generador:

print(next(generador))


Ejemplo completo: 

def pares(): 
    for numero in range(0, 10, 2): 
        yield numero

        print("Se reanuda la ejecucion")

generador = pares()

print(next(generador))


En consola:
0 

--> Visualizamos que el primer elemento que el generador genera y retorna es 0, sin embargo nosotros podemos llamar a la funcion next la "n" cantidad de veces que deseemos. Si por ejemplo llamo a la funcion 6 veces, voy a obtener los primeros 6 elementos de el generador. Ejm:

print(next(generador))
print(next(generador))
print(next(generador))
print(next(generador))
print(next(generador))
print(next(generador))

En consola: Los genera perfecto. 


 De esta forma entonces es como nosotros vamos a obtener los elementos conforme a demanda, siempre que nosotros los necesitemos. En este caso al nosotros llamar a nuestro generador el generador retorna y pausa su ejecucion, no es hasta que nuevamente el generador es llamado cuando se reanuda su ejecucion. De esta manera se comprende mejor como funciona una lazy iterator, nosotros vamos a consumir el generador siempre que lo necesitemos.

 La principal ventaja de todo esto recae en el uso de memoria, los generadores son recomendados ampliamente cuando vayamos a trabajar con colecciones de miles, cientos de miles o inclusive millones de registros donde estos registros probablemente no los necesitemos todos de una sola vez sino que los vayamos consumiendo conforme nosotros vayamos avanzando, conforme nosotros los vayamos requiriendo. 

 En el ejemplo, podemos ver que cada linea de codigo nos permite obtener un nuevo objeto del generador y por supuesto nosotros pudiesemos ejecutar diferentes sentencias entre una ejecucion y otra, ejm: 


print(next(generador))

print(next(generador))

print(next(generador))

print(next(generador))

print(next(generador))

print("Ejecutamos codigo entre un llamado y otro.")

print(next(generador))

En consola:
0
Se reanuda la ejecucion
2
Se reanuda la ejecucion
4
Se reanuda la ejecucion
6
Se reanuda la ejecucion
8
Ejecutamos codigo entre un llamado y otro.
Se reanuda la ejecucion
10
 
--> Perfecto. 


 
 Importa saber que si nosotros intentamos obtener el siguiente elemento del generador cuando este ya haya finalizado, utilizando la funcion next es muy probable que obtengamos un error, el error stop iteration. Ejm, vamos a pedir la lista de numero pares del 1 al 10, pero la vamos a pedir 6 veces, y del 1 al 10 solo hay 5 veces numeros pares:


def pares(): 
    for numero in range(0, 10, 2): 
        yield numero

        print("Se reanuda la ejecucion")

generador = pares()

print(next(generador))
 
print(next(generador))

print(next(generador))

print(next(generador))

print(next(generador))

print("Ejecutamos codigo entre un llamado y otro.")

print(next(generador))

En consola:
0
Se reanuda la ejecucion
2
Se reanuda la ejecucion
4
Se reanuda la ejecucion
6
Se reanuda la ejecucion
8
Ejecutamos codigo entre un llamado y otro.
Se reanuda la ejecucion
Traceback (most recent call last):
  File "C:\Users\Usuario\Desktop\python\python.programas\modulo_7\generadores.py", line 138, in <module>
    print(next(generador))
          ^^^^^^^^^^^^^^^
StopIteration

--> Como el generador ya finalizo y como no podemos obtener un siguiente elemento de el, se lanza el error StopIteration. 

 Este error facilmente podemos validarlo utilizando try y except, es decir vamos a trabajar con los errores de la siguiente manera: 


def pares(): 
    for numero in range(0, 10, 2): 
        yield numero

        print("Se reanuda la ejecucion")

generador = pares()

while True:
    try:
        par = next(generador)
        print(par)
    except StopIteration:
        print("El generador finalizo.")
        break

--> Lo que hacemos aca es:

- Comenzamos el generador -> generador = pares()

- Mediante un ciclo while infinito -> while True. 

Comenzamos a obtener cada uno de los siguientes valores del generador e imprimimos en consola: 
        par = next(generador)
        print(par)

Y cuando el generador simplemente se quede sin valores a retornar, mostramos un pequeno mensaje:
    except StopIteration:
        print("El generador finalizo.")

Y finalizamos con el ciclo while:
        break


 Cada bloque de try, obligatoriamente necesita su bloque except. Con try y except lo que hacemos es que vamos a intentar algo y en dado caso algun tipo de error ocurra, seremos capaces de ejecutar un bloque para que maneje la excepcion. En el ejemplo anterior vamos a trabajar con el error StopIteration, el cual es el error que estamos trabajando especificamente. 


En consola: 
0
Se reanuda la ejecucion
2
Se reanuda la ejecucion
4
Se reanuda la ejecucion
6
Se reanuda la ejecucion
8
Se reanuda la ejecucion
El generador finalizo.

--> Funciona. 


En conclucion, un generador no es mas que un tipo especial de funcion que nos permite retornar valores que facilmente podemos iterar para ello utilizamos la palabra reservada yield, esta palabra reservada nos permite retornar un valor y suspender de forma momentanea la ejecucion de la funcion, no es hasta que el generador es nuevamente llamado cuando la funcion se reanuda desde el punto donde se quedo. Si nosotros intentamos obtener valores cuando el generador ya finalizo, vamos a obtener como error un StopIteration, error que facilmente podemos manejar si trabajamos con un try y un except.  


----------------------------------------------------------------------------------------------------------------

#20) CLASE 20 - DOCUMENTAR FUNCIONES. 

 Una muy buena practica de programacion al momento de crear funciones es que siempre que podamos las documentemos. Y para ello, tulizando Python nos apoyaremos del Docstring.

 Veamos un ejemplo: 

- Vamos a crear una funcion bastante sencilla, que me va a permitir sumar dos numero enteros y poseera dos parametros y vamos a retornar la suma de los numeros. 

def suma(numero_1, numero_2):
    return numero_1 + numero_2
 
--> Ahora, por buenas practicas de programacion siempre que creemos una funcion lo aconsejable es que las documentemos. En Python para documenta una funcion lo haremos utilizando un Docstring. 

-> En Docstring no es mas que un comentario que se coloca en la primera linea de codigo de nuestra funcion. Por convencion vamos a utilizar para este comentario triple comillas dobles para abrir y cerrar """ """. 

 En la primera linea de este comentario vamos a colocar una descripcion de lo que realiza la funcion, por ejemplo: La funcion suma 2 numero enteros.

 posteriormente podemos describir mas en detalle los valores de entrada y los valores de salida con los cuales trabaja la funcion, ejm: Argumentos:
    numero_1 (int)
    numero_2 (int)

    Se retorna la suma de los parametros.


Ejm completo:

def suma(numero_1, numero_2):
    """
    La funcion suma 2 numero enteros.

    Argumentos:
    numero_1 (int)
    numero_2 (int)

    Se retorna la suma de los parametros.
    """

    return numero_1 + numero_2


--> Esta seria la documentacion de mi funcion. Ya que la funcion es bastante sencilla, la documentacion de igual forma lo es. 
 

Entonces, esto:
 
    """
    La funcion suma 2 numero enteros.

    Argumentos:
    numero_1 (int)
    numero_2 (int)

    Se retorna la suma de los parametros.
    """

...Es el Docstring, un comentario que se coloca en la primera linea de codigo de nuestra funcion. Dentro del comentario en la primera linea, vamos a colocar una breve descripcion de lo que realiza la funcion.Posteriormente podemos detallar cada una de las partes de la funcion, por ejemplo sus argumentos, el o los valores que retorna, etc.

 En el Docstring incluso podemos poner un to do list. De la siguiente manera:

    """
    La funcion suma 2 numero enteros.

    Argumentos:
    numero_1 (int)
    numero_2 (int)

    Se retorna la suma de los parametros.

    TODO:
        *
    """  

 En este caso, por lo sencillo de la funcion el TODO quedara vacio. 


 Lo interesante de todo esto es que el Docstring quedara almacenado en el atributo __doc__. En Python existen documentables, este tipo de objetos poseen el atributo __doc__ y mediante este atributo nosotros seremos capaces de comentar su respectiva documentacion. Los objetos documentables son: Modulos, Clases, Metodos y Funciones. 

 En este caso (en el ejemplo) el Docstring sera almacenado en el atributo __doc__ de nuestra funcion. Podemos confirmar esto impriendo en consola dicho atributo, de la siguiente manera: print(suma.__doc__) -> Usamos el nombre de la funcion seguido del un punto y __doc__

Ejemplo completo:

def suma(numero_1, numero_2):
    """
    La funcion suma 2 numero enteros.

    Argumentos:
    numero_1 (int)
    numero_2 (int)

    Se retorna la suma de los parametros.

    TODO:
        *
    """

    return numero_1 + numero_2


print(suma.__doc__)

En consola:
    La funcion suma 2 numeros enteros.

    Argumentos:
    numero_1 (int)
    numero_2 (int)

    Se retorna la suma de los parametros.

    TODO:
        *


--> Perfecto, imprimimos en consola lo que el atributo doc almacena. 


 Tambien podemos tener el mismo resultado en consola utilizando la funcion help. Ejm:

print(help(suma)) 

--> Se lee: vamos a imprimir lo que la funcion help, pasando como argumento nuestra funcion retorne. 


def suma(numero_1, numero_2):
    """
    La funcion suma 2 numero enteros.

    Argumentos:
    numero_1 (int)
    numero_2 (int)

    Se retorna la suma de los parametros.

    TODO:
        *
    """

    return numero_1 + numero_2


#print(suma.__doc__)
print(help(suma)) 

En consola: Efectivamente obtengo el mismo resultado que al usar el atributo __doc__.



----------------------------------------------------------------------------------------------------------------

#21) CLASE 21 - TESTEAR FUNCIONES.


 Una caracteristica muy interesante de Python es que nosotros podemos testear nuestras funciones utilizando el Docstring, o sea nosotros podemos comprobar el comportamiento de una funcion unicamente con comentarios. Veamos como:

-> Estaremos trabajando nuevamente con la funcion anterior, la funcion suma. 

def suma(numero_1, numero_2):
    """
    La funcion suma 2 numero enteros.

    Argumentos:
    numero_1(int)
    numero_2(int)

    Se retorna la suma de los parametros.

    """
    return numero_1 + numero_2


--> Como podemos observar la funcion ya posee su Docstring. 

 Recordemos que el Docstring no es mas que un comentario el cual se coloca en la primera linea de codigo de nuestra funcion y por convencion este comentario se va a crear utilizando triple comillas dobles al abrir y cerrar.

 Volviendo a nuestra funcion, podemos observar que ya se encuentra comentada y en el comentario tenemos descrito el funcionamiento de la funcion. Lo que voy hacer es colocar la pruebas para comprobar que la funcion, funciona correctamente. Para ello vamos a "simular" que nos encontramos dentro de la consola, esta simulacion la hacemos utilizando triple mayor que >>>, y hacemos el llamado a la funcion. En este caso colocamos: suma() y dentro de los parentesis los correspondientes argumentos. Ejm:

def suma(numero_1, numero_2):
    """
    La funcion suma 2 numero enteros.

    Argumentos:
    numero_1(int)
    numero_2(int)

    Se retorna la suma de los parametros.

    >>> suma(10, 20)

    """
    return numero_1 + numero_2


 Debajo del llamado a la funcion debo colocar el valor que daria la ejecucion de la funcion. O sea, si yo hago el llamado de la funcion suma pasando como argumentos 10 y 20, el resultado de la suma de 10 y 20 es 30. Entonces debajo de el llamado, en una nueva linea debo escribir este valor, debo escribir 30. Ejm:

def suma(numero_1, numero_2):
    """
    La funcion suma 2 numero enteros.

    Argumentos:
    numero_1(int)
    numero_2(int)

    Se retorna la suma de los parametros.

    >>> suma(10, 20)
    30

    """
    return numero_1 + numero_2


--> Ya esta seria nuestra primera prueba, "simulando" que estamos llamando a nuestra funcion en consola. Utilizando >>> y posteriormente hacemos el llamado a nuestra funcion, despues de este llamado en una nueva linea vamos a colocar el deber ser o sea lo que la funcion deberia retornar. 

 Nosotros podemos tener la "n" cantidad de pruebas que deseemos, podemos poner debajo de esta prueba otra con valores distintos, sumando por ejemplo 100 y 200. Pero el profesor nos aconseja que intentemos limitar la cantidad de pruebas a utilizar, un maximo de tres. Esto por temas de legibilidad. 

 Anadamos en nuestro ejemplo otra prueba:

def suma(numero_1, numero_2):
    """
    La funcion suma 2 numero enteros.

    Argumentos:
    numero_1(int)
    numero_2(int)

    Se retorna la suma de los parametros.

    >>> suma(10, 20)
    30

    >>> suma(100, 200)
    300

    """
    return numero_1 + numero_2


 Ahora, para que nosotros podamos probar nuestra funcion utilizando estas pruebas debemos ubicarno en nuestra terminal y ejecutar el siguiente comando: python + -m doctest (modulo doctest) + nombre del archivo. Asi:
 
python -m doctest nombre_del_archivo_a_probar 


 Al nosotros utilizar el modulo doctest lo que se hara sera probar todos los OBJETOS DOCUMENTABLES a traves de su docstring. 

 Recordemos que los objetos documentables son 4. Los Modulos, las Clases, los Metodos y las Funciones. Entonces todos los objetos que se encuentres dentro del archivo y sean objetos documentables el modulo doctest procedera a probarlos, utilizando su docstring. 

 
Aplicandolo en el ejemplo, seria:

python -m doctest documentar.py

--> Al ejecutar el comando y no obtener ningun error quiere decir que todas las pruebas que se encuentran dentro del archivo han sido probadas y han sido exitosas. 


 Pero, si por ejemplo colocamos dentro del docstring una prueba erronea, si en vez de poner que la suma de 10 y 20 da 50, me va a dar un error en consola al momento de ejecutar el comando. El error me va a indicar que la prueba ha fallado, indicandome el error de lo que yo esperaba y el valor que realmente se obtuvo.  


 Con esto confirmamos que todos los objetos documentables dentro del archivo se van a probar utilizando el modulo doctest y para ello haremos uso de los docstrgings. Dentro de los docstrings vamos a simular el llamado a la funcion en consola.



----------- MODULO_8->CLASES----------------------

--------------------------------------------------

COMPLEMENTO INICIAL:

¿¿¿QUE ES UNA CLASE???

CONCEPTO #1-> Una clase no es mas que un conjunto de variables y metodos que cuando los agrupamos podemos utilizarlos para definir en nuestro codigo cualquier concepto que queramos.

 Un objeto no es mas que una instancia especifica de esta clase. 

 Cuando quiero definir un objeto utilizando una clase, tomo una variable le doy el nombre que quiera y digo que es igual a mi clase, y mi clase la llamo como si fuese una funcion. Como hemos dicho, una clase es un conjunto de variable y metodos, por lo tanto si queremos acceder a algunas de estas variables o propiedades de un objeto especifico que hayamos creado o alguno de esos metodos lo hacemos utilizando un punto (.).

CONCEPTO #2-> Las clases proveen una forma de empaquetar datos y funcionalidad juntos. Al crear una nueva clase, se crea un nuevo tipo de objeto, permitiendo crear nuevas instancias de ese tipo. Cada instancia de clase puede tener atributos adjuntos para mantener su estado. Las instancias de clase también pueden tener métodos (definidos por su clase) para modificar su estado.

 Un método es un bloque de código que contiene una serie de instrucciones.

-----------------------------------------------------

#1) CLASE 1 - CLASES.


 En Python para que nosotros podamos crear nuestras propias clases, lo haremos utilizando la palabra reservada class. 
 Ejemplo, vamos a crear una clase la cual nos permita representar a un usuario. Pasos:

- Colocamos la palabra reservada class.

- Seguido colocamos el nombre de la clase. Nombre que por convencion vamos a utilizar la nomenclatura CamelCase, esta nomenclatura nos indica que la primera letra de cada palabra va a encontrarse en mayuscula y si el nombre de la clase se compone de dos o mas palabras vamos a unir esas palabras, sin  ningun tipo de caracter intermedio. Ejm: CamelCase.
Tambien por convencion el nombre de la clase va a encontrarse en singular. Seguido vienen los dos puntos y la indentacion para un nuevo bloque. En el ejemplo la clase tendra por nombre usuario, por lo tanto la primera letra sera en mayuscula: Usuario. 

- Posteriormente creamos un nuevo bloque, dentro del bloque nosotros vamos a colocar todos aquellos atributos y metodos que deseemos la clase posea. 
En este caso, para el ejemplo no pretendo que la clase posea ningun tipo de atributo ni ningun tipo de metodo, asi que voy a dejar el bloque completamente vacio. Pero en Python no podemos simplemente dejar el bloque vacio porque nos daria un error, entonces para evitar bloques vacios lo que podemos hacer es utilizar la palabra reservada pass. 
Con esto le indicamos a Python que por el momento el bloque no realizara ningun tipo de accion, quiza mas adelante pero por ahora no. 

El ejemplo:

class Usuario:
    pass

--> De esta forma tan sencilla es como nosotros podemos crear clases en Python.


 Una vez nosotros hayamos definido una clase, ya seremos capaces de instanciar la "n" cantidad objetos que deseemos. Por ejemplo, creemos un usuario que sea cody.
 
[¿¿¿QUE ES INSTANCIAR UN OBJETO???
R: Se llama instancia a todo objeto que derive de algun otro. Instancia significa crear un objeto a partir de una clase.]

...Ejm: Creemos un usuario que sea cody.

- Colocamos Cody que es nuestra variable, signo igual seguido de nuestra clase, parentesis y dentro de los parentesis vamos a colocar los argumentos necesarios para poder inicializar los atributos del objeto. En este caso el objeto no posee ningun tipo de atributo, asi que no vamos a colocar argumentos. 

- Procedemos a imprimir en consola el objeto cody.


class Uruario:
    pass

cody = Usuario()  
print(cody)


En consola:
<__main__.Usuario object at 0x000002094043E0D0>

--> Se me indica que el objeto es de tipo usuario. Lo cual nos indica que hemos definido de forma correcta nuestra clase y hemos creado de forma correcta nuestro objeto. 


Entonces, de esta forma tan sencilla seremos capaces de definir clases las cuales a su vez nos permitan crear una "n" cantidad de objetos. 

¿¿¿QUE ES UN OBJETO EN PYHTON???
R: Un objeto en Python es una colección única de datos (atributos) y comportamiento (métodos).
 Un objeto es una instancia de una clase.


----------------------------------------------------
#2) CLASE 2 - ATRIBUTOS DE CLASE.

 Algo muy interesante de Python en el apartado de atributos, es que nosotros podremos dividir los atributos en dos tipos, estos son los atributos de clase y los atributos de instancia. 

- Atributos de clase: Son atributos los cuales le pertenecen a una clase y para que nosotros podamos utilizarlos, obligatoriamente tendremos que utilizar dicha clase. 

- Atributos de instancia: Son atributos los cuales le pertenecen a un objeto y para que nosotros podamos utilizarlos, obligatoriamente trabajaremos con el objeto. 


 ATRIBUTOS DE CLASE: Para crear este tipo de atributos unicamente basta con simplemente crear variables dentro de la clase.
 
 Ejm, vamos a utilizar la clase usuario y vamos a crear dos nuevos atributos. Uno llamado username y email, ambos no son mas que strings vacios. 

class Usuario:
    username = ""
    email = ""

--> De esta forma es como podemos crear atributos de clase, basta con definir variables dentro de la clase. Estos atributos le pertenecen a la clase, y para que nosotros podamos utilizarlos obligatoriamente haremos uso de la clase. 

Por ejemplo imprimamos en consola el atributo username. Si deseamos imprimir en consola los atributos de una clase, debemos colocar el nombre de la clase + . + el nombre del atributo con el cual queremos trabajar. Ejm: print(Usuario.username)

Ejm completo, vamos a imprimir en consola el atributo username. 

class Usuario:
    username = ""
    email = ""

print(Usuario.username)

En consola:

--> No visualizamos nada, ya que es un string vacio. Si lo lleno voy a visualizar su contenido. Ejm:


class Usuario:
    username = "Username por default"
    email = ""

print(Usuario.username)

En consola:
Username por default


Entonces de esta forma es como nosotros visualizamos los atributos de clase, ya sea para lectura como en el caso del ejemplo (Queriamos leer el contenido del atributo) o para escritura, ya que si quisieramos modificar el valor del atibuto tambien podemos hacerlo de esta forma.

Ejm: Vamos a modificar el atributo username. Lo que debemos hacer es colocar (fuera del bloque de codigo) la clase + . + username y asignamos un nuevo valor.

class Usuario:
    username = "Username por default"
    email = ""

Usuario.username = "User1"
Usuario.email = "info@codigofacilito.com"

print(Usuario.username)
print(Usuario.email)

En consola:
User1
info@codigofacilito.com

--> Visualizamos los atributos de clase con sus nuevos valores.



----------------------------------------------------
#3) CLASE 3 - ATRIBUTOS DE INSTANCIA.


 Para este video estaremos trabajando nuevamente con la clase usuario, la cual posee dos atributos DE CLASE ya definidos en la clase anterior. 

class Usuario:
    username = "Username por default"
    email = " "


 Entonces, lo primero que haremos sera crear un objeto de tipo usuario, este objeto tendra por nombre user1.
 Y posteriormente intentare acceder al atributo username mediante el objeto. 

user1 = Usuario() --> El objeto tipo usuario.
print(user1.username) --> Acceso al atributo username mediante el objeto.


Ejemplo completo:

class Usuario:
    username = "Username por default"
    email = " "

user1 = Usuario()
print(user1.username) 

En consola:
Username por default

--> Perfecto, logre acceder al atributo username mediante el objeto


 PERO, habiamos comentado que username es un atributo de clase y que los atributos de clase unicamente pueden ser utilizados por las clases??? 
Como puede ser que con el objeto user1 puedo acceder al atributo de clase username???

 Respuesta, esto es parcialmente verdadero. Ya que aca ocurre algo muy interesante. 

 En Python nosotros podemos anadir de forma dinamica atributos a nuestro objeto, esto en tiempo de ejecucion. 
 Y para nosotros poder lograr esto, internamente Python trabaja con un meta atributo, meta atributo que tiene por nombre: __dict__.

 Dentro del meta atributo __dict__ vamos a encontrar todos aquellos atributos que posea nuestro objeto. Vamos a verificarlo, imprimamos en consola el objeto user1 seguido de (.) y el meta atributo (user1.__dict__)
 Y este atributo va a almacenar mediante un diccionario todos aquellos atributos que posea nuestro objeto. 

Ejemplo completo: 

class Usuario:
    username = "Username por default"
    email = " "

user1 = Usuario()
print(user1.username)


print(user1.__dict__)

En consola:
Username por default
{}

--> Visualizamos un diccionario completamente vacio, puesto que el objeto user1 por el momento no posee ningun tipo de atributo. 


 Esto es algo que debemos de tener muy encuenta a la hora de establecer el porque estamos utilizando un atributo de clase. 
 Ya que cuando nosostros utilizamos un atributo para nuestro objeto (en el ejemplo el atributo username para el objeto user1) Python realiza los siguientes pasos:

#1- Verifica si el atributo existe dentro del objeto.
-> Si el atributo que nosotros queremos utilizar efectivamente se encuentra dentro del objeto, entonces se utiliza dicho atributo. En el caso del ejemplo no se encuentra dentro del objeto, entonces pasa al paso 2.

#2- Verifica si el atributo existe dentro de la clase. 
-> Si el atributo existe dentro de la clase, se utiliza dicho atributo, un atributo de clase. Justo lo que esta pasando en el ejemplo. 

OJO: Esto unicamente va a funcionar para lectura. 

 Y en dado caso nosotros queramos acceder a un atributo que no exista dentro de nuestro objeto y que tampoco exista dentro de la clase, entonces Python pasa al paso numero 3. 

#3- Lanzar un error.


 Tambien podemos confirmar todo esto si accedemos al id de los objetos. Ejm: 

print(id(user1.username)) -> id mediante mi objeto
print(id(Usuario.username)) -> id mediante la clase


EJEMPLO COMPLETO: 

class Usuario:
    username = "Username por default"
    email = " "

user1 = Usuario()
print(user1.username)

print(id(user1.username)) 
print(id(Usuario.username))


print(user1.__dict__)

En consola:
Username por default
1843760684992
1843760684992
{}

--> Podemos confirmar que en efecto ambos atributos son lo mismo. 


 Entonces, recordemos que en Python nosotros podemos anadir de forma dinamica, en tiempo de ejecucion atributos para nuestros objetos. Estos atributos se van a almacenar en el meta atributo __dict__ y mediante este atributo nosotros seremos capaces de conocer todos aquellos atributos que posea nuestro objeto, esto mediante un diccionario.  


----------------------------------------------------
#4) CLASE 4 - ATRIBUTOS DINAMICOS.

 Repasando -> Como mencionamos anteriormente los atributos de instancia no son mas que atributos los cuales le pertenecen a un objeto, y para que nosotros podamos utilizar dichos atributos obligatoriamente lo haremos mediante el objeto. De igual forma recordemos que en Python nosotros podemos anadir de forma dinamica atributos a nuestros objetos, estos atributos se van a almacenar en el meta atributo __dict__ , y de igual forma recordemos que si nosotros intentamos acceder a un atributo que el objeto no posea entonces Python va a buscar este atributo dentro de la clase y si la clase posee dicho atributo entonces se utilizara el atributo de clase, si por el contrario el atributo que queremos utilizar no se encuentra ni dentro del objeto ni dentro de la clase entonces Python lanzara un error.  

 Aprendamos a anadir atributos a nuestros objetos, de forma dinamica. 

 
class Usuario:
    username = "Username por default"
    email = ""

user1 = Usuario()

print(user1.username)

print(id(user1.username))
print(id(Usuario.username))

print(user1.__dict__)


--> En el video anterior nosotros intentamos utilizar el atributo username de nuestro objeto (nuestro objeto user1) pero como este atributo no existe dentro del objeto, simplemente accedimos al atributo de clase (username = "Username por default"), donde unicamente se nos permite la lectura. OJO, nosotros NO PODREMOS modificar atributos de clase. Por ejemplo si nosotros hacemos los siguiente: debajo de user1 escribimos user1.username = "Cody"

user1 = Usuario()

user1.username = "Cody"

Estaremos anadiendo de forma dinamica un nuevo atributo a nuestro objeto. NO es que vamos a modificar el valor de username, vamos es a crear otro username. Estaremos anadiendo el atributo al objeto y por supuesto estaremos estableciendo un valor inicial. Veamos el ejemplo completo con su ejecucion.   

class Usuario:
    username = "Username por default"
    email = ""


user1 = Usuario()
print(user1.username)

user1.username = "Cody" -> Anadimos el atributo al objeto
print(user1.username)


print(id(user1.username))
print(id(Usuario.username))

print(user1.__dict__)

En consola:
Username por default
Cody
2139565861168
2139565875136
{'username': 'Cody'}


--> Al ejecutar visualizamos los dos atributos y que sus id son completamente diferentes. Ahora estamos trabajando con un atributo de instancia que es user1.username = "Cody" y un atributo de clase que es username = "Username por default". Y tambien podemos observar que dentro del diccionario se encuentra un item nuevo, una llave y un valor. 

 Ya que Python al observar que nosotros estamos asignando un valor a un atributo que no existe dentro del objeto, entonces Python procede a anadir de forma dinamica en tiempo de ejecucion dicho atributo al objeto. En el caso del ejemplo username pasa a ser un atributo de instancia, un atributo el cual le pertenece al objeto. 

 Entonces de esta forma tan sencilla es como nosotros podemos anadir nuevos atributos a nuestros objetos. Basta con colocar el objeto + . + el atributo que nosotros queremos anadir y luego su correspondiente valor. De esta forma estamos anadiendo un atributo a nuestro objeto. Cuando Python nota que estamos asignando un valor a un atributo que no existe, entonces se procede a anadir dicho atributo al objeto. Veamos un ejemplo, vamos a anadir un nuevo atributo a nuestro objeto user1. 

class Usuario:
    username = "Username por default"
    email = ""


user1 = Usuario()
print(user1.username)

user1.username = "Cody" 
user1.password = "1234" -> Nuevo atributo al objeto.
print(user1.username)


print(id(user1.username))
print(id(Usuario.username))

print(user1.__dict__)

En consola:
Username por default
Cody
2412241627440
2412241641408
{'username': 'Cody', 'password': '1234'}

--> Podemos observar que mi objeto user1 ahora posee dos atributos. 


 Tambien podemos modificar los atributos facilmente, de forma dinamica. Veamos un ejemplo, debajo del print, agreguemos un nuevo valor para password. 


class Usuario:
    username = "Username por default"
    email = ""


user1 = Usuario()
print(user1.username)

user1.username = "Cody" 
user1.password = "1234" -> Nuevo atributo al objeto.
print(user1.username)

print(id(user1.username))
print(id(Usuario.username))

user1.password = "password"

print(user1.__dict__)

En consola:
Username por default
Cody
2412241627440
2412241641408
{'username': 'Cody', 'password': 'password'}

--> Ya tiene un nuevo valor. 

 En la siguiente clase vamos a aprender a estandarizar los atributos para los objetos de una misma clase, de esta forma los objetos que creemos siempre tendran los mismos atributos ya que si bien podemos anadir de forma dinamica los atributos a nuestros objetos no es la mejor practica, ya que si nosotros anadimos de forma dinamica atributos a nuestros objetos de forma indiscriminada al final del dia tendremos objetos los cuales discrepen tanto en cantidad como en nombre de los atributos. Lo recomendable es estandarizar los atributos que posean los objetos. 


----------------------------------------------------
#5) CLASE 5 - METODOS.

  En el video anterior aprendimos que en Python podemos anadir atributos a nuestros objetos en tiempo de ejecucion, esto puede parecer una buena idea pero no lo es, ya que si nosotros no estandarizamos tanto los nombres como la cantidad de atributos que va a poseer un objeto a la larga podemos tener ciertos errores.  

Por ejemplo, en el siguiente caso:

class Usuario:
    username = "Username por default"
    email = " "


user1 = Usuario()
user2 = Usuario()

user1.username = "Cody"
user1.password = "1234"
print(user1.username)

print(id(user1.username))
print(id(Usuario.username))


--> En este caso tenemos dos objetos, los cuales son:

user1 = Usuario()
user2 = Usuario()

... Y ambos objetos son de tipo Usuario. 

 Sin embargo, a pesar que ambos objetos son de la misma clase, los objetos poseen atributos diferentes. Por su parte user1 posee 2 atributos, los cuales son:

user1.username = "Cody"
user1.password = "1234"

Y user2 no posee atributo alguno. 


 Lo cual todo esto desde el punto de vista del profesor esta completamente mal. 

 Lo recomendable es que cuando nosotros creemos objetos de un mismo tipo de clase, estos objetos comiencen con los mismos atributos, que estos objetos se encuentren estandarizados. Ya que si nosotros no hacemos esto es probable que lleguemos a toparnos con objetos los cuales posean mas o menos atributos y eso nos puede ocasionar ciertos problemas. 

 A continuacion, vamos a aprender a estandarizar atributos para nuestros objetos. De tal forma que cuando nosotros creemos objetos de un mismo tipo de clase estos objetos siempre comiencen con la misma cantidad de atributos y los mismos nombres. 

 Para ello vamos a crear un nuevo metodo. Del ejemplo anterior vamos a eliminar todo menos la definicion de la clase. Ejm:

class Usuario:


 Ahora, para que nosotros podamos crear metodos basta con definir funciones dentro de las clases, por ejemplo voy a crear un metodo llamado inicializar y mediante este metodo seremos capaces de inicializar los atributos para nuestros objetos. Entonces sabemos ya que basta con definir una funcion dentro de la clase. Ejm: 

class Usuario:

    def inicializar():
        pass

 
 Ahora, para que esta funcion pueda considerarse un metodo obligatoriamente debe poseer un parametro, parametro el cual hace referencia al objeto perse, al objeto que llama al metodo y por convencion este parametro tendra por nombre "self" haciendo referencia a sigo mismo.  

class Usuario:

    def inicializar(self):
        pass

 Ahora, sabiendo que self hace referencia al objeto perse y como aprendimos en la clase anterior, nosotros podemos anadir atributos a nuestros objetos. Asi que colocamos el objeto + . + el atributo que nosotros queramos anadir. Ejm: 

class Usuario:

    def inicializar(self):
        self.username = " "
        self.password = " "

-> Estos atributos se van a anadir siempre y cuando nosotros llamemos a la funcion inicializar, username y password se anaden al objeto. 


 Ahora, vamos a proceder a crear dos objetos. Ejm:

class Usuario:

    def inicializar(self):
        self.username = " "
        self.password = " "

user1 = Usuario()
user2 = Usuario()

--> Una vez tengamos los objetos vamos a proceder  imprimir en consola los objetos que acabo de crear junto al meta atributo __dict__ para conocer todos aquellos atributos que posean. Ejm:

class Usuario:

    def inicializar(self):
        self.username = " "
        self.password = " "

user1 = Usuario()
user2 = Usuario()

print(user1.__dict__)
print(user2.__dict__)

En consola:
{}
{}

--> En efecto, observamos que ambos objetos no poseen ningun tipo de atributo, los diccionarios se encuentran completamente vacios.  


 Sin embargo si a estos objetos les ejecutamos el metodo inicializar, colocando: user1.inicializar() y user2.inicializar(). Ejm: 

class Usuario:

    def inicializar(self):
        self.username = " "
        self.password = " "

user1 = Usuario()
user2 = Usuario() 

user1.inicializar()
user2.inicializar()

print(user1.__dict__)
print(user2.__dict__)

En consola: 
{'username': ' ', 'password': ' '}
{'username': ' ', 'password': ' '}

--> Podemos ver que en forma dinamica, en tiempo de ejecucion se van a anadir los atributos username y password a los objetos. 

Explicacion textual: 
 Visualizamos que ambos objetos poseen ahora dos atributos, estos atributos se anaden al objeto al momento de llamar al metodo inicializar. Colocamos el objeto (self).username y .password y asignamos un valor, valor que en el ejemplo es un string vacio. Si recordamos, cuando Python nota que estamos asignando un valor a un atributo que no existe dentro del objeto entonces se procede a anadir dicho atributo al objeto y eso es lo que estamos haciendo en esta parte:

def inicializar(self):
        # Anadiendo atributos al objeto.
        self.username = " "
        self.password = " "

... En esta parte estamos anadiendo atributos al objeto y recordemos que el parametros self hace referencia al objeto perse, o sea es como decir user1.username, user1.password y user2.username, user2.password.  


 Como el metodo inicializar unicamente posee el parametro self, nosotros no vamos a colocar argumento alguno al momento de llamar a este metodo en user1.inicializar() y user2.inicializar(), ya que el parametro sera el objeto y como el objeto ya lo hemos definido user1 y user2, no hay necesidad de colocar ningun tipo de argumento.

 Ahora, si nosotros quiseramos inicializar los atributos con algun tipo de valor con algun tipo de valor podemos hacerlo. Por ejemplo, podemos colocar en el metodo inicializar dos parametros mas: username y password. Ejm:

def inicializar(self, username, password):
        self.username = " "
        self.password = " "

 Y tambien vamos a asignar a los atributos de instancia self.username y self.password, dichos valores de los parametros. 

def inicializar(self, username, password):
        self.username = username
        self.password = password

--> Al nosotros hacer esto ahora si hay que colocar argumentos para estos dos parametros, para los parametros username y password. Recordando que al parametro self no hay que colocarle ningun tipo de argumento, ya que por si solo toma al objeto user1 y user2, el parametro self representa al objeto perse. 
 Asi que en user1.inicializar y en user2.inicializar vamos a colocar unicamente dos strings que corresponden respectivamente a los parametros username y password. Ejm: 

user1.inicializar("User1", "password1")
user2.inicializar("User2", "password2")



EJEMPLO COMPLETO: 

class Usuario:

    def inicializar(self, username, password):
        self.username = username
        self.password = password

user1 = Usuario()
user2 = Usuario() 

user1.inicializar("User1", "password1")
user2.inicializar("User2", "password2")

print(user1.__dict__)
print(user2.__dict__)

En consola: 
{'username': 'User1', 'password': 'password1'}
{'username': 'User2', 'password': 'password2'}

--> Ahora estamos creando objetos con la misma cantidad y con los mismos nombres de sus atributos, username y password. Estamos estandarizando los atributos que tendran los objetos de una clase en comun. 
 Todos los objetos de la clase Usuario tendran 2 atributos (los atributos username y password) esto siempre y cuando los objetos llamen a la funcion inicializar. Dentro de esta funcion nosotros anadimos a los atributos de forma dinamica con self.username y self.password a el objeto pudiendo establecer valor por default, como podemos observar viendo user1, user2, password1, password2. 


 Si nosotros por ejemplo creamos un tercer usuario:
 user3 = Usuario:

user3.inicializar("Cody", "password3")

y tambien imprimimos a ese tercer usuario con el meta atributo __dict__ para poder visualizar el contenido de su diccionario. 


EJEMPLO COMPLETO: 

class Usuario:

    def inicializar(self, username, password):
        self.username = username
        self.password = password

user1 = Usuario()
user2 = Usuario() 
user3 = Usuario()

user1.inicializar("User1", "password1")
user2.inicializar("User2", "password2")
user3.inicializar("Cody", "password3")

print(user1.__dict__)
print(user2.__dict__)
print(user3.__dict__)

En consola:
{'username': 'User1', 'password': 'password1'}
{'username': 'User2', 'password': 'password2'}
{'username': 'Cody', 'password': 'password3'}

--> Podemos observar nuevamente la estandarizacion de los atributos, ahora TODOS los objetos de tipo Usuario van a tener por lo menos dos atributos tanto username como password, esto siempre y cuando se mande a llamar al metodo inicializar. 


 Ahora, si bien esto funciona. El que nosotros podamos estandarizar tanto los nombres como la cantidad de atributos que tendran los objetos de una misma clase NO es la mejor forma de hacerlo. Ya que Python internamente maneja el metodo __init__ y mediante este metodo seremos capaces de inicializar los atributos de un objeto al momento de instanciarlo, por lo tanto ya no sera necesario utilizar metodos que nos permitan inicializar atributos, ya que estariamos realizando una tarea doble. 


----------------------------------------------------
#6) CLASE 6 - METODO INIT

 En Python para que nosotros podamos definir e inicializar atributos para un objeto, al momento de crearlo haremos uso del metodo init. 


class Usuario:

    def inicializar(self, username, password):
        self.username = username
        self.password = password

user1 = Usuario()
user2 = Usuario()
user3 = Usuario()

print(user1.__dict__)
print(user2.__dict__)
print(user3.__dict__)

 Vamos a trabajar con el ejemplo anterior, y lo que haremos sera que cuando se cree un objeto de tipo Usuario, obligatoriamente este objeto posea dos atributos username y password, opcionalmente podemos colocar valores para dichos atributos, para ello nos apoyaremos del metodo init. Vamos a hacer lo siguiente:

- Primero, vamos a sobreescribir el metodo init

    def __init__():
        pass

- Como es un metodo, obligatoriamente debe poseer por primer parametro, un parametro el cual haga como referencia al objeto perse. Que por convencion este parametro sera nombrado como self. 

    def __init__(self):
        pass

EJEMPLO COMPLETO:

class Usuario:

    def __init__(self):
        pass

user1 = Usuario()
user2 = Usuario()
user3 = Usuario()

print(user1.__dict__)
print(user2.__dict__)
print(user3.__dict__)


En consola:
{}
{}
{}

--> Esta todo bien, estamos sobreescribiendo el metodo init pero este no realiza absolutamente nada (pass).

 
 Utilizamos la palabra sobreescribir ya que todas las clases en Python, heredan de la clase Object, la clase principal. Clase que posee el metodo init, entonces lo que estamos haciendo es sobreescribir el comportamiento de este metodo. 

 El metodo init se va a llamar cuando nosotros instanciemos un objeto. Entiendase por instanciar un objeto como la creacion del mismo objeto, o sea cuando escribo user1 = Usuario(), user2 = Usuario(), user3 = Usuario(). 
 Veamos un ejemplo, imprimamos en consola un pequeno mensaje:

class Usuario:

    def __init__(self):
        print("Estamos creando un usuario")

user1 = Usuario()
user2 = Usuario()
user3 = Usuario()

print(user1.__dict__)
print(user2.__dict__)
print(user3.__dict__)

En consola:
Estamos creando un usuario
Estamos creando un usuario
Estamos creando un usuario
{}
{}
{}

--> Confirmamos que efectivamente el metodo (def __init__) se va a ejecutar cuando se instancie un objeto, en el ejemplo se instanciaron tres mensajes porque se instanciaron tres objetos. 

 
 Ya con esto en mente podemos hacer lo siguiente en el metodo:

class Usuario:

    def __init__(self):
        self.username = " "
        self.password = " "
 
--> De esta forma la indicamos a Python que cuando nosotros creemos un objeto de tipo Usuario, este objeto obligatoriamente va a poseer dos atributos, tanto username como password y por default estos atributos almacenaran un string vacio. 

EJEMPLO COMPLETO: 

class Usuario:

    def __init__(self):
        self.username = " "
        self.password = " "

user1 = Usuario()
user2 = Usuario()
user3 = Usuario()

print(user1.__dict__)
print(user2.__dict__)
print(user3.__dict__)

En consola:
{'username': '', 'password': ''}
{'username': '', 'password': ''}
{'username': '', 'password': ''}

--> Ahora en efecto los objetos poseen dos atributos, estamos estandarizando nuevamente la cantidad y nombre de atributos que poseeran nuestros objetos. Objetos que corresponden a un mismo tipo de clase.  


 Entonces, reiteramos que el metodo init se va a ejecutar siempre que nosotros creemos un objeto de la clase. 

 Ahora, el metodo init no unicamente nos permite definir que atributos tendra el objeto sino que inclusive podemos inicializarlos, para ello trabajaremos con parametros.

 Por ejemplo creemos un parametro llamado username y uno llamado password, ejm:
    def __init__(self, username, password)

 Mediante estos parametros seremos capaces de obtener los valores de entrada que se hayan colocado al momento de generar, al momento de instanciar el objeto.  Y estos valores simplemente los vamos a asignar a los atributos self.username y self.password, atributos de instancia. Ejm:

    def __init__(self, username, password)
        self.username = username
        self.password = password


EJEMPLO COMPLETO: 

class Usuario:

    def __init__(self, username, password):
        self.username = username
        self.password = password

user1 = Usuario()
user2 = Usuario()
user3 = Usuario()

print(user1.__dict__)
print(user2.__dict__)
print(user3.__dict__)

En consola:
Traceback (most recent call last):
  File "C:\Users\Usuario\Desktop\python\python.programas\modulo_8\metodo_init.py", line 7, in <module>
    user1 = Usuario()
            ^^^^^^^^^
TypeError: Usuario.__init__() missing 2 required positional arguments: 'username' and 'password'

--> Obtenemos un error, ya que se me indica que el metodo init requiere dos argumentos, un argumento para el parametro username y un argumento para el parametro password. Asi que simplemente colocamos los valores en la instancia. Ejm:

user1 = Usuario("user1", "password1")
user2 = Usuario("user2", "password2")
user3 = Usuario("user3", "password3")

-> Estamos creando un objeto (user1, user2, user3) y al momento de crearlo estamos definiendo e inicializando sus atributos. 


EJEMPLO COMPLETO: 

class Usuario:

    def __init__(self, username, password):
        self.username = username
        self.password = password

user1 = Usuario("user1", "password1")
user2 = Usuario("user2", "password2")
user3 = Usuario("user3", "password3")

print(user1.__dict__)
print(user2.__dict__)
print(user3.__dict__)

En consola:
{'username': 'user1', 'password': 'password1'}
{'username': 'user2', 'password': 'password2'}
{'username': 'user3', 'password': 'password3'}

--> Listo, todo correcto. 


 Entonces, ya vemos que de esta forma tan sencilla seremos capaces de definir e inicializar atributos para nuestros objetos de una misma clase. 
 En este caso le estamos indicando a Python que todos los objetos de tipo Usuario van a poseer dos atributos, el atributo username y el atributo password, mas adelante el objeto puede poseer mas atributos pero cuando se crea obligatoriamente tendra estos dos. De igual forma la indicamos que al momento de isnstanciar el objeto, obligatoriamente debe colocar dos valores para dichos parametros (username y password), colocamos los argumentos y listo.


 Para finalizar es importante mencionar que todo lo que hemos aprendido acerca de las funciones aplica para los metodos. Por ejemplo nosotros pudiesemos crear parametros los cuales tengan valores por default. Ejm:

    def __init__(self, username="", password=""):

 Y nosotros pudiesemos crear objetos los cuales utilicen estos valores por default. En el ejemplo el objeto que creamos para que utilice los valores por default es user4 = Usuario().

EJEMPLO COMPLETO:

class Usuario:

    def __init__(self, username="", password=""):
        self.username = username
        self.password = password

user1 = Usuario("user1", "password1")
user2 = Usuario("user2", "password2")
user3 = Usuario("user3", "password3")
        
user4 = Usuario()

print(user1.__dict__)
print(user2.__dict__)
print(user3.__dict__)
print(user4.__dict__)

--> Los primero tres objetos establecen su username y su password, y el cuarto objeto utiliza los valores por default que posean los parametros.

En consola: 
{'username': 'user1', 'password': 'password1'}
{'username': 'user2', 'password': 'password2'}
{'username': 'user3', 'password': 'password3'}
{'username': '', 'password': ''}

--> Perfecto, el ultimo objeto posee strings vacios para sus atributos. 


----------------------------------------------------
#7) CLASE 7 - HERENCIA.

 Para explicar la herencia, estaremos trabajando con dos nuevas clases. La clase Mascota y la clase Perro, vamos a hacer que ambas clases tengan una relacion, una relacion de herencia, la clase Mascota es la clase padre, y la clase Perro es la clase hija, perro va a heredar de la clase Mascota. 

class Mascota: # Clase Padre
    pass

class Perro: # Clase Hija
    pass

 En Python, para que nosotros podamos hereder de otra clase debemos hacer lo siguiente: Despues de el nombre de la clase vamos a colocar parentesis y dentro de los parentesis vamos a colocar la clase de la cual queremos heredar, en este caso la clase Perro va a heredar de la clase Mascota. Ejm:

class Mascota: # Clase Padre
    pass

class Perro(Mascota): # Clase Hija
    pass

 Al nosotros hacer esto, los objetos de tipo Perro facilmente podran acceder a todos aquellos atributos y metodos que se encuentren dentro de la clase Mascota.  
 Por ejemplo, vamos a definir una par de metodos dentro de la clase Mascota, metodos que solo van a imprimir un pequeno mensaje en consola. 

class Mascota:
    
    def comer(self):
        print("La mascota come.")

    def dormir(self):
        print("La mascota duerme.")

class Perro:
    pass


--> La clase Mascota ahora posee dos metodos, metodos los cuales pueden facilmente ser utilizados por todos aquellos objetos de tipo Perro.


 Ahora, vamos a crear un objeto llamado duke que sera igual a un objeto de tipo Perro.

duke = Perro()


 Como el objeto es de tipo Perro, y como la clase Perro hereda de la clase Mascota, este objeto duke = Perro() facilmente puede utilizar los metodos y atributos que se encuentren dentro de Mascota. Por ejemplo:

duke.comer()
duke.dormir()

-> Estos metodos no se encuentran dentro de la clase Perro, pero si se encuentra dentro de la clase Mascota pero como la clase Perro hereda de la clase Mascota, todos los objetos de ese tipo pueden acceder a la clase padre.

EJEMPLO COMPLETO:

class Mascota:
    
    def comer(self):
        print("La mascota come.")

    def dormir(self):
        print("La mascota duerme.")

class Perro(Mascota):
    pass

duke = Perro()

duke.comer()
duke.dormir()

En consola:
La mascota come.
La mascota duerme.

--> Perfecto, visualizamos los dos mensajes. 


 Ahora, algo importante a mencionar es que una clase puede convertirse en clase padre una "n" cantidad de veces. 

 Por ejemplo, si yo definiera una nueva clase Gato, y quiero que la clase Gato herede de la clase Mascota, podemos hacerlo, basta nuevamente con colocar Mascota dentro de los parentesis, ejm:

class Gato(Mascota):

--> Y de igual forma todos aquellos objetos de tipo Gato podran acceder a los atributos y metodos de la clase Mascota. Ejm, vamos a crear un objeto llamado:

patricio = Gato()

patricio.comer()
patricio.dormir()


EJEMPLO COMPLETO:

class Mascota:
    
    def comer(self):
        print("La mascota come.")

    def dormir(self):
        print("La mascota duerme.")

class Perro(Mascota):
    pass

class Gato(Mascota):

duke = Perro()

duke.comer()
duke.dormir()

patricio = Gato

patricio.comer()
patricio.dormir()

En consola: 
La mascota come.
La mascota duerme.
La mascota come.
La mascota duerme.

--> Visualizamos los mensajes dos veces, una vez por cada mascota. 


----------------------------------------------------
#8) CLASE 8 - HERENCIA MULTIPLE.

 Algo interesante de Python, con respecto al tema de herencia es que a diferencia de otros lenguajes de programacion Python permite la herencia multiple. 
 Esto quiere decir que una clase puede heredar de multiples clases, lo cual por supuesto tiene muchas ventajas. Veamos un ejemplo: Para este video nuevamente estaremos trabajando con la clase Gato y con la clase Mascota.

class Mascota:
    def comer(self):
        print("La mascosta come.")

    def dormir(self):
        print("La mascota duerme.")

class Gato(Mascota):
    pass

--> En este caso como podemos observar, la clase Gato hereda de la clase Mascota. Y lo que vamos a hacer en este video es implementar la herencia multiple, vamos a hacer que la clase Gato herede de 2 clases, de la clase Mascota y de una nueva clase que vamos a crear a continuacion llamada Felino. 


class Mascota:

    def comer(self):
        print("La mascota come.")

    def dormir(self):
        print("La mascota duerme.")

class Felino:

    def cazar(self):
        print("El felino caza.")

--> Ahora vamos a hacer que la clase Gato, herede tanto de la clase Mascota como de la clase Felino. Y para ello es algo bastante sencillo, unicamente vamos a colocar dentro de los parentesis y separadas por una coma, todas aquellas clases de las cuales queramos heredar. Ejm:

class Gato(Mascota, Felino):
    pass
    
--> De esta forma la clase Gato hereda de dos clases, estamos implementando la herencia multiple. Todos los objetos de tipo Gato facilmente pueden acceder tanto a los atributos y metodos de la clase Mascota y de la clase Felino.  

EJEMPLO COMPLETO, creando un de tipo Gato:

class Mascota:

    def comer(self):
        print("La mascota come.")

    def dormir(self):
        print("La mascota duerme.")

class Felino:

    def cazar(self):
        print("El felino caza.")

class Gato(Mascota, Felino):
    pass

patricio = Gato()

-> Este objeto es de tipo Gato, y la clase Gato hereda tanto de Mascota como de Felino, este objeto puede acceder tanto a los atributos y metodos de las clases padre. Ejm:


patricio.comer()
patricio.dormir()

patricio.cazar()



EJEMPLO COMPLETO: 

class Mascota:

    def comer(self):
        print("La mascota come.")

    def dormir(self):
        print("La mascota duerme.")


class Felino:

    def cazar(self):
        print("El felino caza.")

class Gato(Mascota, Felino):
    pass

patricio = Gato()

patricio.comer()
patricio.dormir()

patricio.cazar()

En consola:
La mascota come.
La mascota duerme.
El felino caza.

--> Visualizamos los 3 mensajes. 

 Con esto confirmamos que en Python es posible la herencia multiple, esto tiene muchas ventajas, sobre todo cuando queremos extender funcionalidades para nuestros objetos. 


 Es importante mencionar que las clases padre de igual forma pueden convertirse en clases hijas, estas clases de igual forma pueden heredar de otras clases.
 Veamos, vamos a abstraer un poco mas el tema de las mascotas. Vamos a crear una nueva clase aun mas abstracta llamada Animal y va a estar por encima de la clase Mascota, esta clase sera la clase padre de la clase Mascota, o sea Mascota hereda de Animal. Y para ser un poco mas abstractos en nuestra forma de pensar, comer y dormir son acciones que hacen los animales asi que vamos a mover los metodos que estan en la clase Mascota a la clase Animal. Ejm:


class Animal:
    def comer(self):
        print("El animal come.")

    def dormir(self):
        print("El animal duerme.")

class Mascota(Animal):
    pass

class Felino:
    def cazar(self):
        print("El felino caza.")

class Gato(Mascota, Felino):
    pass


patricio = Gato()

patricio.comer()
patricio.dormir()

patricio.cazar()


En consola:
El animal come.
El animal duerme.
El felino caza.

--> Ahora, la clase Gato hereda de la clase Mascota que a su vez la clase Mascota hereda de la clase Animal. Como Gato es un animal, indirectamente por ser una mascota entonces Gato puede comer y puede dormir. Ya que estos metodos se encuentran dentro de la clase padre. 

NOTA: Entre mas nivel jerarquico tenga una clase, esta se volvera mas abstracta y por supuesto a la inversa, entre menos nivel jerarquico tenga una clase esta sera mas concreta. 


----------------------------------------------------
#8) CLASE 8 - SOBRE ESCRITURA DE METODOS.

 La sobreescritura de metodos o tambien conocida como la sobrecarga de metodos, es uno de los temas principales al momento de trabajar con programacion orientada a objetos y consiste principalmente en que una clase hija puede modificar el comportamiento de los metodos de la clase padre, esto con la finalidad de que estos comportamientos se adecuen a las necesidades de la clase hija, veamos un ejemplo: 

- Para este video estaremos trabajando con las siguientes clases:

class Animal:

    def comer(self):
        print("El animal come.")

    def dormir(self):
        print("El animal duerme.")

class Mascota(Animal):
    pass

class Felino:

    def cazar(self):
        print("El felino caza.")

class Gato(Mascota, Felino):
    pass


--> Vamos a modificar el comportamiento del metodo comer y del metodo dormir, los dos metodos que se encuentran dentro de la clase Animal. Vamos a modificar los mensajes que se imprimen en consola para que se adecuen a la clase Gato, ya que sabemos los animales tienen diferentes formas de comer y de dormir, en este caso vamos a modificar el comportamiento para un animal en concreto, para que se adecue mas a un gato.  

Entonces, en la clase Gato:

- Definimos el metodo __init__ , si recordamos el metodo init nos permite tanto establecer como inicializar los atributos para nuestros objetos. En este caso quiero que cuando un objeto de tipo Gato se cree, se le coloque un nombre, asi que procedo a anadir el atributo "nombre" a el objeto, de esta forma: Agregando nombre dentro de los parentesis y luego: self.nombre = nombre

    def __init__(self, nombre):
        self.nombre = nombre


- Posteriormente voy a crear el objeto gato y le colocamos un nombre dentro de los parentesis:

patricio = Gato("Patricio") 

- Posteriormente voy a ejecutar tanto el metodo comer como el metodo dormir. 

patricio.comer()
patricio.dormir()



EJEMPLO COMPLETO:

class Animal:

    def comer(self):
        print("El animal come.")

    def dormir(self):
        print("El animal duerme.")

class Mascota(Animal):
    pass

class Felino:

    def cazar(self):
        print("El felino caza.")

class Gato(Mascota, Felino):

    def __init__(self, nombre):
        self.nombre = nombre

patricio = Gato("Patricio")

patricio.comer()
patricio.dormir()


En consola:
El animal come.
El animal duerme.

--> Vemos los mensajes que se encuentran dentro de la clase padre. Nada nuevo. 


¿¿¿PERO, COMO FUNCIONA INTERNAMENTE PYTHON CON EL TEMA DE HERENCIA???

R-> En este caso "patricio.comer" el objeto Gato intenta ejecutar el metodo comer, lo que hace Python es lo siguiente: Primero va a buscar si el metodo comer se encuentra dentro de la clase Gato, la clase a la cual pertenece el objeto. Como este objeto no se encuentra dentro de la clase va a buscar en un nivel superior, va a buscar en las clases de las cuales hereda, en el ejemplo la clase Gato va a asi: class Gato(Mascota, Felino) y comienza a buscar leyendo de izquierda a derecha, primero va a buscar dentro de la clase Mascota y luego va a buscar dentro de la clase Felino. Estando en la clase Mascota al percatarse de que el metodo comer tampoco existe, entonces sube otro nivel jerarquico, va a buscar dentro de la clase Animal y como en este caso la clase Animal si posee el metodo comer entonces se ejecuta dicho metodo. De esta forma es como Python va a buscar lo metodos que se encuentren dentro de clases padre. 

 Y si por ejemplo dentro de la clase Mascota, que es la segunda clase inmediata, nosotros sobreescribimos el metodo comer (que para que nosotros podamos sobreescibir un metodo basta con volverlo a definir) por ejemplo:

class Mascota(Animal):

    def comer(self):
        print("La mascota come")

--> Al momento de ejecutar el mensaje va a cambiar para el metodo comer, va a tomar el que esta en la clase Mascota. Entonces resumiendo, como la clase Gato no posee el metodo comer, lo busca en la clase Mascota y como la clase Mascota si posee el metodo comer ya no hay necesidad de buscar en la clase padre Animal.

 De esta forma es como nosotros podemos sobre escribir metodos en Python, simplemente basta con volver a definir dicho metodo. 

 
 A continuacion vamos a sobre escribir los metodos comer y dormir para la clase Gato. Vamos a agregar el nombre Patricio en los metodos comer y dormir.

class Gato(Mascota, Felino):

    def __init__(self, nombre):
        self.nombre = nombre

--> Aca definimos el metodo init y agregamos el atributo nombre al objeto. 

  
Ahora, colocamos la funcion comer y dormir, y vamos a imprimir en consola mediante un f string el nombre del gato. Ejm:

    def comer(self):
        print(f'{self.nombre}' come.)


    def dormir(self):
        print(f'{self.nombre}' duerme.)


EJEMPLO COMPLETO:

class Gato(Mascota, Felino):

    def __init__(self, nombre):
        self.nombre = nombre

    def comer(self):
        print(f'{self.nombre}' come.)

    def dormir(self):
        print(f'{self.nombre}' duerme.)

patricio = Gato("Patricio")

patricio.comer()
patricio.dormir()

--> De esta manera agregamos el nombre del gato a la clase Gato.



 Entonces, recordemos. Para que nosotros podamos sobre escribir un metodo basta con definir el metodo dentro de la clase hija, y dentro de este nuevo metodo basta con definir el nuevo comportamiento que nosotros deseemos. 


----------------------------------------------------
#9) CLASE 9 - SOBRE ESCRITURA DE METODOS PT2.


 Habra ocasiones en las cuales a pesar que nosotros ya hayamos sobre escrito los metodos de la clase padre tengamos la necesidad de obligatoriamente ejecutarlos, en estos casos lo mejor que podemos hacer es simplemente utilizar la funcion super. 

 La funcion super nos permite acceder a la clase padre inmediata la cual facilmente podemos utilizar para ejecutar sus metodos, veamos un ejemplo: 

 Trabajamos con el ejemplo de la clase pasada:

class Animal:

    def comer(self):
        print("El animal come.")

    def dormir(self):
        print("El animal duerme.")


class Mascota(Animal):

    def comer(self):
        print("La mascota come.")


class Felino:

    def cazar(self):
        print("El felino caza.")


class Gato(Mascota, Felino):

    def __init__(self, nombre):
        self.nombre = nombre

    def comer(self):
        print(f'{self.nombre} come.')


patricio = Gato("Patricio")

patricio.comer()


En consola: 
Patricio come.
 

--> En este caso, podemos observar que hemos sobre escrito el metodo comer. Sobre escribimos el metodo comer en la clase Gato. 


 ¿¿¿QUE PASA SI YO DESEO EJECUTAR DENTRO DEL METODO COMER, EL METODO COMER DE LA CLASE PADRE, DE LA CLASE MASCOTA???

--> Para ello voy a colocar en el metodo comer de la clase Gato la palabra super seguida de parentesis y posteriormente ejecuto el metodo comer, metodo que se encuentra dentro de la clase padre. Ya que la funcion super nos permite acceder al padre inmediato de la clase, que en este caso seria Mascota. Ejm:

    def comer(self):
        super().comer()
        print(f'{self.comer} come.')


EJEMPLO COMPLETO:

class Animal:

    def comer(self):
        print("El animal come.")

    def dormir(self):
        print("El animal duerme.")


class Mascota(Animal):

    def comer(self):
        print("La mascota come.")


class Felino:

    def cazar(self):
        print("El felino caza.")


class Gato(Mascota, Felino):

    def __init__(self, nombre):
        self.nombre = nombre

    def comer(self):
        super().comer()
        print(f'{self.comer} come.')


patricio = Gato("Patricio")

patricio.comer()


En consola: 
La mascota come.

--> Podemos ver como se ejecuta el metodo de nuestra clase padre de manera correcta. 


 De esta forma tan sencilla es como nosotros podemos ejecutar metodos de nuestra clase padre, haciendo uso de la funcion super()


----------------------------------------------------
#10) CLASE 10 - METODOS DE CLASE.

 Al igual que con los atributos, a los metodos los podemos clasificar en 2 tipos.
 Serian los metodos de instancia, metodos los cuales le pertenecen a los objetos y a los metodos de clase, metodos los cuales le pertenecen a la clase. 

 Como ya hemos aprendido a crear metodos de instancia, ahora vamos a aprender a crear metodos de clase, y para ello estaremos utilizando decoradores. 


- Para esta clase estaremos trabajando con la clase Circulo:

class circulo():

- Esta clase poseera un atributo de clase, que sera pi y vamos a almacenar parte de la constante:


class circulo():

    pi = 3.141592


- Posteriormente vamos a crear el metodo de clase, para ello vamos a definir un metodo que en este caso tendra por nombre area(), mediante este metodo seremos capaces de calcular el area de un circulo. 

class circulo():

    pi = 3.141592

    def area():
        pass 


- En el metodo de clase, debemos colocar de forma obligatoria un objeto el cual represente a la clase perse, a la clase circulo. Y por convencion, como queremos que este metodo sea un metodo de clase, el parametro tendra por nombre cls (parametro que hace referencia a la clase). Posteriormente vamos a colocar todos aquellos paremetros necesarios para que el metodo funcione, en este caso seria el radio.  

class circulo():

    pi = 3.141592

    def area(cls, radio):
        pass 

- Vamos ahora en el metodo a retornar pi, que le pertenece a la clase, entonces colocamos cls.pi por radio al cuadrado -> De esta forma quedaria la formula, para calcular el area de un circulo: pi * radio al cuadrado.  


class circulo():

    pi = 3.141592

    def area(cls, radio):
        return cls.pi * (radio ** 2)


 Sin embargo si nosotros dejamos el metodo tal y como se encuentra actualmente, este sera un metodo de instancia. A pesar de haberle colocado cls como primer parametro. Bueno, como hemos mencionado anteriormente cls es unicamente por convencion al igual que self. Entonces, internamente Python toma este metodo como un metodo de instancia y no como un metodo de clase, asi que para que nosotros podamos convertir este metodo de instancia a un metodo de clase, vamos a decorar utilizando @classmethod, ejm: 

class circulo():

    pi = 3.141592

    @classmethod
    def area(cls, radio):
        return cls.pi * (radio ** 2)


--> Con esto le indicamos a Python que ahora el metodo area, es un metodo de clase. Un metodo el cual pertenece a la clase, y para que podamos utilizar este metodo lo haremos a traves de la clase y no a traves de un objeto. 
Veamos:

- Vamos a imprimir el resultado de calcular el area del circulo que tiene por radio 14. 

resultado = Circulo.area(14)

 => Colocamos la clase + . + el metodo de clase que queremos utilizar y pasamos como argumento radio. 
 Ya no hay que colocar argumento para cls puesto que ya hemos definido la clase en Circulo.area y si recordamos cls hace referencia a la clase perse. En este caso (return cls.pi *(radio ** 2)) la utilizamos para acceder a su atributo pi.


EJEMPLO COMPLETO IMPRIMIENDO RESULTADO:

class Circulo():

    pi = 3.141592

    @classmethod
    def area(cls, radio):
        return cls.pi * (radio ** 2)

resultado = Circulo.area(14)
print(resultado)

En consola:
615.752032

--> Visualizamos el area del circulo. Podemos confirmar que el metodo area es un metodo de clase, puesto que lo estamos utilizando directamente con la clase Circulo, sin la necesidad de crear un objeto. 


- COMPRAR EL BLOCK DE NOTAS PARA PYTHON Y UN BOLIGRAFO.
- COMENZAR CON LAS PRACTICAS.
- REPASO Y EXAMEN.






